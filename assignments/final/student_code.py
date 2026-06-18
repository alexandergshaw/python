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
student_name = "Your Name"

# Leave this exactly as-is.
assignment_label = "final"


# ── Branching / conditionals ─────────────────────────────────────────────────
def grade_label(score):
    """Return "A" (90+), "B" (80-89), "C" (70-79), or "F" (below 70)."""
    # TODO: use if / elif / else to return the right letter.
    return ""


# ── Loops ────────────────────────────────────────────────────────────────────
def count_active_days(steps, goal):
    """Count how many values in `steps` are >= goal, using a loop."""
    # TODO: use the counting pattern (start at 0, add 1 when steps reach goal).
    return 0


# ── Functions ────────────────────────────────────────────────────────────────
def average(numbers):
    """Return the average of a list of numbers (0 for an empty list)."""
    # TODO: return the sum divided by the count (or 0 if empty).
    return 0


# ── Data structures ──────────────────────────────────────────────────────────
def total_items(cart):
    """Add up all the quantities (values) in a dictionary and return the total."""
    # TODO: sum the dictionary's values (0 for an empty dict).
    return 0


# ── File I/O + error handling ────────────────────────────────────────────────
def parse_numbers(lines):
    """Convert a list of text lines into ints, skipping non-numbers (try/except).

    Example: parse_numbers(["10", "x", "20"]) -> [10, 20]
    """
    # TODO: loop over lines; try int(line); skip on ValueError.
    return []


# ── Classes ──────────────────────────────────────────────────────────────────
class Wallet:
    """A wallet that tracks an owner and a money balance."""

    # TODO: write __init__(self, owner) so it stores self.owner and sets
    #       self.balance to 0.

    # TODO: write deposit(self, amount) so it adds amount to self.balance.
    pass


# ── Inheritance ──────────────────────────────────────────────────────────────
class RewardsWallet(Wallet):
    """A Wallet that also earns reward points."""

    # TODO: write reward_points(self) that returns self.balance // 10
    #       (whole reward points, one for every 10 in the balance).
    #       You inherit __init__ and deposit() from Wallet.
    pass


# ── Lambdas ──────────────────────────────────────────────────────────────────
# TODO: replace this stub with a lambda that returns x times itself.
square = lambda x: None


# ── Decorators (add_bonus is PROVIDED -- do not change it) ────────────────────
def add_bonus(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) + 5
    return wrapper


# TODO: put @add_bonus above this function, and return level * 10.
def base_points(level):
    return 0


def get_dashboard_payload():
    """Return the data for your Final Project widget.

    Make this YOUR data.  Put at least 3 of your own numbers in `values` and a
    matching label for each one in `labels`, with at least 2 numbers different.
    """
    my_labels = []
    my_values = []

    return {
        "title": "Final Project Integration",
        "values": my_values,
        "labels": my_labels,
    }
