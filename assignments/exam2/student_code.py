# =============================================================================
#  EXAM 2 — Test 2 Prep
#  File: assignments/exam2/student_code.py
# =============================================================================
#
#  WHAT THIS PRACTICE COVERS (Assignments 4-10)
#  ---------------------------------------------------------------------------
#  Exam-style practice across every second-half topic, one small piece at a time:
#
#    * Functions & modularization   mean() and a function that calls it
#    * Data structures (dict)       price_total()
#    * File I/O + error handling     parse_floats()  with try/except
#    * Classes                       the Tally class
#    * Inheritance                   ResettableTally(Tally)
#    * Lambdas                       the `cube` lambda
#    * Decorators                    base_points() with @add_bonus
#    * Debugging                     fix the bug in count_failures()
#
#  Write each one from the rules given, then make the tests pass.  Finally,
#  fill in get_dashboard_payload() with at least 3 of your own numbers.
# =============================================================================

"""Starter code for exam2: Test 2 Prep."""

# Change this to your real name.
student_name = "Your Name"

# Leave this exactly as-is.
assignment_label = "exam2"


# ── Functions & modularization ───────────────────────────────────────────────
def mean(numbers):
    """Return the average of a list of numbers (return 0 for an empty list)."""
    # TODO: return the sum divided by the count (or 0 if the list is empty).
    return 0


def below_average_count(numbers):
    """Count how many numbers are below the average. CALL mean() to get it."""
    # TODO: get the average by calling mean(numbers), then count the numbers
    #       that are strictly less than it.
    return 0


# ── Data structures ──────────────────────────────────────────────────────────
def price_total(prices):
    """Add up all the values in a dictionary of prices and return the total."""
    # TODO: sum the dictionary's values (0 for an empty dict).
    return 0


# ── File I/O + error handling ────────────────────────────────────────────────
def parse_floats(lines):
    """Convert a list of text lines into floats, skipping any that aren't numbers.

    Use try / except around float(line) so bad lines are skipped.
    Example: parse_floats(["1.5", "oops", "2.0"]) -> [1.5, 2.0]
    """
    # TODO: loop over lines; try float(line); skip on ValueError.
    return []


# ── Classes ──────────────────────────────────────────────────────────────────
class Tally:
    """Keeps a running tally starting at zero."""

    # TODO: write __init__(self) so it sets self.count to 0.

    # TODO: write bump(self) so it increases self.count by 1.
    pass


# ── Inheritance ──────────────────────────────────────────────────────────────
class ResettableTally(Tally):
    """A Tally that can also be reset back to zero."""

    # TODO: write reset(self) so it sets self.count back to 0.
    #       (You inherit __init__ and bump() from Tally.)
    pass


# ── Lambdas ──────────────────────────────────────────────────────────────────
# TODO: replace this stub with a lambda that returns x times x times x (x cubed).
cube = lambda x: None


# ── Decorators (add_bonus is PROVIDED -- do not change it) ────────────────────
def add_bonus(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) + 5
    return wrapper


# TODO: put @add_bonus above this function, and return level * 10.
def base_points(level):
    return 0


# ── Debugging ────────────────────────────────────────────────────────────────
def count_failures(results):
    """Count the False values in `results`. There is a bug -- fix the marked line."""
    failed = 0
    for result in results:
        if not result:
            failed = failed   # BUG: this never increases the count
    return failed


def get_dashboard_payload():
    """Return the data for your Exam 2 prep widget.

    Put your own numbers in `values` and a matching label for each one in
    `labels`.  Keep at least 3 items in each list, with at least 2 of the
    numbers different from one another.
    """
    my_labels = []
    my_values = []

    return {
        "title": "Test 2 Prep",
        "values": my_values,
        "labels": my_labels,
    }
