# =============================================================================
#  ASSIGNMENT 4 — Functions and Modularization
#  File: assignments/assignment4/student_code.py
# =============================================================================
#
#  WHAT YOU'RE LEARNING THIS WEEK
#  ---------------------------------------------------------------------------
#  A FUNCTION is a named, reusable block of code.  You define one with `def`,
#  give it inputs in the parentheses, and hand a result back with `return`:
#
#      def add(a, b):
#          return a + b
#
#      total = add(3, 7)     # total is 10
#
#  MODULARIZATION means building bigger jobs out of small functions, and having
#  one function CALL another instead of repeating code.  For example, a function
#  that needs an average can just call your `average` function rather than
#  re-writing the math:
#
#      def average(numbers):
#          ...
#
#      def how_many_above_average(numbers):
#          avg = average(numbers)     # reuse the function above!
#          ...
#
#  YOUR TASK (three small things)
#  ---------------------------------------------------------------------------
#  1. Finish `average(numbers)` -- return the mean (sum divided by how many).
#
#  2. Finish `above_average_count(numbers)` -- CALL your `average` function,
#     then count how many numbers are greater than that average.
#
#  3. Fill in `get_dashboard_payload()` with at least 3 of your own numbers.
#
#  WORKED EXAMPLE (use different data, don't copy it)
#  ---------------------------------------------------------------------------
#      title  = "Daily Expenses"
#      labels = ["Mon", "Tue", "Wed"]
#      values = [12, 8, 19]
# =============================================================================

"""Starter code for assignment4: Functions, Modularization."""

# Change this to your real name.
student_name = "Your Name"

# Leave this exactly as-is.
assignment_label = "assignment4"


def average(numbers):
    """Return the average (mean) of a list of numbers.

    Add the numbers up and divide by how many there are.  If the list is
    empty, return 0 so we never divide by zero.

    Examples (these are what the tests expect):
        average([2, 4, 6])  ->  4.0
        average([10])       ->  10.0
        average([])         ->  0
    """
    # TODO: handle the empty list, then return the sum divided by the count.
    return 0


def above_average_count(numbers):
    """Count how many numbers are ABOVE the average of the list.

    First get the average by CALLING your average() function above.  Then loop
    through `numbers` and count how many are strictly greater than that average.

    Examples (these are what the tests expect):
        above_average_count([2, 4, 6])      ->  1     (only 6 is above 4.0)
        above_average_count([10, 10, 10])   ->  0     (none are above 10.0)
        above_average_count([1, 2, 3, 4])   ->  2     (3 and 4 are above 2.5)
    """
    # TODO: call average(numbers), then count numbers greater than it.
    return 0


def get_dashboard_payload():
    """Return the data for your Assignment 4 widget.

    Put your own numbers in `values` and a matching label for each one in
    `labels`.  Keep at least 3 items in each list, with at least 2 of the
    numbers different from one another.
    """
    my_labels = []   # e.g. ["Mon", "Tue", "Wed"]
    my_values = []   # e.g. [12, 8, 19]

    return {
        "title": "Functions, Modularization",
        "values": my_values,
        "labels": my_labels,
    }
