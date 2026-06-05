# =============================================================================
#  ASSIGNMENT 7 — OOP: Classes
#  File: assignments/assignment7/student_code.py
# =============================================================================
#
#  WHAT YOU'RE LEARNING THIS WEEK
#  ─────────────────────────────────────────────────────────────────────────────
#  OBJECT-ORIENTED PROGRAMMING (OOP) — A way of organizing code by grouping
#  related data and behavior into a single unit called a CLASS.
#
#  Think of a class as a BLUEPRINT, and objects (instances) as the actual
#  things built from that blueprint.
#
#      Blueprint: "Dog"        →  class Dog
#      Actual dog: "Rex"       →  rex = Dog("Rex", "Labrador", 3)
#
#  ── Defining a class ─────────────────────────────────────────────────────────
#
#      class Dog:
#          """Represents a dog."""
#
#          def __init__(self, name, breed, age):
#              """Constructor — runs when you create a new Dog instance.
#
#              `self` refers to THIS specific object being created.
#              All instance attributes must be set on `self`.
#              """
#              self.name  = name    # instance attribute: this dog's name
#              self.breed = breed   # instance attribute: this dog's breed
#              self.age   = age     # instance attribute: this dog's age
#
#          def bark(self):
#              """Instance method — a function that belongs to the class."""
#              return f"{self.name} says: Woof!"
#
#          def describe(self):
#              return f"{self.name} is a {self.age}-year-old {self.breed}."
#
#  ── Creating and using instances ─────────────────────────────────────────────
#
#      rex  = Dog("Rex",  "Labrador",  3)   # create one Dog
#      luna = Dog("Luna", "Poodle",    5)   # create another Dog
#
#      print(rex.name)         # Rex            — access an attribute
#      print(rex.bark())       # Rex says: Woof! — call a method
#      print(luna.describe())  # Luna is a 5-year-old Poodle.
#
#      # You can also change attributes after creation:
#      rex.age = 4
#
#  ── KEY TERMS ────────────────────────────────────────────────────────────────
#  class       — the blueprint / template
#  instance    — a specific object created from the class
#  __init__    — the constructor (runs on creation, always has `self` first)
#  self        — a reference to the current instance inside methods
#  attribute   — a variable stored ON the object (self.name, self.age)
#  method      — a function defined inside a class (always takes self)
#
#  YOUR TASK: Build an "expense model" widget.
#  ─────────────────────────────────────────────────────────────────────────────
#  Create an Expense class (or similar) that stores a category and amount.
#  Make a list of Expense instances, and use their attributes to compute
#  summary data for the dashboard.
#
#  WORKED EXAMPLE (use different data!):
#      transactions = [("Food", 14.2), ("Books", 22.0), ("Transport", 9.5)]
#      → Create an Expense class with category and amount attributes.
#      → Compute total, max expense, count.
#      → values: [45.7, 22.0, 3]
#      → labels: ["Total Spent", "Largest", "# Items"]
# =============================================================================

"""Starter code for assignment7: OOP: Classes."""

# ── Identity variables ────────────────────────────────────────────────────────
student_name = "Your Name"
assignment_label = "assignment7"


# =============================================================================
#  DEFINE YOUR CLASS HERE (above get_dashboard_payload)
#  ─────────────────────────────────────────────────────────────────────────────
#  Start simple: give it an __init__ and at least one method.
#
#  Example skeleton:
#
#      class Expense:
#          """Represents a single expense transaction."""
#
#          def __init__(self, category, amount):
#              """Create an Expense with a category name and dollar amount."""
#              self.category = category
#              self.amount   = amount
#
#          def is_large(self, threshold=20.0):
#              """Return True if this expense is above the threshold."""
#              return self.amount > threshold
#
#          def summary(self):
#              """Return a short string describing this expense."""
#              return f"{self.category}: ${self.amount:.2f}"
# =============================================================================


# ── Dashboard function ────────────────────────────────────────────────────────
def get_dashboard_payload():
    """Return dashboard-ready data for the Assignment 7 widget.

    Your job:
      1. Define a class above this function (see skeleton above).
      2. Create a list of instances from your class.
      3. Use the instance attributes and/or methods to compute summary stats.
      4. Return at least 3 stats as values with matching labels.
    """
    # ── Create instances ───────────────────────────────────────────────────
    # Replace with your own data.
    # transactions = [
    #     Expense("Food",      14.20),
    #     Expense("Books",     22.00),
    #     Expense("Transport",  9.50),
    #     Expense("Coffee",     5.75),
    # ]

    # ── Compute stats from instances ───────────────────────────────────────
    # Use a loop to pull out .amount (or whatever your attribute is called).
    # amounts = [e.amount for e in transactions]   # list comprehension shorthand
    # total   = sum(amounts)
    # largest = max(amounts)
    # count   = len(transactions)

    my_values = []
    my_labels = []

    return {
        "title": "OOP: Classes",
        "values": my_values,
        "labels": my_labels,
    }

