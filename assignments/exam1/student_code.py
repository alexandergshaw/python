# =============================================================================
#  EXAM 1 — Test 1
#  File: assignments/exam1/student_code.py
# =============================================================================
#
#  WHAT THIS TEST COVERS (Assignments 0-3)
#  ---------------------------------------------------------------------------
#  * Variables and types
#  * Branching / conditionals   (if / elif / else, comparisons)
#  * Loops                      (for item in list, the counting/summing pattern)
#
#  This is Test 1: write two short functions from the rules given,
#  then make the tests pass.  Everything here uses skills from the first weeks.
#
#  THE SUMMING PATTERN (helpful for the second function)
#  ---------------------------------------------------------------------------
#  Start a total at 0 before the loop, then add to it inside the loop:
#
#      total = 0
#      for number in [2, 5, 8]:
#          total = total + number
#      # total is now 15
#
#  TIP: number % 2 == 0 is True when `number` is even (no remainder when
#  divided by 2).
#
#  YOUR TASK (three small things)
#  ---------------------------------------------------------------------------
#  1. Finish `classify_number(n)` -- return "negative", "zero", or "positive".
#  2. Finish `sum_even(numbers)`  -- add up only the even numbers in a list.
#  3. Fill in `get_dashboard_payload()` with at least 3 of your own numbers.
#
#  WORKED EXAMPLE (use different data, don't copy it)
#  ---------------------------------------------------------------------------
#      title  = "My Results"
#      labels = ["Q1", "Q2", "Q3"]
#      values = [4, 3, 1]
# =============================================================================

"""Starter code for exam1: Test 1."""

# Change this to your real name.
student_name = "Alex Shaw"

# Leave this exactly as-is.
assignment_label = "exam1"


def classify_number(n):
    """Describe a number as "negative", "zero", or "positive".

    Rules to follow:
      * If n is LESS THAN 0     -> return "negative"
      * If n is EXACTLY 0       -> return "zero"
      * If n is GREATER THAN 0  -> return "positive"

    Examples (these are what the tests expect):
        classify_number(-4)  ->  "negative"
        classify_number(0)   ->  "zero"
        classify_number(7)   ->  "positive"
    """
    if n < 0:
        return "negative"
    elif n == 0:
        return "zero"
    else:
        return "positive"


def sum_even(numbers):
    """Add up only the even numbers in a list and return the total.

    `numbers` is a list of whole numbers.  Loop through it and add a number to
    your running total only when it is even (number % 2 == 0).

    Examples (these are what the tests expect):
        sum_even([1, 2, 3, 4])  ->  6     (2 + 4)
        sum_even([1, 3, 5])     ->  0     (no even numbers)
    """
    total = 0
    for number in numbers:
        if number % 2 == 0:
            total += number
    return total


def get_dashboard_payload():
    """Return the data for your Test 1 widget.

    Put your own numbers in `values` and a matching label for each one in
    `labels`.  Keep at least 3 items in each list, with at least 2 of the
    numbers different from one another.
    """
    my_labels = ["Q1", "Q2", "Q3"]
    my_values = [4, 3, 1]

    return {
        "title": "Test 1",
        "values": my_values,
        "labels": my_labels,
    }
