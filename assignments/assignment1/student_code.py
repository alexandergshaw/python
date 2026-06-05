# =============================================================================
#  ASSIGNMENT 1 — Variables, I/O, and Branching
#  File: assignments/assignment1/student_code.py
# =============================================================================
#
#  WHAT YOU'RE LEARNING THIS WEEK
#  ─────────────────────────────────────────────────────────────────────────────
#  This assignment covers the three most fundamental building blocks of Python:
#
#  1. VARIABLES — A variable is a named storage container for a piece of data.
#     You create one by writing:  name = value
#
#       temperature = 72          # an integer (whole number)
#       city = "Denver"           # a string (text in quotes)
#       is_raining = False        # a boolean (True or False)
#       price = 9.99              # a float (decimal number)
#
#     Variable names can't start with a number, can't have spaces (use _
#     instead), and are case-sensitive (Temperature ≠ temperature).
#
#  2. INPUT / OUTPUT — Python reads input from the user with input() and
#     prints output with print().
#
#       name = input("What is your name? ")  # pauses and waits for typing
#       print("Hello,", name)                # prints: Hello, Alex
#
#     IMPORTANT for this assignment: Because your code runs automatically in
#     the browser (not interactively), you should NOT call input() inside
#     get_dashboard_payload().  Instead, hard-code your data directly as
#     variable values.  You can still use print() for debugging — it shows
#     up in the browser console.
#
#  3. BRANCHING (if / elif / else) — Branching lets your program make
#     decisions.  Use it to run different code depending on a condition.
#
#       score = 85
#       if score >= 90:
#           grade = "A"
#       elif score >= 80:
#           grade = "B"      # ← this one runs because 85 >= 80
#       elif score >= 70:
#           grade = "C"
#       else:
#           grade = "F"
#
#     Rules:
#       • The condition after `if` or `elif` must evaluate to True or False.
#       • Use == to compare equality (NOT a single =, which assigns values).
#       • Use >, <, >=, <=, != for numeric comparisons.
#       • The else block runs when none of the above conditions matched.
#       • Indentation (4 spaces) is what Python uses instead of { } braces.
#
#  YOUR TASK: Build a "daily summary" widget.
#  ─────────────────────────────────────────────────────────────────────────────
#  Imagine you tracked something each day this week — temperatures, steps
#  walked, hours studied, calories eaten, whatever you like.  Store those
#  numbers in a list and use branching to classify each one (e.g., "High",
#  "Medium", "Low").  Then fill get_dashboard_payload() with that data.
#
#  WHAT IS A LIST?
#  ─────────────────────────────────────────────────────────────────────────────
#  A list is an ordered collection of values, written with square brackets [].
#  Items are separated by commas.
#
#      days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
#      temps = [68, 72, 75, 70, 65]
#
#  You access items by their index (position), starting at 0:
#      print(temps[0])   # prints 68
#      print(temps[2])   # prints 75
#
#  WORKED EXAMPLE (use different data — don't copy this!)
#  ─────────────────────────────────────────────────────────────────────────────
#  Data: temperatures = [68, 71, 75], city = "Austin"
#  → labels: ["Mon Temp", "Tue Temp", "Wed Temp"]
#  → values: [68, 71, 75]
#  → title:  "Austin Daily Temperatures"
# =============================================================================

"""Starter code for assignment1: Variables, I/O, Branching."""

# ── Identity variables ────────────────────────────────────────────────────────
# Change this to your real name.
student_name = "Your Name"

# DO NOT change this line.
assignment_label = "assignment1"


# ── Dashboard function ────────────────────────────────────────────────────────
def get_dashboard_payload():
    """Return dashboard-ready data for the Assignment 1 widget.

    Your job:
      1. Create some variables to represent your daily data
         (temperatures, steps, scores — your choice).
      2. Optionally use if/elif/else to classify or transform your values.
      3. Build labels and values lists from your data.
      4. Return them in the dictionary below.

    Remember the rules:
      - At least 3 items in each list.
      - Same number of labels and values.
      - At least 2 different numbers in values.
    """
    # ── Step 1: Define your data as variables ──────────────────────────────
    # Replace these with your own numbers and labels.
    # Example:
    #   day1_temp = 68
    #   day2_temp = 71
    #   day3_temp = 75

    # ── Step 2: (Optional) Use branching to classify values ────────────────
    # Example:
    #   if day1_temp > 70:
    #       day1_label = "Warm"
    #   else:
    #       day1_label = "Cool"

    # ── Step 3: Assemble your lists ────────────────────────────────────────
    # Replace these empty lists with your data.
    my_labels = []   # e.g., ["Monday", "Tuesday", "Wednesday"]
    my_values = []   # e.g., [68, 71, 75]

    return {
        # Write a short, descriptive title for your widget.
        "title": "Variables, I/O, Branching",

        # Your list of numbers (at least 3, at least 2 must be different).
        "values": my_values,

        # Your list of labels (same count as values, all non-empty strings).
        "labels": my_labels,
    }

