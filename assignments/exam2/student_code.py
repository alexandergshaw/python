# =============================================================================
#  EXAM 2 — Test 2 Prep
#  File: assignments/exam2/student_code.py
# =============================================================================
#
#  WHAT THIS FILE IS FOR
#  ─────────────────────────────────────────────────────────────────────────────
#  This is your second pre-exam practice assignment, covering everything from
#  the second half of the course.  Use it as a personal study session — write
#  code that genuinely challenges you.  If it's too easy, you're not growing!
#
#  EXAM 2 TOPICS TO REVIEW
#  ─────────────────────────────────────────────────────────────────────────────
#  ✓  Functions — definition, parameters, defaults, return values
#  ✓  Data Structures — list, dict, tuple, set and their use cases
#  ✓  File I/O — open(), read, write, append, "with" statement
#  ✓  Error Handling — try/except, common exception types
#  ✓  OOP Basics — class, __init__, self, attributes, instance methods
#  ✓  Inheritance — class Child(Parent), super().__init__()
#  ✓  Polymorphism — same method name, different behavior
#  ✓  Lambda functions — lambda x: expression
#  ✓  map() and filter()
#  ✓  Decorators — wrapping functions to add behavior
#
#  EXAM STUDY CHECKLIST
#  ─────────────────────────────────────────────────────────────────────────────
#  □  Can you write a class with inheritance from scratch?
#  □  Can you explain what `super().__init__()` does?
#  □  Can you sort a list of dictionaries by a nested key using lambda?
#  □  Can you write a decorator that times how long a function takes?
#  □  Can you chain map() and filter() calls?
#  □  Can you handle a missing key in a dictionary without crashing?
#        → Use: my_dict.get("key", default_value)
#  □  Can you predict what this outputs?
#        class A:
#            def greet(self): return "A"
#        class B(A):
#            def greet(self): return "B"
#        objects = [A(), B(), A()]
#        print([o.greet() for o in objects])    # ["A", "B", "A"]
#
#  PRACTICE CHALLENGES
#  ─────────────────────────────────────────────────────────────────────────────
#  Challenge 1: Write a class BankAccount with deposit() and withdraw() methods.
#               Raise a ValueError if a withdrawal exceeds the balance.
#  Challenge 2: Use map() to convert a list of Fahrenheit temps to Celsius.
#               Formula: C = (F - 32) * 5 / 9
#  Challenge 3: Write a decorator that counts how many times a function is called.
#  Challenge 4: Given a list of dicts [{"name": ..., "score": ...}, ...],
#               use filter() to keep only scores above 80, and sorted() to
#               sort the remaining items by score descending.
#
#  YOUR TASK: Complete get_dashboard_payload() with exam-style code.
#  ─────────────────────────────────────────────────────────────────────────────
#  WORKED EXAMPLE (use different data!):
#      timed_prompts = ["loops", "files", "classes", "lambdas"]
#      → each "prompt" maps to a self-assessed comfort score
#      → values: [comfort scores]
#      → labels: topic names
# =============================================================================

"""Starter code for exam2: Test 2 Prep."""

# ── Identity variables ────────────────────────────────────────────────────────
student_name = "Your Name"
assignment_label = "exam2"


# ── Dashboard function ────────────────────────────────────────────────────────
def get_dashboard_payload():
    """Return dashboard-ready data for the Exam 2 prep widget.

    Challenge yourself this time:
      - Use a class with at least one method.
      - Use a lambda somewhere.
      - Use try/except around something that could fail.
      - Return at least 3 meaningful computed values — not hard-coded ones.
    """
    # ── Your study data ────────────────────────────────────────────────────
    # Idea: rate your confidence in each topic 1–10, then compute stats.
    # topics = {
    #     "Functions":    8,
    #     "OOP":          7,
    #     "Lambdas":      6,
    #     "Decorators":   5,
    #     "File I/O":     9,
    # }

    # ── Compute summary stats ──────────────────────────────────────────────
    # scores = list(topics.values())
    # avg    = sum(scores) / len(scores)
    # best   = max(scores)
    # worst  = min(scores)

    my_values = []
    my_labels = []

    return {
        "title": "Test 2 Prep",
        "values": my_values,
        "labels": my_labels,
    }

