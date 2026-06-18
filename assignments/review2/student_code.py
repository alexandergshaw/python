# =============================================================================
#  REVIEW 2 — OOP and Advanced Python Review
#  File: assignments/review2/student_code.py
# =============================================================================
#
#  WHAT THIS REVIEW COVERS (Assignments 4-10)
#  ---------------------------------------------------------------------------
#  This review touches every second-half topic, one tiny piece at a time:
#
#    * Functions & modularization   average() and a function that calls it
#    * Data structures (dict)       total_items()
#    * File I/O + error handling     parse_numbers()  with try/except
#    * Classes                       the Counter class
#    * Inheritance                   ResettableCounter(Counter)
#    * Lambdas                       the `square` lambda
#    * Decorators                    base_points() with @add_bonus
#    * Debugging                     fix the bug in count_passes()
#
#  None of these is hard on its own -- they're all things you've done before.
#  Work top to bottom and run the tests as you go.
#
#  Finally, fill in get_dashboard_payload() with at least 3 of your own numbers.
# =============================================================================

"""Starter code for review2: Review: OOP/Advanced."""

# Change this to your real name.
student_name = "Alex Shaw"

# Leave this exactly as-is.
assignment_label = "review2"


# ── Functions & modularization ───────────────────────────────────────────────
def average(numbers):
    """Return the average of a list of numbers (return 0 for an empty list)."""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


def above_average_count(numbers):
    """Count how many numbers are above the average. CALL average() to get it."""
    avg = average(numbers)
    count = 0
    for number in numbers:
        if number > avg:
            count += 1
    return count


# ── Data structures ──────────────────────────────────────────────────────────
def total_items(cart):
    """Add up all the quantities (values) in a dictionary and return the total."""
    return sum(cart.values())


# ── File I/O + error handling ────────────────────────────────────────────────
def parse_numbers(lines):
    """Convert a list of text lines into ints, skipping any that aren't numbers.

    Use try / except around int(line) so bad lines are skipped, not crashes.
    Example: parse_numbers(["10", "x", "20"]) -> [10, 20]
    """
    numbers = []
    for line in lines:
        try:
            numbers.append(int(line))
        except ValueError:
            pass
    return numbers


# ── Classes ──────────────────────────────────────────────────────────────────
class Counter:
    """Counts up from zero."""

    def __init__(self):
        self.count = 0

    def add(self, n):
        self.count += n


# ── Inheritance ──────────────────────────────────────────────────────────────
class ResettableCounter(Counter):
    """A Counter that can also be reset back to zero."""

    def reset(self):
        self.count = 0


# ── Lambdas ──────────────────────────────────────────────────────────────────
# A lambda that returns x multiplied by itself.
square = lambda x: x * x


# ── Decorators (add_bonus is PROVIDED -- do not change it) ────────────────────
def add_bonus(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) + 5
    return wrapper


@add_bonus
def base_points(level):
    return level * 10


# ── Debugging ────────────────────────────────────────────────────────────────
def count_passes(results):
    """Count the True values in `results`. There is a bug -- fix the marked line."""
    passed = 0
    for result in results:
        if result:
            passed = passed + 1
    return passed


def get_dashboard_payload():
    """Return the data for your Review 2 widget.

    Put your own numbers in `values` and a matching label for each one in
    `labels`.  Keep at least 3 items in each list, with at least 2 of the
    numbers different from one another.
    """
    my_labels = ["Quiz", "Project", "Midterm", "Final"]
    my_values = [90, 94, 82, 88]

    return {
        "title": "Review: OOP/Advanced",
        "values": my_values,
        "labels": my_labels,
    }
