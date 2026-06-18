# =============================================================================
#  ASSIGNMENT 10 — CI/CD and Debugging
#  File: assignments/assignment10/student_code.py
# =============================================================================
#
#  WHAT YOU'RE LEARNING THIS WEEK
#  ---------------------------------------------------------------------------
#  CI/CD means your tests run automatically in the cloud (GitHub Actions) every
#  time you push.  A green check means your code passed; a red X means a test
#  failed.  The CI/CD checklist for setting this up is in INSTRUCTIONS.md.
#
#  DEBUGGING is the skill of finding and fixing code that runs but gives the
#  WRONG answer.  The best tool is the test output itself: it tells you exactly
#  which input produced which wrong result, so you can trace back to the line
#  that's misbehaving.
#
#  YOUR TASK (two small things)
#  ---------------------------------------------------------------------------
#  1. The `count_passes` function below already runs without crashing -- but it
#     gives the WRONG answer.  Run the tests, read which case fails, and fix the
#     one line that's wrong so it counts correctly.  (Hint: trace what happens
#     to `passed` each time the loop finds a True value.)
#
#  2. Fill in `get_dashboard_payload()` with at least 3 of your own numbers.
#
#  WORKED EXAMPLE (use different data, don't copy it)
#  ---------------------------------------------------------------------------
#      title  = "Build Results"
#      labels = ["Passed", "Failed", "Retries"]
#      values = [8, 2, 3]
# =============================================================================

"""Starter code for assignment10: CI/CD, Debugging."""

# Change this to your real name.
student_name = "Alex Shaw"

# Leave this exactly as-is.
assignment_label = "assignment10"


def count_passes(results):
    """Count how many builds passed.

    `results` is a list of True/False values, where True means a build passed.
    This should return how many of them are True.

    Examples (these are what the tests expect):
        count_passes([True, False, True])  ->  2
        count_passes([])                    ->  0
        count_passes([True, True, True])    ->  3

    NOTE: there is a bug below.  The function runs, but the count comes out
    wrong.  Find the broken line and fix it.
    """
    passed = 0
    for result in results:
        if result:
            passed = passed + 1
    return passed


def get_dashboard_payload():
    """Return the data for your Assignment 10 widget.

    Put your own numbers in `values` and a matching label for each one in
    `labels`.  Keep at least 3 items in each list, with at least 2 of the
    numbers different from one another.
    """
    my_labels = ["Passed", "Failed", "Retries"]
    my_values = [8, 2, 3]

    return {
        "title": "CI/CD, Debugging",
        "values": my_values,
        "labels": my_labels,
    }
