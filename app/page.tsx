"use client";

import { useEffect, useMemo, useState } from "react";
import type { PyodideInterface } from "pyodide";

// Load Pyodide from the CDN instead of bundling the npm package. The npm
// `pyodide` package pulls in Node built-ins and has no way to locate its WASM
// assets inside a browser bundle, which is why `loadPyodide()` was failing.
// We inject the matching-version script and call the global `loadPyodide`,
// pointing `indexURL` at the same CDN folder so it finds the .wasm/stdlib files.
const PYODIDE_VERSION = "0.29.4";
const PYODIDE_CDN = `https://cdn.jsdelivr.net/pyodide/v${PYODIDE_VERSION}/full/`;

declare global {
  interface Window {
    loadPyodide?: (options?: { indexURL?: string }) => Promise<PyodideInterface>;
  }
}

let pyodideScriptPromise: Promise<void> | null = null;

function loadPyodideScript(): Promise<void> {
  if (typeof window === "undefined") {
    return Promise.reject(new Error("Pyodide can only load in the browser."));
  }
  if (window.loadPyodide) {
    return Promise.resolve();
  }
  if (!pyodideScriptPromise) {
    pyodideScriptPromise = new Promise<void>((resolve, reject) => {
      const script = document.createElement("script");
      script.src = `${PYODIDE_CDN}pyodide.js`;
      script.onload = () => resolve();
      script.onerror = () => reject(new Error("Failed to download the Pyodide script."));
      document.head.appendChild(script);
    });
  }
  return pyodideScriptPromise;
}

async function initPyodide(): Promise<PyodideInterface> {
  await loadPyodideScript();
  if (!window.loadPyodide) {
    throw new Error("loadPyodide is unavailable after loading the Pyodide script.");
  }
  return window.loadPyodide({ indexURL: PYODIDE_CDN });
}

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

/**
 * Python harness, defined once in the Pyodide global scope.
 *
 * `run_assignment_tests(dir, run_id)` runs the assignment's real
 * `test_assignment.py` (written to `dir` alongside `student_code.py`) using the
 * stdlib `unittest` runner and returns a JSON string describing the outcome.
 * An assignment unlocks only when every test in that file passes.
 *
 * Each call loads the test module under a unique name so results never leak
 * between assignments, and best-effort extracts the dashboard payload (only
 * when the tests pass) so the widget can render without re-running the code.
 */
const TEST_HARNESS = `
import importlib.util
import io
import json
import pathlib
import sys
import unittest


def run_assignment_tests(dir_path, run_id):
    base = pathlib.Path(dir_path)
    test_file = base / "test_assignment.py"
    if not test_file.exists():
        return json.dumps({"ok": False, "ran": 0, "summary": "No test_assignment.py found."})

    # Load the test file fresh under a unique module name so nothing is cached
    # between assignments.
    mod_name = "test_assignment_%s" % run_id
    spec = importlib.util.spec_from_file_location(mod_name, test_file)
    module = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(module)
    except Exception as exc:  # noqa: BLE001
        return json.dumps({"ok": False, "ran": 0, "summary": "Could not load tests: %s" % exc})

    suite = unittest.TestLoader().loadTestsFromModule(module)
    result = unittest.TextTestRunner(stream=io.StringIO(), verbosity=0).run(suite)

    ran = result.testsRun
    broken = len(result.failures) + len(result.errors)
    passed = ran - broken
    ok = result.wasSuccessful() and ran > 0

    if ran == 0:
        summary = "No tests were found to run."
    elif ok:
        summary = "All %d unit tests passed." % ran
    else:
        summary = "%d of %d unit tests passed." % (passed, ran)

    payload = None
    if ok:
        try:
            sc_spec = importlib.util.spec_from_file_location(
                "student_code_%s" % run_id, base / "student_code.py"
            )
            sc_mod = importlib.util.module_from_spec(sc_spec)
            sc_spec.loader.exec_module(sc_mod)
            fn = getattr(sc_mod, "get_dashboard_payload", None)
            raw = fn() if callable(fn) else None
            if isinstance(raw, dict):
                payload = {
                    "title": raw.get("title"),
                    "values": list(raw.get("values", [])),
                    "labels": list(raw.get("labels", [])),
                }
        except Exception:  # noqa: BLE001
            payload = None

    return json.dumps(
        {"ok": ok, "ran": ran, "passed": passed, "summary": summary, "payload": payload},
        default=str,
    )
`;

type TestRunResult = {
  ok: boolean;
  ran: number;
  passed?: number;
  summary: string;
  payload?: unknown;
};

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

async function evaluateAssignment(
  pyodide: PyodideInterface,
  assignment: AssignmentMeta,
  runId: number,
): Promise<AssignmentStatus> {
  const response = await fetch(`/api/student-code?assignment=${assignment.id}`);
  if (!response.ok) {
    return {
      ...assignment,
      complete: false,
      payload: null,
      message: "Could not load assignment files.",
    };
  }

  const { code, testCode } = (await response.json()) as {
    code?: string;
    testCode?: string | null;
  };

  if (typeof code !== "string") {
    return { ...assignment, complete: false, payload: null, message: "Missing student_code.py." };
  }
  if (typeof testCode !== "string") {
    return {
      ...assignment,
      complete: false,
      payload: null,
      message: "Missing test_assignment.py — cannot run unit tests.",
    };
  }

  // Drop both files into Pyodide's virtual filesystem so the test can import the
  // student code exactly the way it does on disk (via __file__.with_name(...)).
  const dir = `/assignments/${assignment.id}`;
  try {
    pyodide.FS.mkdirTree(dir);
  } catch {
    // Directory already exists from a previous run — fine, we overwrite below.
  }
  pyodide.FS.writeFile(`${dir}/student_code.py`, code);
  pyodide.FS.writeFile(`${dir}/test_assignment.py`, testCode);

  const runTests = pyodide.globals.get("run_assignment_tests") as {
    destroy?: () => void;
    (dir: string, runId: number): string;
  };

  let result: TestRunResult;
  try {
    result = JSON.parse(runTests(dir, runId)) as TestRunResult;
  } catch {
    return {
      ...assignment,
      complete: false,
      payload: null,
      message: "The unit-test runner crashed.",
    };
  } finally {
    runTests.destroy?.();
  }

  const payload = isValidPayload(result.payload) ? result.payload : null;

  return {
    ...assignment,
    complete: Boolean(result.ok),
    payload,
    message: result.summary || (result.ok ? "Unit tests passed." : "Unit tests failed."),
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
        const pyodide = await initPyodide();
        // Define the unittest harness once; every assignment reuses it.
        pyodide.runPython(TEST_HARNESS);

        const nextStatuses: AssignmentStatus[] = [];

        let runId = 0;
        for (const assignment of ASSIGNMENTS) {
          const status = await evaluateAssignment(pyodide, assignment, runId++);
          nextStatuses.push(status);
        }

        if (mounted) {
          setStatuses(nextStatuses);
        }
      } catch (error) {
        // Surface the real cause in the console — the UI message is generic.
        console.error("Pyodide initialization failed:", error);
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

  // An assignment unlocks the moment its unit tests pass. The chart bars render
  // only when get_dashboard_payload() also returns non-trivial data.
  const unlockedWidgets = useMemo(
    () => statuses.filter((status) => status.complete),
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
          background: "rgba(1,10,4,0.85)",
          backdropFilter: "blur(12px)",
          borderBottom: "1px solid var(--border-subtle)",
        }}
      >
        <div className="flex items-center gap-3">
          {/* Logo mark */}
          <div
            className="flex h-8 w-8 items-center justify-center rounded-lg text-sm font-bold text-[#021006]"
            style={{ background: "linear-gradient(135deg, var(--accent-600), var(--accent-violet))" }}
          >
            Py
          </div>
          <span className="text-sm font-semibold" style={{ color: "var(--text-primary)" }}>
            <span style={{ color: "var(--accent-500)" }}>~/python-course</span>{" "}
            <span style={{ color: "var(--text-secondary)" }}>$</span> dashboard
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
            Pass the <code className="rounded px-1 py-0.5 font-mono text-[10px]" style={{ background: "var(--bg-card)", color: "var(--accent-400)" }}>test_assignment.py</code> unit tests in each assignment to unlock dashboard widgets.
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
              const status = loading ? undefined : statuses.find((s) => s.id === assignment.id);
              const complete = status?.complete;
              return (
                <li
                  key={assignment.id}
                  className="group rounded-xl p-2.5 transition-colors duration-150"
                  style={{
                    background: complete ? "rgba(45,255,106,0.08)" : "var(--bg-card)",
                    border: `1px solid ${complete ? "rgba(45,255,106,0.30)" : "var(--border-subtle)"}`,
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
                  {!loading && !complete && status?.message && (
                    <p className="mt-1 text-[10px]" style={{ color: "var(--locked-fg)" }}>
                      {status.message}
                    </p>
                  )}
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
              background: "linear-gradient(135deg, var(--bg-surface) 0%, #06180d 100%)",
              border: "1px solid var(--border-subtle)",
              boxShadow: "var(--shadow-card)",
            }}
          >
            <h2 className="text-xl font-bold gradient-text">
              &gt; Personal Data Dashboard
              <span className="cursor-blink ml-1" aria-hidden="true">&nbsp;</span>
            </h2>
            <p className="mt-1 text-sm" style={{ color: "var(--text-secondary)" }}>
              Widgets appear automatically when an assignment&apos;s{" "}
              <code
                className="rounded px-1.5 py-0.5 font-mono text-xs"
                style={{ background: "var(--bg-card)", color: "var(--accent-400)" }}
              >
                test_assignment.py
              </code>{" "}
              unit tests all pass.
            </p>
          </div>

          {/* Widget grid */}
          <div className="grid gap-4 sm:grid-cols-2">
            {loading
              ? Array.from({ length: 4 }).map((_, i) => <SkeletonCard key={i} />)
              : unlockedWidgets.map((status) => {
                  // Capture in a local const so TS keeps the non-null narrowing
                  // inside the .map() callback below.
                  const payload = status.payload;
                  const maxVal = payload ? Math.max(...payload.values.map(Math.abs)) : 0;
                  return (
                    <article
                      key={status.id}
                      className="card-complete rounded-2xl p-5 transition-transform duration-200 hover:-translate-y-0.5"
                      style={{
                        background: "var(--bg-card)",
                        border: "1px solid rgba(45,255,106,0.25)",
                        boxShadow: "var(--shadow-card)",
                      }}
                    >
                      {/* Widget header */}
                      <div className="mb-3 flex items-start justify-between gap-2">
                        <h3 className="text-sm font-bold" style={{ color: "var(--text-primary)" }}>
                          {payload?.title ?? status.title}
                        </h3>
                        <span
                          className="shrink-0 rounded-full px-2 py-0.5 text-[10px] font-bold uppercase tracking-wide"
                          style={{ background: "var(--complete-bg)", color: "var(--complete-fg)" }}
                        >
                          ✓ {status.id}
                        </span>
                      </div>

                      {payload ? (
                        /* Data rows with mini-bar */
                        <div className="space-y-2">
                          {payload.labels.map((label, index) => (
                            <div key={`${status.id}-${label}-${index}`}>
                              <div className="flex items-center justify-between">
                                <span className="text-xs" style={{ color: "var(--text-secondary)" }}>
                                  {label}
                                </span>
                                <span className="text-xs font-semibold tabular-nums" style={{ color: "var(--text-primary)" }}>
                                  {payload.values[index]}
                                </span>
                              </div>
                              <MiniBar value={payload.values[index]} max={maxVal} />
                            </div>
                          ))}
                        </div>
                      ) : (
                        /* Tests pass, but get_dashboard_payload() has no chartable data yet */
                        <p className="text-xs leading-relaxed" style={{ color: "var(--text-secondary)" }}>
                          Unit tests passing. Return non-trivial{" "}
                          <code className="rounded px-1 py-0.5 font-mono text-[10px]" style={{ background: "var(--bg-base)", color: "var(--accent-400)" }}>
                            title / labels / values
                          </code>{" "}
                          from <code className="font-mono text-[10px]" style={{ color: "var(--accent-400)" }}>get_dashboard_payload()</code> to chart your data.
                        </p>
                      )}
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
                background: "linear-gradient(135deg, rgba(45,255,106,0.14), rgba(0,255,163,0.10))",
                border: "1px solid rgba(45,255,106,0.40)",
                color: "var(--complete-fg)",
                boxShadow: "0 0 24px rgba(45,255,106,0.20)",
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

