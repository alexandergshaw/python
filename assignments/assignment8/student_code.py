# =============================================================================
#  ASSIGNMENT 8 — Advanced OOP: Inheritance
#  File: assignments/assignment8/student_code.py
# =============================================================================
#
#  WHAT YOU'RE LEARNING THIS WEEK
#  ---------------------------------------------------------------------------
#  INHERITANCE lets one class build on another.  The CHILD class automatically
#  gets everything the PARENT has, and can:
#     * ADD new methods of its own, and
#     * OVERRIDE (replace) a parent method by defining one with the same name.
#
#      class Animal:
#          def __init__(self, name):
#              self.name = name
#          def sound(self):
#              return "..."
#
#      class Cat(Animal):           # Cat inherits from Animal
#          def sound(self):         # OVERRIDE: replace the parent's version
#              return "meow"
#
#      c = Cat("Felix")
#      c.name        # "Felix"   <- inherited from Animal automatically
#      c.sound()     # "meow"    <- Cat's own version
#
#  YOUR TASK (two small things)
#  ---------------------------------------------------------------------------
#  The `Account` class below is DONE for you -- do NOT change it.  Your job is
#  to write a child class `SavingsAccount` that inherits from `Account` and:
#
#     1. OVERRIDES `kind()` so it returns "savings" instead of "basic".
#     2. ADDS a new method `add_interest(self, rate)` that grows the balance:
#        it should increase self.balance by (self.balance * rate).
#        For example, a balance of 100 with rate 0.10 becomes 110.
#
#  You do NOT need to write __init__ for SavingsAccount -- it is inherited from
#  Account, so SavingsAccount(100) already sets self.balance to 100.
#
#  Then fill in `get_dashboard_payload()` with at least 3 of your own numbers.
#
#  WORKED EXAMPLE (use different data, don't copy it)
#  ---------------------------------------------------------------------------
#      title  = "Account Balances"
#      labels = ["Checking", "Savings", "Bonus"]
#      values = [100, 110, 25]
# =============================================================================

"""Starter code for assignment8: Advanced OOP."""

# Change this to your real name.
student_name = "Alex Shaw"

# Leave this exactly as-is.
assignment_label = "assignment8"


# ---------------------------------------------------------------------------
#  PROVIDED FOR YOU -- do not change this class.
# ---------------------------------------------------------------------------
class Account:
    """A basic bank account that just holds a balance."""

    def __init__(self, balance):
        self.balance = balance

    def kind(self):
        return "basic"


# ---------------------------------------------------------------------------
#  YOUR CODE -- write the SavingsAccount class below.
# ---------------------------------------------------------------------------
class SavingsAccount(Account):
    """A savings account: inherits from Account, adds interest."""

    def kind(self):
        return "savings"

    def add_interest(self, rate):
        self.balance += self.balance * rate


def get_dashboard_payload():
    """Return the data for your Assignment 8 widget.

    Put your own numbers in `values` and a matching label for each one in
    `labels`.  Keep at least 3 items in each list, with at least 2 of the
    numbers different from one another.
    """
    my_labels = ["Checking", "Savings", "Bonus"]
    my_values = [100, 110, 25]

    return {
        "title": "Advanced OOP",
        "values": my_values,
        "labels": my_labels,
    }
