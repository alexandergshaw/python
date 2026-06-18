# =============================================================================
#  REVIEW 1 — Fundamentals Review
#  File: assignments/review1/student_code.py
# =============================================================================
#
#  WHAT THIS REVIEW COVERS (Assignments 0-3)
#  ---------------------------------------------------------------------------
#  * Variables           name = value
#  * Branching           if / elif / else
#  * Conditionals        comparing with ==, !=, <, >, <=, >=
#  * Loops               for item in list:  with the counting pattern
#
#  This review asks you to write TWO small functions, one that branches and
#  one that loops, plus your usual widget data.  Nothing new -- just practice
#  the fundamentals from the first weeks.
#
#  YOUR TASK (three small things)
#  ---------------------------------------------------------------------------
#  1. Finish `grade_label(score)` -- turn a number into a letter grade using
#     if / elif / else.
#
#  2. Finish `count_passing(scores, passing)` -- loop through a list of scores
#     and count how many reached the passing mark.
#
#  3. Fill in `get_dashboard_payload()` with at least 3 of your own numbers
#     and matching labels.
#
#  WORKED EXAMPLE (use different data, don't copy it)
#  ---------------------------------------------------------------------------
#      title  = "My Quiz Scores"
#      labels = ["Quiz 1", "Quiz 2", "Quiz 3"]
#      values = [88, 92, 74]
# =============================================================================

"""Starter code for review1: Review: Fundamentals."""

# Change this to your real name.
student_name = "Alex Shaw"

# Leave this exactly as-is.
assignment_label = "review1"


def grade_label(score):
    """Turn a numeric score into a letter grade using if / elif / else.

    Rules to follow:
      * score 90 or above  -> return "A"
      * score 80 to 89     -> return "B"
      * score 70 to 79     -> return "C"
      * anything below 70  -> return "F"

    Examples (these are what the tests expect):
        grade_label(95)  ->  "A"
        grade_label(82)  ->  "B"
        grade_label(73)  ->  "C"
        grade_label(50)  ->  "F"
    """
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "F"


def count_passing(scores, passing):
    """Count how many scores reached the passing mark.

    `scores` is a list of numbers.  `passing` is a single number.  Loop through
    `scores` and count how many are GREATER THAN OR EQUAL TO `passing`.

    Examples (these are what the tests expect):
        count_passing([55, 70, 90], 70)  ->  2
        count_passing([10, 20], 50)       ->  0
    """
    count = 0
    for score in scores:
        if score >= passing:
            count += 1
    return count


def get_dashboard_payload():
    """Return the data for your Review 1 widget.

    Put your own numbers in `values` and a matching label for each one in
    `labels`.  Keep at least 3 items in each list, with at least 2 of the
    numbers different from one another.
    """
    my_labels = ["Quiz 1", "Quiz 2", "Quiz 3"]
    my_values = [88, 92, 74]

    return {
        "title": "Review: Fundamentals",
        "values": my_values,
        "labels": my_labels,
    }
