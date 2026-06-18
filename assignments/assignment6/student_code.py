# =============================================================================
#  ASSIGNMENT 6 — File I/O and Error Handling
#  File: assignments/assignment6/student_code.py
# =============================================================================
#
#  WHAT YOU'RE LEARNING THIS WEEK
#  ---------------------------------------------------------------------------
#  FILE I/O -- when you read a text file, you get its contents as a list of
#  lines (each line is a string).  In this assignment we hand you that list of
#  lines directly so you can practice processing it, exactly like you would
#  after reading a real file:
#
#      lines = ["10", "20", "30"]     # imagine these came from a file
#
#  ERROR HANDLING (try / except) -- real data is messy.  Some "lines" won't be
#  valid numbers.  Instead of letting the program crash, you wrap risky code in
#  try / except so you can skip the bad ones:
#
#      try:
#          number = int(text)     # this CRASHES if text isn't a number
#      except ValueError:
#          pass                   # not a number -- just skip it
#
#  YOUR TASK (two small things)
#  ---------------------------------------------------------------------------
#  1. Finish `parse_numbers(lines)` -- go through a list of text lines and
#     return a list of the ones that are valid whole numbers, turning each into
#     an int and SKIPPING anything that isn't a number.  Use try / except.
#
#  2. Fill in `get_dashboard_payload()` with at least 3 of your own numbers.
#
#  WORKED EXAMPLE (use different data, don't copy it)
#  ---------------------------------------------------------------------------
#      title  = "Readings From File"
#      labels = ["Row 1", "Row 2", "Row 3"]
#      values = [10, 20, 30]
# =============================================================================

"""Starter code for assignment6: File I/O, Error Handling."""

# Change this to your real name.
student_name = "Your Name"

# Leave this exactly as-is.
assignment_label = "assignment6"


def parse_numbers(lines):
    """Turn a list of text lines into a list of whole numbers.

    `lines` is a list of strings (imagine each one is a line read from a file).
    Go through them one at a time.  For each line, TRY to convert it to an int
    with int(line).  If that works, add the number to your result list.  If it
    raises a ValueError (because the text isn't a number), skip that line.

    Examples (these are what the tests expect):
        parse_numbers(["10", "x", "20", ""])  ->  [10, 20]
        parse_numbers(["5"])                   ->  [5]
        parse_numbers([])                      ->  []
    """
    # TODO: loop over lines; use try/except around int(line) to skip bad lines.
    return []


def get_dashboard_payload():
    """Return the data for your Assignment 6 widget.

    Put your own numbers in `values` and a matching label for each one in
    `labels`.  Keep at least 3 items in each list, with at least 2 of the
    numbers different from one another.
    """
    my_labels = []   # e.g. ["Row 1", "Row 2", "Row 3"]
    my_values = []   # e.g. [10, 20, 30]

    return {
        "title": "File I/O, Error Handling",
        "values": my_values,
        "labels": my_labels,
    }
