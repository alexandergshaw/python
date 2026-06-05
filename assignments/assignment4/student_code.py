# =============================================================================
#  ASSIGNMENT 4 — Functions and Modularization
#  File: assignments/assignment4/student_code.py
# =============================================================================
#
#  WHAT YOU'RE LEARNING THIS WEEK
#  ─────────────────────────────────────────────────────────────────────────────
#  FUNCTIONS — A function is a named, reusable block of code.  You've already
#  been using functions (print(), len(), sum(), range(), and get_dashboard_payload
#  itself!).  This week you learn to WRITE your own.
#
#  ── Defining a function ──────────────────────────────────────────────────────
#      def function_name(parameter1, parameter2):
#          """Docstring: describes what this function does."""
#          # ... body code ...
#          return result
#
#  • `def` — keyword that starts a function definition
#  • function_name — what you'll call it later (use snake_case by convention)
#  • parameters — inputs the function receives (optional, can have none)
#  • return — sends a value back to whoever called the function
#  • docstring — a string literal right after `def ...` that documents it
#
#  ── Calling a function ───────────────────────────────────────────────────────
#      result = function_name(value1, value2)
#
#  ── Example ──────────────────────────────────────────────────────────────────
#      def add(a, b):
#          """Return the sum of a and b."""
#          return a + b
#
#      total = add(3, 7)   # total is now 10
#      print(total)        # prints: 10
#
#  ── Default parameters ───────────────────────────────────────────────────────
#  You can give parameters default values so they're optional when calling:
#
#      def greet(name, greeting="Hello"):
#          return greeting + ", " + name + "!"
#
#      print(greet("Alex"))           # Hello, Alex!
#      print(greet("Sam", "Hi"))      # Hi, Sam!
#
#  WHY MODULARIZE?
#  ─────────────────────────────────────────────────────────────────────────────
#  Modularization means breaking a big program into small, focused functions.
#  Benefits:
#    • Each function does ONE thing and does it well (easier to understand).
#    • You can reuse a function anywhere without copy-pasting code.
#    • When something breaks, you only have to fix it in ONE place.
#    • You can test each function independently.
#
#  YOUR TASK: Build a "function splitter" widget.
#  ─────────────────────────────────────────────────────────────────────────────
#  Write HELPER FUNCTIONS that each do one small job (e.g., calculate_total,
#  calculate_average, find_largest), and then call them from inside
#  get_dashboard_payload().  This is modularization in practice!
#
#  WORKED EXAMPLE (use different data!):
#      expenses = [12.5, 8.25, 19.0]
#      → define: total_expenses(), average_expense(), largest_expense()
#      → values: [39.75, 13.25, 19.0]
#      → labels: ["Total", "Average", "Largest"]
# =============================================================================

"""Starter code for assignment4: Functions, Modularization."""

# ── Identity variables ────────────────────────────────────────────────────────
student_name = "Your Name"
assignment_label = "assignment4"


# =============================================================================
#  WRITE YOUR HELPER FUNCTIONS HERE (above get_dashboard_payload)
#  ─────────────────────────────────────────────────────────────────────────────
#  Define at least 2 helper functions that each do ONE specific calculation.
#  Then call them inside get_dashboard_payload() below.
#
#  Example helper function:
#
#      def calculate_total(numbers):
#          """Return the sum of all numbers in the list."""
#          total = 0
#          for n in numbers:
#              total += n
#          return total
#
#      def calculate_average(numbers):
#          """Return the mean average of the numbers list."""
#          if len(numbers) == 0:
#              return 0
#          return sum(numbers) / len(numbers)
# =============================================================================


# ── Dashboard function ────────────────────────────────────────────────────────
def get_dashboard_payload():
    """Return dashboard-ready data for the Assignment 4 widget.

    Your job:
      1. Define at least 2 helper functions above this one.
      2. Create your input data (a list of numbers).
      3. CALL your helper functions to compute results.
      4. Assemble those results into labels and values.
      5. Return the dictionary.

    Remember: don't do all the math inside this function!
    Delegate to your helpers — that's the whole point of modularization.
    """
    # ── Your input data ────────────────────────────────────────────────────
    # Replace with your own expenses, scores, or other numbers.
    # my_data = [12.5, 8.25, 19.0, 5.75, 22.00]

    # ── Call your helper functions ─────────────────────────────────────────
    # Example:
    #   total   = calculate_total(my_data)
    #   average = calculate_average(my_data)
    #   largest = max(my_data)

    # ── Build your output ──────────────────────────────────────────────────
    my_values = []   # results from your helper functions
    my_labels = []   # descriptive label for each result

    return {
        "title": "Functions, Modularization",
        "values": my_values,
        "labels": my_labels,
    }

