# =============================================================================
#  FINAL PROJECT — Full Dashboard Integration
#  File: assignments/final/student_code.py
# =============================================================================
#
#  CONGRATULATIONS -- YOU MADE IT TO THE FINAL!
#  ---------------------------------------------------------------------------
#  This capstone touches a little of EVERYTHING from the whole course.  Each
#  piece is small and familiar -- you've done every one of these before.  Work
#  top to bottom, run the tests as you go, and finish by filling in your own
#  dashboard data.
#
#  WHAT YOU'LL PRACTICE (one small piece each)
#  ---------------------------------------------------------------------------
#    * Branching / conditionals    grade_label()
#    * Loops                        count_active_days()
#    * Functions                    average()
#    * Data structures (dict)       total_items()
#    * File I/O + error handling     parse_numbers()  with try/except
#    * Classes                       the Wallet class
#    * Inheritance                   RewardsWallet(Wallet)
#    * Lambdas                       the `square` lambda
#    * Decorators                    base_points() with @add_bonus
#
#  Then make get_dashboard_payload() show off YOUR data -- something real you'd
#  like to visualize (study hours, budget, fitness, game scores, anything).
# =============================================================================

"""Starter code for final: Final Project Integration."""

# Make sure this is YOUR name -- it's the last time you'll change it!
student_name = "Alex Shaw"

# Leave this exactly as-is.
assignment_label = "final"


# ── Branching / conditionals ─────────────────────────────────────────────────
def grade_label(score):
    """Return "A" (90+), "B" (80-89), "C" (70-79), or "F" (below 70)."""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "F"


# ── Loops ────────────────────────────────────────────────────────────────────
def count_active_days(steps, goal):
    """Count how many values in `steps` are >= goal, using a loop."""
    count = 0
    for day in steps:
        if day >= goal:
            count += 1
    return count


# ── Functions ────────────────────────────────────────────────────────────────
def average(numbers):
    """Return the average of a list of numbers (0 for an empty list)."""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


# ── Data structures ──────────────────────────────────────────────────────────
def total_items(cart):
    """Add up all the quantities (values) in a dictionary and return the total."""
    return sum(cart.values())


# ── File I/O + error handling ────────────────────────────────────────────────
def parse_numbers(lines):
    """Convert a list of text lines into ints, skipping non-numbers (try/except).

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
class Wallet:
    """A wallet that tracks an owner and a money balance."""

    def __init__(self, owner):
        self.owner = owner
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount


# ── Inheritance ──────────────────────────────────────────────────────────────
class RewardsWallet(Wallet):
    """A Wallet that also earns reward points."""

    def reward_points(self):
        return self.balance // 10


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


def get_dashboard_payload():
    """Return the data for your Final Project widget.

    Make this YOUR data.  Put at least 3 of your own numbers in `values` and a
    matching label for each one in `labels`, with at least 2 numbers different.
    """
    my_labels = ["Savings", "Expenses", "Remaining"]
    my_values = [1200, 830, 370]

    return {
        "title": "Final Project Integration",
        "values": my_values,
        "labels": my_labels,
    }
