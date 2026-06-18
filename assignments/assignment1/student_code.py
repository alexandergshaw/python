# =============================================================================
#  ASSIGNMENT 1 — Variables, Input/Output, and Branching
#  File: assignments/assignment1/student_code.py
# =============================================================================
#
#  WHAT YOU'RE LEARNING THIS WEEK
#  ---------------------------------------------------------------------------
#  * VARIABLES  -- named boxes that hold values:   city = "Denver"
#  * INPUT / OUTPUT -- a function takes INPUT through its parentheses and
#                      hands back OUTPUT with `return`.  (We use return values
#                      instead of input()/print() because your code runs
#                      automatically in the browser.)
#  * BRANCHING (if / elif / else) -- letting the program choose what to do:
#
#        if score >= 90:
#            grade = "A"
#        elif score >= 80:
#            grade = "B"
#        else:
#            grade = "C"
#
#    Reminders:
#      - Use >, <, >=, <= to compare numbers.
#      - The block under each `if`/`elif`/`else` is indented 4 spaces.
#      - Only ONE branch runs: Python checks them top to bottom and stops at
#        the first one that is True.
#
#  YOUR TASK (two small things)
#  ---------------------------------------------------------------------------
#  1. Finish `temperature_label(temp)` so it returns a word describing how warm
#     a temperature is.  Use if / elif / else.  The exact rules are written in
#     the function below -- translate those rules into branches.
#
#  2. Fill in `get_dashboard_payload()` with at least 3 of your own numbers
#     (e.g. the temperature each day this week) and matching labels.
#
#  WORKED EXAMPLE (use different data, don't copy it)
#  ---------------------------------------------------------------------------
#      title  = "Austin Daily Temps"
#      labels = ["Mon", "Tue", "Wed"]
#      values = [68, 71, 75]
# =============================================================================

"""Starter code for assignment1: Variables, I/O, Branching."""

# Change this to your real name.
student_name = "Your Name"

# Leave this exactly as-is.
assignment_label = "assignment1"


def temperature_label(temp):
    """Return a word describing a temperature, using if / elif / else.

    Rules to follow:
      * If temp is LESS THAN 60      -> return the string "cold"
      * If temp is 60 up to (but not including) 80 -> return "warm"
      * If temp is 80 OR MORE        -> return "hot"

    Examples (these are what the tests expect):
        temperature_label(45)  ->  "cold"
        temperature_label(72)  ->  "warm"
        temperature_label(95)  ->  "hot"

    Replace the line below with your own if / elif / else branches.
    """
    # TODO: write your branches here and return "cold", "warm", or "hot".
    return ""


def get_dashboard_payload():
    """Return the data for your Assignment 1 widget.

    Put your own daily numbers in `values` and a matching label for each one
    in `labels`.  Keep at least 3 items in each list, with at least 2 of the
    numbers different from one another.
    """
    my_labels = []   # e.g. ["Mon", "Tue", "Wed"]
    my_values = []   # e.g. [68, 71, 75]

    return {
        "title": "Variables, I/O, Branching",
        "values": my_values,
        "labels": my_labels,
    }
