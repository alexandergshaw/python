# =============================================================================
#  ASSIGNMENT 9 — Lambdas and Decorators
#  File: assignments/assignment9/student_code.py
# =============================================================================
#
#  WHAT YOU'RE LEARNING THIS WEEK
#  ---------------------------------------------------------------------------
#  A LAMBDA is a tiny one-line function with no name.  These two are the same:
#
#      def double(x):          double = lambda x: x * 2
#          return x * 2
#
#  You call it just like any function:  double(5)  ->  10
#
#  A DECORATOR is a function that wraps another function to add behavior.  You
#  apply one by writing @name on the line above a function:
#
#      @add_bonus
#      def score():
#          return 10
#      # because of @add_bonus, calling score() runs the wrapped version
#
#  YOUR TASK (three small things)
#  ---------------------------------------------------------------------------
#  1. Write a lambda named `square` that takes one number and returns that
#     number multiplied by itself.  (Replace the stub below.)
#
#  2. The decorator `add_bonus` is PROVIDED for you (don't change it).  It adds
#     5 to whatever number a function returns.  Finish `base_points(level)` so
#     it returns the level multiplied by 10 -- AND apply the decorator by
#     writing  @add_bonus  on the line above the function.
#
#  3. Fill in `get_dashboard_payload()` with at least 3 of your own numbers.
#
#  WORKED EXAMPLE (use different data, don't copy it)
#  ---------------------------------------------------------------------------
#      title  = "Points Earned"
#      labels = ["Level 1", "Level 2", "Level 3"]
#      values = [15, 25, 35]
# =============================================================================

"""Starter code for assignment9: Lambdas/Decorators."""

# Change this to your real name.
student_name = "Your Name"

# Leave this exactly as-is.
assignment_label = "assignment9"


# TODO 1: replace this stub with a lambda that returns x times itself.
#         Example shape:  square = lambda x: ...
square = lambda x: None


# ---------------------------------------------------------------------------
#  PROVIDED FOR YOU -- do not change this decorator.
#  It wraps a function and adds 5 to whatever number that function returns.
# ---------------------------------------------------------------------------
def add_bonus(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) + 5
    return wrapper


# TODO 2: put @add_bonus on the line directly above this function, and make it
#         return level * 10.
def base_points(level):
    # TODO: return the level multiplied by 10.
    return 0


def get_dashboard_payload():
    """Return the data for your Assignment 9 widget.

    Put your own numbers in `values` and a matching label for each one in
    `labels`.  Keep at least 3 items in each list, with at least 2 of the
    numbers different from one another.
    """
    my_labels = []   # e.g. ["Level 1", "Level 2", "Level 3"]
    my_values = []   # e.g. [15, 25, 35]

    return {
        "title": "Lambdas/Decorators",
        "values": my_values,
        "labels": my_labels,
    }
