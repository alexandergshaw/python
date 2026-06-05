# =============================================================================
#  REVIEW 1 — Fundamentals Review (Weeks 1–5)
#  File: assignments/review1/student_code.py
# =============================================================================
#
#  WHAT THIS REVIEW COVERS
#  ─────────────────────────────────────────────────────────────────────────────
#  This is your chance to revisit everything from the first half of the course:
#
#  ┌─────────────────────────────────────────────────────────────────────────┐
#  │  TOPIC              │  QUICK REMINDER                                   │
#  ├─────────────────────────────────────────────────────────────────────────┤
#  │  Variables          │  name = value   (str, int, float, bool)           │
#  │  print / input      │  print("hi")  |  x = input("prompt: ")           │
#  │  Conditionals       │  if / elif / else with ==, !=, <, >, <=, >=       │
#  │  Logical operators  │  and, or, not                                     │
#  │  for loops          │  for item in collection:  / for i in range(n):   │
#  │  while loops        │  while condition:  (don't forget to update it!)  │
#  │  Lists              │  [a, b, c]  — index with [0], slice with [1:3]   │
#  │  List methods       │  .append(), .remove(), .sort(), len(), sum()      │
#  └─────────────────────────────────────────────────────────────────────────┘
#
#  REVIEW TIPS
#  ─────────────────────────────────────────────────────────────────────────────
#  • Try to write code FROM MEMORY before looking anything up.
#  • If something isn't working, add print() statements to see what your
#    variables contain at each step — this is the most important debugging
#    skill you can build.
#  • Re-read your previous student_code.py files — they're all YOUR work!
#
#  YOUR TASK: Recreate a "fundamentals review" widget that demonstrates skills
#  from Assignments 0–3.
#  ─────────────────────────────────────────────────────────────────────────────
#  Suggested approach:
#    1. Create a list of 4–6 numbers (scores, temperatures, prices — anything).
#    2. Use a loop to compute the total, average, and at least one conditional
#       classification (e.g., "Pass" if score >= 70 else "Fail").
#    3. Return at least 3 computed values in your payload.
#
#  WORKED EXAMPLE (use different data!):
#      score_inputs = ["88", "92", "74"]
#      scores = [int(s) for s in score_inputs]    # convert strings → ints
#      → average ≈ 84.67, min = 74, max = 92
#      → values: [84.67, 74, 92]
#      → labels: ["Average Score", "Lowest", "Highest"]
# =============================================================================

"""Starter code for review1: Review: Fundamentals."""

# ── Identity variables ────────────────────────────────────────────────────────
student_name = "Your Name"
assignment_label = "review1"


# ── Dashboard function ────────────────────────────────────────────────────────
def get_dashboard_payload():
    """Return dashboard-ready data for the Review 1 widget.

    Show off your week 1–5 skills:
      - Create variables of different types (int, float, str, bool).
      - Use a loop to compute summary statistics on a list of numbers.
      - Use at least one if/elif/else conditional to classify something.
      - Collect your results into labels and values lists, then return them.
    """
    # ── Your review data ───────────────────────────────────────────────────
    # Replace with your own list of numbers.
    # my_data = [88, 92, 74, 67, 95]

    # ── Use fundamentals to summarize the data ────────────────────────────
    # Compute things like: average, max, min, count of items above a threshold.
    # Use a for loop for at least one computation.

    # ── Build output ──────────────────────────────────────────────────────
    my_values = []   # at least 3 computed numbers
    my_labels = []   # matching descriptive label for each number

    return {
        "title": "Review: Fundamentals",
        "values": my_values,
        "labels": my_labels,
    }

