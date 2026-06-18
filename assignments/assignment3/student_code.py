# =============================================================================
#  ASSIGNMENT 3 — Loops
#  File: assignments/assignment3/student_code.py
# =============================================================================
#
#  WHAT YOU'RE LEARNING THIS WEEK
#  ---------------------------------------------------------------------------
#  A LOOP runs the same block of code once for each item in a list.  The most
#  common kind is the `for` loop:
#
#      steps = [4200, 7000, 8100]
#      for day in steps:          # `day` becomes 4200, then 7000, then 8100
#          print(day)
#
#  THE COUNTING PATTERN (you'll use this today)
#  ---------------------------------------------------------------------------
#  Start a counter at 0 BEFORE the loop, then add 1 inside the loop whenever
#  something is true:
#
#      total = 0
#      for number in [3, 9, 1, 8]:
#          if number > 5:
#              total = total + 1     # only counts the big ones
#      # total is now 2  (9 and 8)
#
#  YOUR TASK (two small things)
#  ---------------------------------------------------------------------------
#  1. Finish `count_active_days(steps, goal)` so it loops through a list of
#     daily step counts and returns HOW MANY days reached the goal.  The exact
#     rule is written in the function below.
#
#  2. Fill in `get_dashboard_payload()` with at least 3 of your own daily
#     numbers and matching labels.
#
#  WORKED EXAMPLE (use different data, don't copy it)
#  ---------------------------------------------------------------------------
#      title  = "Steps This Week"
#      labels = ["Mon", "Tue", "Wed", "Thu"]
#      values = [4200, 7000, 8100, 10020]
# =============================================================================

"""Starter code for assignment3: Loops."""

# Change this to your real name.
student_name = "Alex Shaw"

# Leave this exactly as-is.
assignment_label = "assignment3"


def count_active_days(steps, goal):
    """Count how many days reached the step goal.

    `steps` is a list of numbers (one per day).  `goal` is a single number.
    Loop through `steps` and count how many are GREATER THAN OR EQUAL TO `goal`.
    Return that count (a whole number).

    Examples (these are what the tests expect):
        count_active_days([1000, 5000, 8000], 4000)  ->  2
        count_active_days([1, 2, 3], 10)             ->  0
        count_active_days([10, 10], 5)               ->  2

    Use the counting pattern: start at 0, loop, add 1 when a day reaches goal.
    """
    count = 0
    for day in steps:
        if day >= goal:
            count += 1
    return count


def get_dashboard_payload():
    """Return the data for your Assignment 3 widget.

    Put your own daily numbers in `values` and a matching label for each one
    in `labels`.  Keep at least 3 items in each list, with at least 2 of the
    numbers different from one another.
    """
    my_labels = ["Mon", "Tue", "Wed", "Thu"]
    my_values = [4200, 7000, 8100, 10020]

    return {
        "title": "Loops",
        "values": my_values,
        "labels": my_labels,
    }
