# =============================================================================
#  ASSIGNMENT 2 — Conditionals and Testing
#  File: assignments/assignment2/student_code.py
# =============================================================================
#
#  WHAT YOU'RE LEARNING THIS WEEK
#  ─────────────────────────────────────────────────────────────────────────────
#  CONDITIONALS (if / elif / else)
#  ─────────────────────────────────────────────────────────────────────────────
#  Conditionals let your program choose different paths depending on whether
#  something is True or False.  You already saw them in Assignment 1 — now
#  you'll use them more deliberately to build a "budget checker."
#
#  Comparison operators (these produce True or False):
#      ==   equal to                  (5 == 5  → True)
#      !=   not equal to              (5 != 3  → True)
#      >    greater than              (10 > 7  → True)
#      <    less than                 (3 < 10  → True)
#      >=   greater than or equal to  (5 >= 5  → True)
#      <=   less than or equal to     (4 <= 5  → True)
#
#  Logical operators (combine conditions):
#      and  — both must be True       (x > 0 and x < 100)
#      or   — at least one must be True  (color == "red" or color == "blue")
#      not  — flips True to False     (not is_raining)
#
#  Example:
#      purchase = 45.00
#      budget   = 60.00
#
#      if purchase > budget:
#          status = "Over budget!"
#      elif purchase == budget:
#          status = "Exactly on budget."
#      else:
#          status = "Within budget."
#
#  TESTING
#  ─────────────────────────────────────────────────────────────────────────────
#  This week you'll also learn what "automated tests" are.  A test is code that
#  checks whether YOUR code works correctly.  In this project, tests live in
#  `test_assignment.py` in the same folder.
#
#  How to run tests (GUI only — no terminal):
#    1. Open the Testing panel (beaker icon ⚗️ in the left sidebar).
#    2. Click "Run All Tests."
#    3. Green ✓ = passed.  Red ✗ = failed (read the message to see why).
#
#  You don't need to write tests yourself yet — just make sure your code passes
#  the existing ones.
#
#  YOUR TASK: Build a "budget checker" widget.
#  ─────────────────────────────────────────────────────────────────────────────
#  Track a few purchases you made (or make up realistic ones) and compare each
#  one to a budget limit.  Use conditionals to label each one ("OK", "Over",
#  "Warning", etc.).  Return the purchase amounts and their labels.
#
#  WORKED EXAMPLE (use completely different data!):
#      purchase_total = 42.50
#      budget_limit   = 60.00
#      → values: [42.50, 60.00, 17.50]   (purchase, budget, remaining)
#      → labels: ["Spent", "Budget", "Remaining"]
# =============================================================================

"""Starter code for assignment2: Conditionals, Testing."""

# ── Identity variables ────────────────────────────────────────────────────────
student_name = "Your Name"
assignment_label = "assignment2"


# ── Dashboard function ────────────────────────────────────────────────────────
def get_dashboard_payload():
    """Return dashboard-ready data for the Assignment 2 widget.

    Your job:
      1. Define a few purchase/expense amounts as variables.
      2. Define a budget limit.
      3. Use if/elif/else to classify each purchase (e.g., "OK" or "Over").
      4. Return your amounts and labels in the dictionary.

    Tips:
      - You can store results in a list by using list.append():
            labels = []
            labels.append("Groceries")   # adds "Groceries" to the end
      - You can mix hard-coded numbers and computed values in your lists.
    """
    # ── Define your purchases ──────────────────────────────────────────────
    # Replace these with your own spending categories and amounts.
    # purchase_groceries = 55.00
    # purchase_gas = 40.00
    # purchase_dining = 80.00
    # budget_limit = 60.00

    # ── Classify each purchase with conditionals ───────────────────────────
    # Example:
    #   if purchase_groceries <= budget_limit:
    #       groceries_status = "Within Budget"
    #   else:
    #       groceries_status = "Over Budget"

    # ── Build your output lists ────────────────────────────────────────────
    my_labels = []   # e.g., ["Groceries", "Gas", "Dining"]
    my_values = []   # e.g., [55.00, 40.00, 80.00]

    return {
        "title": "Conditionals, Testing",
        "values": my_values,
        "labels": my_labels,
    }

