# =============================================================================
#  ASSIGNMENT 8 — Advanced OOP
#  File: assignments/assignment8/student_code.py
# =============================================================================
#
#  WHAT YOU'RE LEARNING THIS WEEK
#  ─────────────────────────────────────────────────────────────────────────────
#  This week builds on last week's class basics with three powerful OOP concepts:
#
#  1. INHERITANCE — A child class can "inherit" everything from a parent class
#     and add or override what it needs.  This avoids repeating code.
#
#      class Animal:
#          def __init__(self, name):
#              self.name = name
#
#          def speak(self):
#              return "..."
#
#      class Dog(Animal):           # Dog inherits from Animal
#          def speak(self):         # OVERRIDE the parent's speak()
#              return f"{self.name} says Woof!"
#
#      class Cat(Animal):
#          def speak(self):
#              return f"{self.name} says Meow!"
#
#      dog = Dog("Rex")
#      cat = Cat("Luna")
#      print(dog.speak())           # Rex says Woof!
#      print(cat.speak())           # Luna says Meow!
#
#  2. super() — Call the parent class's method from inside the child.
#     Useful in __init__ to avoid re-writing the parent's setup code:
#
#      class Dog(Animal):
#          def __init__(self, name, breed):
#              super().__init__(name)   # call Animal.__init__(name)
#              self.breed = breed       # add the new attribute
#
#  3. POLYMORPHISM — "Many forms."  The same method name does different things
#     depending on which class the object belongs to.
#
#      animals = [Dog("Rex"), Cat("Luna"), Dog("Buddy")]
#      for animal in animals:
#          print(animal.speak())   # calls the RIGHT speak() for each type!
#
#  ── Class methods and static methods (bonus!) ────────────────────────────────
#
#      class MathHelper:
#          @staticmethod
#          def square(n):               # doesn't need self — use for utilities
#              return n * n
#
#          @classmethod
#          def from_string(cls, text):  # cls = the class itself, not an instance
#              return cls(int(text))
#
#  YOUR TASK: Build a "reporting objects" widget.
#  ─────────────────────────────────────────────────────────────────────────────
#  Create a parent class (e.g., Report) and at least two child classes that
#  override a shared method (e.g., generate_score()).  Collect instances of
#  the child classes in a list and loop over them to gather data.
#
#  WORKED EXAMPLE (use different data!):
#      student_levels = {"Ari": "gold", "Kai": "silver", "Paz": "bronze"}
#      → Create GoldStudent, SilverStudent classes (inheriting from Student)
#      → Each has a score() method returning a different base score
#      → Compute list of scores, then total, average, count
#      → values: [3, 265, 88.3]
#      → labels: ["# Students", "Total Points", "Avg Points"]
# =============================================================================

"""Starter code for assignment8: Advanced OOP."""

# ── Identity variables ────────────────────────────────────────────────────────
student_name = "Your Name"
assignment_label = "assignment8"


# =============================================================================
#  DEFINE YOUR CLASSES HERE (parent first, then children)
#  ─────────────────────────────────────────────────────────────────────────────
#  Example skeleton:
#
#      class Report:
#          """Base class for all report types."""
#
#          def __init__(self, label):
#              self.label = label
#
#          def generate_score(self):
#              """Override this in subclasses to return a numeric score."""
#              return 0
#
#          def summary(self):
#              return f"{self.label}: {self.generate_score()} pts"
#
#
#      class GoldReport(Report):
#          """Gold-tier report — highest score."""
#
#          def generate_score(self):
#              return 100       # override parent
#
#
#      class SilverReport(Report):
#          """Silver-tier report — mid-range score."""
#
#          def generate_score(self):
#              return 75        # override parent
#
#
#      class BronzeReport(Report):
#          """Bronze-tier report — base score."""
#
#          def generate_score(self):
#              return 50        # override parent
# =============================================================================


# ── Dashboard function ────────────────────────────────────────────────────────
def get_dashboard_payload():
    """Return dashboard-ready data for the Assignment 8 widget.

    Your job:
      1. Define a parent class and at least 2 child classes above.
      2. Create a list of mixed child class instances.
      3. Use polymorphism — call the SAME method on all objects in the list.
      4. Compute summary stats from the results.
      5. Return the stats as values and labels.
    """
    # ── Create a mixed list of instances ──────────────────────────────────
    # Replace with your own class names and data.
    # reports = [
    #     GoldReport("Alpha"),
    #     SilverReport("Beta"),
    #     BronzeReport("Gamma"),
    #     GoldReport("Delta"),
    # ]

    # ── Use polymorphism to gather scores ─────────────────────────────────
    # scores = [r.generate_score() for r in reports]  # calls correct method!
    # total   = sum(scores)
    # average = total / len(scores)
    # count   = len(reports)

    my_values = []
    my_labels = []

    return {
        "title": "Advanced OOP",
        "values": my_values,
        "labels": my_labels,
    }

