# =============================================================================
#  ASSIGNMENT 5 — Data Structures
#  File: assignments/assignment5/student_code.py
# =============================================================================
#
#  WHAT YOU'RE LEARNING THIS WEEK
#  ─────────────────────────────────────────────────────────────────────────────
#  Python has four built-in data structures.  Each has strengths and ideal use
#  cases.  Here's a quick comparison:
#
#  ┌───────────────┬────────────────────────────────────────────────────────┐
#  │  Structure    │  Description & When to Use                             │
#  ├───────────────┼────────────────────────────────────────────────────────┤
#  │  list []      │  Ordered, changeable, allows duplicates.               │
#  │               │  Use when order matters or you need to add/remove.     │
#  │               │  fruits = ["apple", "banana", "apple"]                 │
#  ├───────────────┼────────────────────────────────────────────────────────┤
#  │  tuple ()     │  Ordered, UNCHANGEABLE (immutable), allows duplicates. │
#  │               │  Use for data that should never change (coordinates,   │
#  │               │  RGB values, etc.)                                     │
#  │               │  point = (10, 20)                                      │
#  ├───────────────┼────────────────────────────────────────────────────────┤
#  │  dict {}      │  Key–value pairs, keys are unique, VERY fast lookups.  │
#  │               │  Use when you want to name your data.                  │
#  │               │  prices = {"apple": 1.50, "banana": 0.75}              │
#  ├───────────────┼────────────────────────────────────────────────────────┤
#  │  set {}       │  Unordered, NO duplicates.                             │
#  │               │  Use when you care about unique values only.           │
#  │               │  unique_colors = {"red", "blue", "green"}              │
#  └───────────────┴────────────────────────────────────────────────────────┘
#
#  ── Working with dictionaries (most important this week) ─────────────────────
#
#      groceries = {"apples": 4, "milk": 2, "eggs": 12}
#
#      # Access a value by its key:
#      print(groceries["apples"])    # 4
#
#      # Add a new key-value pair:
#      groceries["bread"] = 1
#
#      # Check if a key exists:
#      if "milk" in groceries:
#          print("we have milk")
#
#      # Loop over all key-value pairs:
#      for item, quantity in groceries.items():
#          print(item, "→", quantity)
#
#      # Get just the keys or just the values:
#      list(groceries.keys())     # ["apples", "milk", "eggs", "bread"]
#      list(groceries.values())   # [4, 2, 12, 1]
#
#  ── List of dictionaries (very common pattern!) ───────────────────────────────
#      students = [
#          {"name": "Ana",  "grade": 92},
#          {"name": "Bo",   "grade": 85},
#          {"name": "Cara", "grade": 78},
#      ]
#      for s in students:
#          print(s["name"], "got", s["grade"])
#
#  YOUR TASK: Build a "shopping map" widget.
#  ─────────────────────────────────────────────────────────────────────────────
#  Create a dictionary that maps item names to quantities (or prices).  Loop
#  over it to build your labels and values lists.
#
#  WORKED EXAMPLE (use different data!):
#      groceries = {"apples": 4, "milk": 1, "eggs": 12, "bread": 2}
#      → labels: list(groceries.keys())    # ["apples", "milk", "eggs", "bread"]
#      → values: list(groceries.values())  # [4, 1, 12, 2]
# =============================================================================

"""Starter code for assignment5: Data Structures."""

# ── Identity variables ────────────────────────────────────────────────────────
student_name = "Your Name"
assignment_label = "assignment5"


# ── Dashboard function ────────────────────────────────────────────────────────
def get_dashboard_payload():
    """Return dashboard-ready data for the Assignment 5 widget.

    Your job:
      1. Create a dictionary mapping names to numeric values.
         (e.g., a shopping list with quantities, a grade book with scores,
         a contact list with ages — anything you like.)
      2. Loop over the dictionary's items to build labels and values lists.
      3. Return those lists in the payload dictionary.

    Bonus challenge: Sort the items by value before building your lists.
    Hint: sorted(my_dict.items(), key=lambda x: x[1])
    """
    # ── Create your dictionary ─────────────────────────────────────────────
    # Replace with your own key-value data.
    # my_data = {
    #     "Apples":  4,
    #     "Milk":    2,
    #     "Eggs":   12,
    #     "Bread":   1,
    #     "Cheese":  3,
    # }

    # ── Build labels and values from the dictionary ────────────────────────
    # Option A — direct conversion:
    #   my_labels = list(my_data.keys())
    #   my_values = list(my_data.values())
    #
    # Option B — loop (gives you more control):
    #   my_labels = []
    #   my_values = []
    #   for name, quantity in my_data.items():
    #       my_labels.append(name)
    #       my_values.append(quantity)

    my_labels = []
    my_values = []

    return {
        "title": "Data Structures",
        "values": my_values,
        "labels": my_labels,
    }

