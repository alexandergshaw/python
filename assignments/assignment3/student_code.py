# =============================================================================
#  ASSIGNMENT 3 — Loops
#  File: assignments/assignment3/student_code.py
# =============================================================================
#
#  WHAT YOU'RE LEARNING THIS WEEK
#  ─────────────────────────────────────────────────────────────────────────────
#  LOOPS — Run the same block of code multiple times without repeating yourself.
#
#  ── for loops ────────────────────────────────────────────────────────────────
#  A `for` loop iterates over every item in a sequence (like a list) one at
#  a time, automatically stopping when it runs out of items.
#
#      fruits = ["apple", "banana", "cherry"]
#      for fruit in fruits:
#          print(fruit)         # prints "apple", then "banana", then "cherry"
#
#  Use range() when you want to loop a specific number of times:
#      for i in range(5):       # i takes values 0, 1, 2, 3, 4
#          print(i)
#
#      for i in range(1, 6):   # i takes values 1, 2, 3, 4, 5
#          print(i)
#
#  ── while loops ──────────────────────────────────────────────────────────────
#  A `while` loop keeps running as long as a condition is True.  Use it when
#  you don't know ahead of time how many iterations you need.
#
#      count = 0
#      while count < 3:
#          print("looping!")
#          count += 1           # count = count + 1  (shorthand for incrementing)
#
#  ⚠️  DANGER: If the condition never becomes False, you get an infinite loop!
#     Always make sure something inside the loop eventually makes it stop.
#
#  ── Accumulator pattern ──────────────────────────────────────────────────────
#  The most common loop pattern is accumulation: start with a "running total"
#  set to 0, then add each item to it inside the loop.
#
#      steps = [4200, 7000, 8100, 10020]
#      total = 0                   # start at zero
#      for s in steps:
#          total += s              # add each day's steps to the running total
#      average = total / len(steps)   # len() returns the number of items
#      print(average)             # 7330.0
#
#  ── Useful built-in functions for lists ──────────────────────────────────────
#      len(my_list)    → number of items (length)
#      sum(my_list)    → sum of all numbers
#      min(my_list)    → smallest number
#      max(my_list)    → largest number
#
#  YOUR TASK: Build a "habit streaks" widget.
#  ─────────────────────────────────────────────────────────────────────────────
#  Track a habit you perform daily (steps, push-ups, pages read, glasses of
#  water — anything works).  Store several days of data in a list.  Use a loop
#  to compute summary statistics (total, average, max, etc.).  Return those
#  stats as your widget data.
#
#  WORKED EXAMPLE (use different data!):
#      steps = [4200, 7000, 8100, 10020]
#      → compute: total, average, best day
#      → values: [29320, 7330, 10020]
#      → labels: ["Total Steps", "Daily Avg", "Best Day"]
# =============================================================================

"""Starter code for assignment3: Loops."""

# ── Identity variables ────────────────────────────────────────────────────────
student_name = "Your Name"
assignment_label = "assignment3"


# ── Dashboard function ────────────────────────────────────────────────────────
def get_dashboard_payload():
    """Return dashboard-ready data for the Assignment 3 widget.

    Your job:
      1. Define a list of daily measurements (steps, scores, anything numeric).
      2. Use a for loop (or while loop) to compute statistics like total,
         average, minimum, or maximum.
      3. Store those computed values in labels/values lists.
      4. Return them in the dictionary.

    Hint — computing an average:
        total = 0
        for value in my_data:
            total += value
        average = total / len(my_data)

    Or use Python's built-in sum():
        average = sum(my_data) / len(my_data)
    """
    # ── Your raw daily data ────────────────────────────────────────────────
    # Replace this with your own list of numbers.
    # daily_data = [4200, 7000, 8100, 10020, 6500]

    # ── Use a loop to compute statistics ──────────────────────────────────
    # Example:
    #   total   = sum(daily_data)
    #   average = total / len(daily_data)
    #   best    = max(daily_data)

    # ── Return your computed stats ─────────────────────────────────────────
    my_values = []   # e.g., [total, average, best]
    my_labels = []   # e.g., ["Total", "Average", "Best Day"]

    return {
        "title": "Loops",
        "values": my_values,
        "labels": my_labels,
    }

