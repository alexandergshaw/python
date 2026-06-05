# =============================================================================
#  REVIEW 2 — OOP and Advanced Python Review (Weeks 7–14)
#  File: assignments/review2/student_code.py
# =============================================================================
#
#  WHAT THIS REVIEW COVERS
#  ─────────────────────────────────────────────────────────────────────────────
#  You've come a long way!  This review covers the second half of the course:
#
#  ┌─────────────────────────────────────────────────────────────────────────┐
#  │  TOPIC              │  QUICK REMINDER                                   │
#  ├─────────────────────────────────────────────────────────────────────────┤
#  │  Functions          │  def name(params): ... return value               │
#  │  Default params     │  def f(x, y=10): ...                              │
#  │  Data Structures    │  list, tuple, dict, set — know when to use each   │
#  │  File I/O           │  with open("f.txt", "r") as f: ...               │
#  │  Error Handling     │  try: ... except SomeError as e: ...             │
#  │  OOP Basics         │  class, __init__, self, attributes, methods       │
#  │  Inheritance        │  class Child(Parent): ...  super().__init__()    │
#  │  Polymorphism       │  same method name, different behavior per class   │
#  │  Lambda             │  lambda x: x * 2                                  │
#  │  map / filter       │  list(map(f, items)) / list(filter(f, items))    │
#  │  Decorators         │  def dec(func): def wrapper(): ... return wrapper │
#  └─────────────────────────────────────────────────────────────────────────┘
#
#  REVIEW TIPS
#  ─────────────────────────────────────────────────────────────────────────────
#  • Can you write a class with __init__ and two methods from memory?
#  • Can you create a subclass that overrides one method?
#  • Can you use a lambda inside sorted() to sort a list of dicts by a key?
#  • Can you write a decorator that prints "START" and "END" around a function?
#  • Do you know the difference between @staticmethod and @classmethod?
#
#  YOUR TASK: Demonstrate second-half skills in a single widget.
#  ─────────────────────────────────────────────────────────────────────────────
#  Build something that uses:
#    ✓ A class with at least 2 attributes and 1 method
#    ✓ A list of instances
#    ✓ A lambda to sort or transform data
#    ✓ At least one try/except for safe data handling
#    ✓ A loop to collect results from instances
#
#  WORKED EXAMPLE (use different data!):
#      class_scores = {"Quiz": 90, "Project": 94, "Midterm": 82, "Final": 88}
#      → labels: list(class_scores.keys())
#      → values: list(class_scores.values())
# =============================================================================

"""Starter code for review2: Review: OOP/Advanced."""

# ── Identity variables ────────────────────────────────────────────────────────
student_name = "Your Name"
assignment_label = "review2"


# =============================================================================
#  DEFINE YOUR CLASS(ES) HERE
#  ─────────────────────────────────────────────────────────────────────────────
#  Aim for a class that:
#    - Has an __init__ with at least 2 parameters (besides self)
#    - Has at least 1 method that returns a computed value
#    - Is used to create at least 3 different instances
# =============================================================================


# ── Dashboard function ────────────────────────────────────────────────────────
def get_dashboard_payload():
    """Return dashboard-ready data for the Review 2 widget.

    Show off your week 7–14 skills in ONE cohesive function:
      - Instantiate your class(es)
      - Use a lambda to sort or transform
      - Use try/except around any parsing/conversion
      - Return meaningful stats
    """
    # ── Your review implementation ─────────────────────────────────────────
    # Write your OOP + advanced Python code here.

    my_values = []
    my_labels = []

    return {
        "title": "Review: OOP/Advanced",
        "values": my_values,
        "labels": my_labels,
    }

