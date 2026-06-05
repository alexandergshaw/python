# =============================================================================
#  EXAM 1 — Test 1 Prep
#  File: assignments/exam1/student_code.py
# =============================================================================
#
#  WHAT THIS FILE IS FOR
#  ─────────────────────────────────────────────────────────────────────────────
#  This is your pre-exam practice assignment.  Completing it unlocks an exam-
#  prep widget on the dashboard, but more importantly it's a chance to make
#  sure you can write Python confidently from scratch, covering everything
#  from the first half of the course.
#
#  EXAM 1 TOPICS TO REVIEW
#  ─────────────────────────────────────────────────────────────────────────────
#  ✓  Variables — creating and naming them, the four basic types
#  ✓  print() — displaying output
#  ✓  Conditionals — if / elif / else, comparison operators, logical operators
#  ✓  for loops — iterating over lists and ranges
#  ✓  while loops — condition-based repetition, avoiding infinite loops
#  ✓  Lists — creating, indexing, slicing, appending, len / sum / min / max
#
#  EXAM STUDY CHECKLIST
#  ─────────────────────────────────────────────────────────────────────────────
#  □  Can you write a for loop from memory (no looking it up)?
#  □  Can you calculate the average of a list using a loop AND using sum()?
#  □  Can you write nested if/elif/else (conditionals inside conditionals)?
#  □  Do you know the difference between = (assign) and == (compare)?
#  □  Can you explain what `range(1, 10, 2)` produces?   (1, 3, 5, 7, 9)
#  □  Can you access the third item in a list? (hint: index 2, not 3!)
#  □  Can you predict what this prints?
#         x = 10
#         for i in range(3):
#             x += i
#         print(x)               # answer: 13  (10 + 0 + 1 + 2)
#
#  PRACTICE CHALLENGES (write these yourself, then check your answers)
#  ─────────────────────────────────────────────────────────────────────────────
#  Challenge 1: Given a list of quiz scores, print only the ones above 80.
#  Challenge 2: Count how many items in a list are negative numbers.
#  Challenge 3: Write a while loop that prints even numbers from 0 to 20.
#  Challenge 4: Given a list, create a new list with each value doubled.
#
#  YOUR TASK: Complete get_dashboard_payload() with practice data.
#  ─────────────────────────────────────────────────────────────────────────────
#  Use this file to practice writing Python from scratch.  Make up some quiz
#  or practice scores, compute some statistics with loops, and return them.
#
#  WORKED EXAMPLE (use different data!):
#      practice_answers = [True, False, True, True]
#      correct = sum(1 for a in practice_answers if a)   # counts True values
#      → values: [4, 3, 1]
#      → labels: ["Questions", "Correct", "Incorrect"]
# =============================================================================

"""Starter code for exam1: Test 1 Prep."""

# ── Identity variables ────────────────────────────────────────────────────────
student_name = "Your Name"
assignment_label = "exam1"


# ── Dashboard function ────────────────────────────────────────────────────────
def get_dashboard_payload():
    """Return dashboard-ready data for the Exam 1 prep widget.

    Challenge yourself:
      - Write the whole function from scratch using what you've learned.
      - Use at least one loop AND one conditional.
      - Compute at least 3 meaningful statistics or values from your data.
      - Don't just hard-code the output — actually compute it!
    """
    # ── Your practice data ─────────────────────────────────────────────────
    # Example: a list of quiz scores from this week's study session.
    # quiz_scores = [78, 85, 90, 62, 95, 88]

    # ── Compute statistics using loops and conditionals ────────────────────
    # Ideas:
    #   - total score, average, highest, lowest
    #   - number of scores above passing threshold
    #   - number of scores below a certain value

    # ── Build your output ──────────────────────────────────────────────────
    my_values = []   # at least 3 numbers
    my_labels = []   # a matching label for each number

    return {
        "title": "Test 1 Prep",
        "values": my_values,
        "labels": my_labels,
    }

