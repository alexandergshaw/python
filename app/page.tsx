"use client";

import { useEffect, useMemo, useState } from "react";
import { loadPyodide, type PyodideInterface } from "pyodide";

type AssignmentId =
  | "assignment0"
  | "assignment1"
  | "assignment2"
  | "assignment3"
  | "review1"
  | "exam1"
  | "assignment4"
  | "assignment5"
  | "assignment6"
  | "assignment7"
  | "assignment8"
  | "assignment9"
  | "assignment10"
  | "review2"
  | "exam2"
  | "final";

type AssignmentMeta = {
  id: AssignmentId;
  title: string;
  week: string;
};

type DashboardPayload = {
  title: string;
  values: number[];
  labels: string[];
};

type AssignmentStatus = {
  id: AssignmentId;
  title: string;
  week: string;
  complete: boolean;
  payload: DashboardPayload | null;
  message: string;
};

const ASSIGNMENTS: AssignmentMeta[] = [
  { id: "assignment0", title: "Setup, Git, Vercel", week: "Week 1" },
  { id: "assignment1", title: "Variables, I/O, Branching", week: "Week 1" },
  { id: "assignment2", title: "Conditionals, Testing", week: "Week 2" },
  { id: "assignment3", title: "Loops", week: "Week 3" },
  { id: "review1", title: "Review: Fundamentals", week: "Week 5" },
  { id: "exam1", title: "Test 1 Prep", week: "Week 6" },
  { id: "assignment4", title: "Functions, Modularization", week: "Week 7" },
  { id: "assignment5", title: "Data Structures", week: "Week 8" },
  { id: "assignment6", title: "File I/O, Error Handling", week: "Week 9" },
  { id: "assignment7", title: "OOP: Classes", week: "Week 10" },
  { id: "assignment8", title: "Advanced OOP", week: "Week 11" },
  { id: "assignment9", title: "Lambdas/Decorators", week: "Week 12" },
  { id: "assignment10", title: "CI/CD, Debugging", week: "Week 13" },
  { id: "review2", title: "Review: OOP/Advanced", week: "Week 14" },
  { id: "exam2", title: "Test 2 Prep", week: "Week 15" },
  { id: "final", title: "Final Integration", week: "Week 16" },
];

function isValidPayload(payload: unknown): payload is DashboardPayload {
  if (!payload || typeof payload !== "object") {
    return false;
  }

  const typedPayload = payload as Record<string, unknown>;
  const { title, values, labels } = typedPayload;

  if (typeof title !== "string" || title.trim().length === 0) {
    return false;
  }

  if (!Array.isArray(values) || !Array.isArray(labels)) {
    return false;
  }

  if (values.length < 3 || labels.length !== values.length) {
    return false;
  }

  const numericValues = values.map((value) => Number(value));
  if (numericValues.some((value) => !Number.isFinite(value))) {
    return false;
  }

  if (new Set(numericValues).size < 2) {
    return false;
  }

  return labels.every((label) => typeof label === "string" && label.trim().length > 0);
}

async function evaluateAssignment(pyodide: PyodideInterface, assignment: AssignmentMeta): Promise<AssignmentStatus> {
  const response = await fetch(`/api/student-code?assignment=${assignment.id}`);
  if (!response.ok) {
    return {
      ...assignment,
      complete: false,
      payload: null,
      message: "Could not load student_code.py",
    };
  }

  const { code } = (await response.json()) as { code: string };
  try {
    pyodide.runPython(code);
  } catch {
    return {
      ...assignment,
      complete: false,
      payload: null,
      message: "Fix Python syntax errors in student_code.py.",
    };
  }

  if (!pyodide.globals.has("get_dashboard_payload")) {
    return {
      ...assignment,
      complete: false,
      payload: null,
      message: "Add get_dashboard_payload() to unlock this widget.",
    };
  }

  const exportedFunction = pyodide.globals.get("get_dashboard_payload") as {
    destroy?: () => void;
    (): unknown;
  };

  let rawPayload: unknown;
  try {
    rawPayload = await exportedFunction();
  } catch {
    return {
      ...assignment,
      complete: false,
      payload: null,
      message: "get_dashboard_payload() raised an error.",
    };
  } finally {
    exportedFunction.destroy?.();
  }

  const payload =
    rawPayload && typeof (rawPayload as { toJs?: () => unknown }).toJs === "function"
      ? ((rawPayload as { toJs: () => unknown }).toJs() as unknown)
      : rawPayload;
  if (rawPayload && typeof (rawPayload as { destroy?: () => void }).destroy === "function") {
    (rawPayload as { destroy: () => void }).destroy();
  }

  if (!isValidPayload(payload)) {
    return {
      ...assignment,
      complete: false,
      payload: null,
      message: "Return non-trivial title/labels/values data to unlock.",
    };
  }

  return {
    ...assignment,
    complete: true,
    payload,
    message: "Widget unlocked",
  };
}

export default function Home() {
  const [statuses, setStatuses] = useState<AssignmentStatus[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    let mounted = true;

    async function loadDashboard() {
      try {
        const pyodide = await loadPyodide();
        const nextStatuses: AssignmentStatus[] = [];

        for (const assignment of ASSIGNMENTS) {
          if (pyodide.globals.has("get_dashboard_payload")) {
            pyodide.globals.delete("get_dashboard_payload");
          }

          const status = await evaluateAssignment(pyodide, assignment);
          nextStatuses.push(status);
        }

        if (mounted) {
          setStatuses(nextStatuses);
        }
      } catch {
        if (mounted) {
          setStatuses(
            ASSIGNMENTS.map((assignment) => ({
              ...assignment,
              complete: false,
              payload: null,
              message: "Pyodide failed to initialize.",
            })),
          );
        }
      } finally {
        if (mounted) {
          setLoading(false);
        }
      }
    }

    void loadDashboard();

    return () => {
      mounted = false;
    };
  }, []);

  const unlockedWidgets = useMemo(
    () => statuses.filter((status) => status.complete && status.payload),
    [statuses],
  );

  return (
    <div className="min-h-screen bg-slate-50 text-slate-900">
      <main className="mx-auto flex w-full max-w-7xl gap-6 p-6 md:p-10">
        <aside className="w-full max-w-xs rounded-xl border border-slate-200 bg-white p-4 shadow-sm">
          <h1 className="text-lg font-semibold">Course Progress</h1>
          <p className="mt-1 text-sm text-slate-600">Complete each student_code.py to unlock dashboard widgets.</p>
          <ul className="mt-4 space-y-3">
            {(loading ? ASSIGNMENTS : statuses).map((assignment) => {
              const complete = !loading && statuses.find((s) => s.id === assignment.id)?.complete;
              return (
                <li key={assignment.id} className="rounded-lg border border-slate-200 p-3">
                  <div className="flex items-center justify-between gap-2">
                    <span className="text-sm font-medium">{assignment.id}</span>
                    <span
                      className={`rounded-full px-2 py-0.5 text-xs font-medium ${
                        complete ? "bg-emerald-100 text-emerald-700" : "bg-amber-100 text-amber-800"
                      }`}
                    >
                      {complete ? "Complete" : "Locked"}
                    </span>
                  </div>
                  <p className="mt-1 text-xs text-slate-600">{assignment.week}</p>
                  <p className="text-xs text-slate-700">{assignment.title}</p>
                </li>
              );
            })}
          </ul>
        </aside>

        <section className="flex-1 rounded-xl border border-slate-200 bg-white p-5 shadow-sm">
          <h2 className="text-lg font-semibold">Personal Data Dashboard</h2>
          <p className="mt-1 text-sm text-slate-600">
            Widgets appear automatically when `get_dashboard_payload()` returns valid, non-trivial data.
          </p>

          <div className="mt-5 grid gap-4 md:grid-cols-2">
            {unlockedWidgets.map((status) => (
              <article key={status.id} className="rounded-lg border border-slate-200 p-4">
                <h3 className="text-sm font-semibold">{status.payload?.title}</h3>
                <table className="mt-2 w-full text-left text-sm">
                  <tbody>
                    {status.payload?.labels.map((label, index) => (
                      <tr key={`${status.id}-${label}-${index}`}>
                        <td className="py-1 text-slate-600">{label}</td>
                        <td className="py-1 font-medium">{status.payload?.values[index]}</td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </article>
            ))}
          </div>

          {!loading && unlockedWidgets.length === 0 && (
            <p className="mt-5 rounded-lg border border-dashed border-slate-300 p-4 text-sm text-slate-600">
              No widgets unlocked yet. Start with `assignments/assignment0/student_code.py`.
            </p>
          )}

          {!loading && statuses.length > 0 && statuses.every((status) => status.complete) && (
            <p className="mt-5 rounded-lg border border-emerald-200 bg-emerald-50 p-4 text-sm text-emerald-800">
              Final Project Integration unlocked: all widgets are now displayed.
            </p>
          )}
        </section>
      </main>
    </div>
  );
}
