# =============================================================================
#  ASSIGNMENT 2 — Conditionals and Testing
#  File: assignments/assignment2/student_code.py
# =============================================================================
#
#  WHAT YOU'RE LEARNING THIS WEEK
#  ---------------------------------------------------------------------------
#  * CONDITIONALS -- comparing two values to get a True/False answer, then
#    acting on it.  The comparison operators are:
#
#        a == b   "a equals b"          a != b   "a is not equal to b"
#        a <  b   "a is less than b"    a >  b   "a is greater than b"
#        a <= b   "a is less than or equal to b"
#        a >= b   "a is greater than or equal to b"
#
#    Notice the difference: a single = ASSIGNS a value, while a double ==
#    COMPARES two values.  Comparisons are what you put after `if` / `elif`.
#
#  * TESTING -- this course gives you a test_assignment.py file full of small
#    checks.  Run it from the Testing panel.  Each check tells you exactly what
#    your code should do.  "Make the tests pass" is the whole game.
#
#  YOUR TASK (two small things)
#  ---------------------------------------------------------------------------
#  1. Finish `budget_status(spent, limit)` so it compares how much was spent
#     against a spending limit and returns one of three words.  The rules are
#     written in the function below.
#
#  2. Fill in `get_dashboard_payload()` with at least 3 of your own numbers
#     (for example, what you spent in a few categories) and matching labels.
#
#  WORKED EXAMPLE (use different data, don't copy it)
#  ---------------------------------------------------------------------------
#      title  = "Weekly Spending"
#      labels = ["Food", "Transit", "Fun"]
#      values = [42, 18, 25]
# =============================================================================

"""Starter code for assignment2: Conditionals, Testing."""

# Change this to your real name.
student_name = "Alex Shaw"

# Leave this exactly as-is.
assignment_label = "assignment2"


def budget_status(spent, limit):
    """Compare spending to a limit and return a status word.

    Rules to follow:
      * If `spent` is LESS THAN `limit`     -> return "under"
      * If `spent` is GREATER THAN `limit`  -> return "over"
      * If they are EQUAL                   -> return "exact"

    Examples (these are what the tests expect):
        budget_status(40, 60)  ->  "under"
        budget_status(75, 60)  ->  "over"
        budget_status(60, 60)  ->  "exact"

    Replace the line below with if / elif / else branches that compare
    `spent` and `limit`.
    """
    if spent < limit:
        return "under"
    elif spent > limit:
        return "over"
    else:
        return "exact"


def get_dashboard_payload():
    """Return the data for your Assignment 2 widget.

    Put your own numbers in `values` and a matching label for each one in
    `labels`.  Keep at least 3 items in each list, with at least 2 of the
    numbers different from one another.
    """
    my_labels = ["Food", "Transit", "Fun"]
    my_values = [42, 18, 25]

    return {
        "title": "Conditionals, Testing",
        "values": my_values,
        "labels": my_labels,
    }
