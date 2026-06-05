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

/** Skeleton shimmer block shown while Pyodide is loading */
function SkeletonCard() {
  return (
    <div className="animate-pulse rounded-xl border p-4" style={{ borderColor: "var(--border-subtle)", background: "var(--bg-card)" }}>
      <div className="mb-3 h-3 w-2/3 rounded-full" style={{ background: "var(--border-subtle)" }} />
      <div className="space-y-2">
        <div className="h-2 rounded-full" style={{ background: "var(--border-subtle)" }} />
        <div className="h-2 w-4/5 rounded-full" style={{ background: "var(--border-subtle)" }} />
        <div className="h-2 w-3/5 rounded-full" style={{ background: "var(--border-subtle)" }} />
      </div>
    </div>
  );
}

/** Mini bar for the dashboard widget — renders a proportional bar next to each value */
function MiniBar({ value, max }: { value: number; max: number }) {
  const pct = max > 0 ? Math.max(2, Math.round((Math.abs(value) / max) * 100)) : 2;
  return (
    <div className="mt-0.5 h-1.5 rounded-full" style={{ background: "var(--border-subtle)" }}>
      <div
        className="h-full rounded-full transition-all duration-500"
        style={{
          width: `${pct}%`,
          background: "linear-gradient(90deg, var(--accent-500), var(--accent-violet))",
        }}
      />
    </div>
  );
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

  const completedCount = useMemo(() => statuses.filter((s) => s.complete).length, [statuses]);
  const allComplete = !loading && statuses.length > 0 && statuses.every((s) => s.complete);

  return (
    <div className="min-h-screen" style={{ background: "var(--bg-base)" }}>
      {/* ── Top bar ────────────────────────────────────────────────────── */}
      <header
        className="sticky top-0 z-20 flex items-center justify-between px-6 py-3"
        style={{
          background: "rgba(8,11,18,0.85)",
          backdropFilter: "blur(12px)",
          borderBottom: "1px solid var(--border-subtle)",
        }}
      >
        <div className="flex items-center gap-3">
          {/* Logo mark */}
          <div
            className="flex h-8 w-8 items-center justify-center rounded-lg text-sm font-bold text-white"
            style={{ background: "linear-gradient(135deg, var(--accent-600), var(--accent-violet))" }}
          >
            Py
          </div>
          <span className="text-sm font-semibold" style={{ color: "var(--text-primary)" }}>
            Personal Data Dashboard Course
          </span>
        </div>

        {/* Global progress pill */}
        {!loading && (
          <div
            className="flex items-center gap-2 rounded-full px-3 py-1 text-xs font-medium"
            style={{ background: "var(--bg-surface)", border: "1px solid var(--border-subtle)", color: "var(--text-secondary)" }}
          >
            <span
              className="h-2 w-2 rounded-full"
              style={{ background: allComplete ? "var(--complete-fg)" : "var(--accent-500)" }}
            />
            {completedCount} / {ASSIGNMENTS.length} complete
          </div>
        )}
      </header>

      <main className="mx-auto flex w-full max-w-7xl gap-6 px-4 py-8 md:px-8">
        {/* ── Sidebar ──────────────────────────────────────────────────── */}
        <aside
          className="w-full max-w-[260px] shrink-0 self-start rounded-2xl p-4"
          style={{
            background: "var(--bg-surface)",
            border: "1px solid var(--border-subtle)",
            boxShadow: "var(--shadow-card)",
            position: "sticky",
            top: "64px",
          }}
        >
          <h1 className="text-base font-bold gradient-text">Course Progress</h1>
          <p className="mt-1 text-xs leading-relaxed" style={{ color: "var(--text-secondary)" }}>
            Complete each <code className="rounded px-1 py-0.5 font-mono text-[10px]" style={{ background: "var(--bg-card)", color: "var(--accent-400)" }}>student_code.py</code> to unlock dashboard widgets.
          </p>

          {/* Progress bar */}
          {!loading && (
            <div className="mt-3">
              <div className="mb-1 flex justify-between text-[10px]" style={{ color: "var(--text-muted)" }}>
                <span>Progress</span>
                <span>{Math.round((completedCount / ASSIGNMENTS.length) * 100)}%</span>
              </div>
              <div className="h-1.5 rounded-full" style={{ background: "var(--border-subtle)" }}>
                <div
                  className="h-full rounded-full transition-all duration-700"
                  style={{
                    width: `${(completedCount / ASSIGNMENTS.length) * 100}%`,
                    background: "linear-gradient(90deg, var(--accent-500), var(--accent-violet))",
                  }}
                />
              </div>
            </div>
          )}

          <ul className="mt-4 space-y-1.5">
            {(loading ? ASSIGNMENTS : statuses).map((assignment) => {
              const complete = !loading && statuses.find((s) => s.id === assignment.id)?.complete;
              return (
                <li
                  key={assignment.id}
                  className="group rounded-xl p-2.5 transition-colors duration-150"
                  style={{
                    background: complete ? "rgba(52,211,153,0.07)" : "var(--bg-card)",
                    border: `1px solid ${complete ? "rgba(52,211,153,0.25)" : "var(--border-subtle)"}`,
                  }}
                >
                  <div className="flex items-center justify-between gap-1">
                    <span
                      className="truncate text-xs font-semibold"
                      style={{ color: complete ? "var(--complete-fg)" : "var(--text-primary)" }}
                    >
                      {assignment.id}
                    </span>
                    <span
                      className="shrink-0 rounded-full px-1.5 py-0.5 text-[10px] font-bold uppercase tracking-wide"
                      style={
                        loading
                          ? { background: "var(--border-subtle)", color: "var(--text-muted)" }
                          : complete
                          ? { background: "var(--complete-bg)", color: "var(--complete-fg)" }
                          : { background: "var(--locked-bg)", color: "var(--locked-fg)" }
                      }
                    >
                      {loading ? "…" : complete ? "✓ done" : "locked"}
                    </span>
                  </div>
                  <p className="mt-0.5 text-[10px]" style={{ color: "var(--text-secondary)" }}>
                    {assignment.week} — {assignment.title}
                  </p>
                </li>
              );
            })}
          </ul>
        </aside>

        {/* ── Main panel ───────────────────────────────────────────────── */}
        <section className="min-w-0 flex-1">
          {/* Panel header */}
          <div
            className="mb-6 rounded-2xl p-5"
            style={{
              background: "linear-gradient(135deg, var(--bg-surface) 0%, #12192e 100%)",
              border: "1px solid var(--border-subtle)",
              boxShadow: "var(--shadow-card)",
            }}
          >
            <h2 className="text-xl font-bold gradient-text">Personal Data Dashboard</h2>
            <p className="mt-1 text-sm" style={{ color: "var(--text-secondary)" }}>
              Widgets appear automatically when{" "}
              <code
                className="rounded px-1.5 py-0.5 font-mono text-xs"
                style={{ background: "var(--bg-card)", color: "var(--accent-400)" }}
              >
                get_dashboard_payload()
              </code>{" "}
              returns valid, non-trivial data.
            </p>
          </div>

          {/* Widget grid */}
          <div className="grid gap-4 sm:grid-cols-2">
            {loading
              ? Array.from({ length: 4 }).map((_, i) => <SkeletonCard key={i} />)
              : unlockedWidgets.map((status) => {
                  const vals = status.payload!.values;
                  const maxVal = Math.max(...vals.map(Math.abs));
                  return (
                    <article
                      key={status.id}
                      className="card-complete rounded-2xl p-5 transition-transform duration-200 hover:-translate-y-0.5"
                      style={{
                        background: "var(--bg-card)",
                        border: "1px solid rgba(52,211,153,0.2)",
                        boxShadow: "var(--shadow-card)",
                      }}
                    >
                      {/* Widget header */}
                      <div className="mb-3 flex items-start justify-between gap-2">
                        <h3 className="text-sm font-bold" style={{ color: "var(--text-primary)" }}>
                          {status.payload?.title}
                        </h3>
                        <span
                          className="shrink-0 rounded-full px-2 py-0.5 text-[10px] font-bold uppercase tracking-wide"
                          style={{ background: "var(--complete-bg)", color: "var(--complete-fg)" }}
                        >
                          ✓ {status.id}
                        </span>
                      </div>

                      {/* Data rows with mini-bar */}
                      <div className="space-y-2">
                        {status.payload?.labels.map((label, index) => (
                          <div key={`${status.id}-${label}-${index}`}>
                            <div className="flex items-center justify-between">
                              <span className="text-xs" style={{ color: "var(--text-secondary)" }}>
                                {label}
                              </span>
                              <span className="text-xs font-semibold tabular-nums" style={{ color: "var(--text-primary)" }}>
                                {status.payload?.values[index]}
                              </span>
                            </div>
                            <MiniBar value={status.payload!.values[index]} max={maxVal} />
                          </div>
                        ))}
                      </div>
                    </article>
                  );
                })}
          </div>

          {/* Empty state */}
          {!loading && unlockedWidgets.length === 0 && (
            <div
              className="flex flex-col items-center justify-center rounded-2xl px-6 py-16 text-center"
              style={{
                background: "var(--bg-surface)",
                border: "1px dashed var(--border-accent)",
              }}
            >
              <div
                className="mb-4 flex h-16 w-16 items-center justify-center rounded-2xl text-3xl"
                style={{ background: "var(--bg-card)", border: "1px solid var(--border-subtle)" }}
              >
                🔒
              </div>
              <p className="text-sm font-semibold" style={{ color: "var(--text-primary)" }}>
                No widgets unlocked yet
              </p>
              <p className="mt-2 max-w-xs text-xs leading-relaxed" style={{ color: "var(--text-secondary)" }}>
                Start with{" "}
                <code
                  className="rounded px-1 py-0.5 font-mono"
                  style={{ background: "var(--bg-card)", color: "var(--accent-400)" }}
                >
                  assignments/assignment0/student_code.py
                </code>{" "}
                and follow the INSTRUCTIONS.md in each folder.
              </p>
            </div>
          )}

          {/* All-complete banner */}
          {allComplete && (
            <div
              className="mt-4 rounded-2xl px-5 py-4 text-sm font-semibold"
              style={{
                background: "linear-gradient(135deg, rgba(52,211,153,0.12), rgba(99,102,241,0.12))",
                border: "1px solid rgba(52,211,153,0.35)",
                color: "var(--complete-fg)",
                boxShadow: "0 0 24px rgba(52,211,153,0.15)",
              }}
            >
              🎉 All widgets unlocked — Final Project Integration complete!
            </div>
          )}
        </section>
      </main>
    </div>
  );
}

