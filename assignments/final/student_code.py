# =============================================================================
#  FINAL PROJECT — Full Dashboard Integration
#  File: assignments/final/student_code.py
# =============================================================================
#
#  CONGRATULATIONS — YOU MADE IT TO THE FINAL!
#  ─────────────────────────────────────────────────────────────────────────────
#  This is the capstone assignment for the entire course.  Everything you've
#  learned over 16 weeks comes together here: variables, branching, loops,
#  functions, data structures, file I/O, error handling, OOP, lambdas,
#  decorators, and CI/CD.
#
#  WHAT YOUR FINAL PROJECT SHOULD DEMONSTRATE
#  ─────────────────────────────────────────────────────────────────────────────
#  Your get_dashboard_payload() should be the most complete, well-organized,
#  and meaningful Python function you've written.  Aim to include:
#
#    ✓ At least one class with __init__, attributes, and methods
#    ✓ Inheritance or polymorphism (if applicable to your data)
#    ✓ A function (or several) defined above get_dashboard_payload
#    ✓ A loop that computes something interesting
#    ✓ At least one conditional
#    ✓ A lambda used with map(), filter(), or sorted()
#    ✓ Error handling around any parsing or risky operation
#    ✓ Meaningful, descriptive variable names throughout
#    ✓ At least one docstring per class and function you define
#
#  DESIGN YOUR OWN DATA
#  ─────────────────────────────────────────────────────────────────────────────
#  The whole point of this dashboard is that it shows YOUR data — not made-up
#  placeholder values.  Think about something real you'd like to visualize:
#
#    📊 Your weekly study hours across different subjects
#    💰 Monthly budget categories and how much you spent in each
#    🏃 Fitness stats: distance run, calories burned, rest days
#    📚 Book ratings you've given to books you've read this year
#    🎮 High scores across your favorite games
#    🌡️  Weather data from your city over the past month
#    ☕ Coffee shops you've visited, rated 1–10
#
#  ...the more personal and real, the more impressive your final widget!
#
#  HOW THE WIDGET UNLOCKS
#  ─────────────────────────────────────────────────────────────────────────────
#  The dashboard engine runs your code automatically and checks that
#  get_dashboard_payload() returns a valid dict with:
#    • "title"  — a non-empty string
#    • "values" — a list of at LEAST 3 numbers, with at least 2 distinct values
#    • "labels" — a list of non-empty strings, same length as "values"
#
#  If all 16 assignments are complete, a special celebration banner appears.
#
#  FINAL CHECKLIST
#  ─────────────────────────────────────────────────────────────────────────────
#  □  student_name is changed to your real name
#  □  get_dashboard_payload() returns valid, non-trivial data
#  □  All tests pass in the Testing panel (beaker icon)
#  □  GitHub Actions checks are green on your pull request
#  □  You have at least one class, one function, one loop, one conditional
#  □  You have docstrings on every function and class you wrote
#  □  Your data is meaningful and describes something real to you
#  □  You merged the PR and the live Vercel dashboard shows your widget
#
#  WORKED EXAMPLE (use completely different data — this is YOUR final project!)
#  ─────────────────────────────────────────────────────────────────────────────
#  widget_data = [
#      {"label": "Savings",   "value": 1200},
#      {"label": "Expenses",  "value":  830},
#      {"label": "Remaining", "value":  370},
#  ]
#  → values: [d["value"] for d in widget_data]   # [1200, 830, 370]
#  → labels: [d["label"] for d in widget_data]   # ["Savings", "Expenses", ...]
# =============================================================================

"""Starter code for final: Final Project Integration."""

# ── Identity variables ────────────────────────────────────────────────────────
# Make sure this is YOUR name — it's the last time you'll change it!
student_name = "Your Name"

# DO NOT change this.
assignment_label = "final"


# =============================================================================
#  WRITE YOUR CLASSES AND HELPER FUNCTIONS HERE
#  ─────────────────────────────────────────────────────────────────────────────
#  Organize your code well:
#    1. Classes first (with docstrings and __init__)
#    2. Helper functions below the classes (with docstrings)
#    3. get_dashboard_payload() last — it calls everything above
#
#  The cleaner and more organized this file is, the better you'll do!
# =============================================================================


# ── Dashboard function ────────────────────────────────────────────────────────
def get_dashboard_payload():
    """Return dashboard-ready data for the Final Project widget.

    This is your masterpiece.  Use everything you've learned:
      - Classes and OOP
      - Functions (your helpers above)
      - Loops and conditionals
      - Lambda expressions
      - Error handling
      - Meaningful, real data you care about

    The widget on the live dashboard will show YOUR title and YOUR data.
    Make it something you're proud of!
    """
    # ── Your final project data and logic ─────────────────────────────────
    # Write your full implementation here, using all your skills.
    # Start simple — get it working first, then make it more sophisticated.

    my_values = []   # at least 3 meaningful numbers from your data
    my_labels = []   # descriptive label for each number

    return {
        # Give your final widget a great title — something that describes
        # YOUR data and makes the dashboard feel personal.
        "title": "Final Project Integration",

        "values": my_values,
        "labels": my_labels,
    }

