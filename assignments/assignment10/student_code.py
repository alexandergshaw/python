# =============================================================================
#  ASSIGNMENT 10 — CI/CD and Debugging
#  File: assignments/assignment10/student_code.py
# =============================================================================
#
#  WHAT YOU'RE LEARNING THIS WEEK
#  ─────────────────────────────────────────────────────────────────────────────
#  CI/CD — Continuous Integration / Continuous Deployment
#  ─────────────────────────────────────────────────────────────────────────────
#  CI/CD is what professional development teams use to automatically check code
#  every time someone pushes a change.  In this course, that's GitHub Actions.
#
#  ── How it works in this project ─────────────────────────────────────────────
#  1. You push a commit to GitHub (via Source Control → Sync in Codespaces).
#  2. GitHub Actions automatically runs your tests (the same ones in the
#     Testing panel) in the cloud.
#  3. On your pull request, a green ✓ or red ✗ appears next to each check.
#  4. You can click a failed check to read the full log output and understand
#     WHY it failed — just like reading a stack trace locally.
#
#  ── Why CI matters ───────────────────────────────────────────────────────────
#  • It catches bugs BEFORE they reach the main branch.
#  • It gives the whole team confidence that new code doesn't break old code.
#  • It documents what was tested and when.
#
#  DEBUGGING
#  ─────────────────────────────────────────────────────────────────────────────
#  Debugging is the process of finding and fixing errors in your code.
#  Common error types you'll encounter:
#
#  SyntaxError      — you wrote Python that isn't valid Python
#                     (missing colon, unmatched quote, wrong indentation)
#                     Python can't even START running your code.
#
#  NameError        — you used a variable name before defining it, or typo'd it
#                     name = "Alex"
#                     print(nme)    # ← NameError: name 'nme' is not defined
#
#  TypeError        — you used the wrong data type for an operation
#                     "5" + 5       # ← TypeError: can only concatenate str to str
#
#  IndexError       — you tried to access a list position that doesn't exist
#                     items = [1, 2, 3]
#                     items[5]      # ← IndexError: list index out of range
#
#  ValueError       — you passed a value of the right type but wrong content
#                     int("hello")  # ← ValueError: invalid literal for int()
#
#  ZeroDivisionError — you tried to divide by zero
#                     10 / 0        # ← ZeroDivisionError
#
#  ── Debugging strategies ─────────────────────────────────────────────────────
#  1. READ THE ERROR MESSAGE — the last line always says what went wrong.
#     The lines above show you WHERE in the code it happened (the traceback).
#
#  2. ADD print() STATEMENTS — scatter print() calls before the error to see
#     what your variables contain at each step.
#
#  3. COMMENT OUT CODE — narrow down the problem by temporarily removing code
#     until the error disappears, then re-add it piece by piece.
#
#  4. CHECK YOUR INDENTATION — Python is whitespace-sensitive.  A misaligned
#     line can cause mysterious bugs.
#
#  YOUR TASK: Build a "CI/CD status" widget.
#  ─────────────────────────────────────────────────────────────────────────────
#  Simulate a CI run history: a list of build results (pass/fail) with retry
#  counts.  Compute statistics like pass rate, total retries, and failure count.
#  Use try/except to guard any conversions or risky operations.
#
#  WORKED EXAMPLE (use different data!):
#      ci_status    = ["pass", "fail", "pass", "pass", "fail"]
#      retry_counts = [0, 2, 0, 1, 3]
#      → pass_count = 3, fail_count = 2, total_retries = 6
#      → values: [3, 2, 6]
#      → labels: ["Passed", "Failed", "Total Retries"]
# =============================================================================

"""Starter code for assignment10: CI/CD, Debugging."""

# ── Identity variables ────────────────────────────────────────────────────────
student_name = "Your Name"
assignment_label = "assignment10"


# ── Dashboard function ────────────────────────────────────────────────────────
def get_dashboard_payload():
    """Return dashboard-ready data for the Assignment 10 widget.

    Your job:
      1. Create a list of build statuses (strings like "pass" or "fail").
      2. Create a matching list of retry counts (integers).
      3. Use a loop and conditionals to count passes, failures, and retries.
      4. Wrap risky operations (like int conversions) in try/except.
      5. Return the computed stats.

    CI/CD challenge: make sure your code passes the automated GitHub Actions
    checks on your pull request before merging!
    """
    # ── Simulate CI run history ────────────────────────────────────────────
    # Replace with your own data.
    # ci_results   = ["pass", "fail", "pass", "pass", "fail", "pass"]
    # retry_counts = [0, 1, 0, 0, 2, 0]

    # ── Compute stats using loops and conditionals ─────────────────────────
    # pass_count    = 0
    # fail_count    = 0
    # total_retries = 0
    # for i, result in enumerate(ci_results):
    #     if result == "pass":
    #         pass_count += 1
    #     else:
    #         fail_count += 1
    #     try:
    #         total_retries += int(retry_counts[i])
    #     except (ValueError, IndexError):
    #         pass   # skip bad data gracefully

    my_values = []
    my_labels = []

    return {
        "title": "CI/CD, Debugging",
        "values": my_values,
        "labels": my_labels,
    }

