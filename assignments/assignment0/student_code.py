# =============================================================================
#  ASSIGNMENT 0 — Setup, Git, and Vercel
#  File: assignments/assignment0/student_code.py
# =============================================================================
#
#  HOW THIS WHOLE COURSE WORKS
#  ─────────────────────────────────────────────────────────────────────────────
#  Every assignment in this course has exactly ONE file you edit: this one,
#  student_code.py.  When you push your changes and open the live Vercel URL,
#  the dashboard automatically runs your Python code in the browser and checks
#  whether `get_dashboard_payload()` returns real data.  If it does, a widget
#  appears on the dashboard showing your results.  Think of each widget as a
#  "proof of work" — it only appears when your code actually runs correctly.
#
#  WHAT YOU EDIT IN THIS FILE
#  ─────────────────────────────────────────────────────────────────────────────
#  1. `student_name`  — Change "Your Name" to YOUR actual name.
#                       This is just a Python string (text surrounded by
#                       double-quotes).  Example: student_name = "Maya Chen"
#
#  2. `assignment_label` — DO NOT change this.  The dashboard uses it to match
#                          your code to the right widget slot.  Leave it as-is.
#
#  3. `get_dashboard_payload()` — This is a Python *function* (a reusable block
#                                 of code that can be "called" to produce a
#                                 result).  You will add your own code inside
#                                 it for every assignment.  For assignment 0,
#                                 just fill in the lists with a few values so
#                                 the widget unlocks.
#
#  WHAT IS A PYTHON FUNCTION?
#  ─────────────────────────────────────────────────────────────────────────────
#  A function is defined with the `def` keyword, followed by the function name,
#  parentheses, and a colon.  The indented block underneath is the function
#  *body* — the code that runs when you call the function.
#
#      def say_hello():        # ← defines a function called say_hello
#          print("Hello!")     # ← this runs when say_hello() is called
#
#  This function already exists for you below.  You only need to fill in the
#  return value (what it hands back to the dashboard).
#
#  WHAT IS A DICTIONARY?
#  ─────────────────────────────────────────────────────────────────────────────
#  A dictionary (dict) is a collection of key–value pairs, written with curly
#  braces {}.  Each key is a name (a string), and each value is the data for
#  that name.
#
#      my_dict = {
#          "color": "blue",    # key "color" maps to the value "blue"
#          "count": 3,         # key "count" maps to the integer 3
#      }
#
#  The dashboard expects a dictionary with three specific keys:
#      "title"  — a short text label shown at the top of your widget
#      "values" — a Python list of numbers  (e.g., [10, 20, 30])
#      "labels" — a Python list of strings  (e.g., ["Mon", "Tue", "Wed"])
#
#  RULES FOR YOUR DATA (READ THESE OR YOUR WIDGET WON'T UNLOCK!)
#  ─────────────────────────────────────────────────────────────────────────────
#  • `values` and `labels` must each have AT LEAST 3 items.
#  • `values` and `labels` must have THE SAME number of items.
#  • At least 2 of the numbers in `values` must be DIFFERENT from each other
#    (i.e., not all the same number — that would be trivial).
#  • Every label must be a non-empty string (not "").
#  • Every value must be a real number (integers like 5 or decimals like 3.14).
#
#  WORKED EXAMPLE (don't copy this — make up your own data!)
#  ─────────────────────────────────────────────────────────────────────────────
#      "title":  "Favorite Colors Survey"
#      "labels": ["Red", "Blue", "Green", "Yellow"]
#      "values": [12, 34, 8, 20]
#
#  YOUR TURN: Replace the empty lists below with your own data.
#  It can be anything — favorite songs, steps walked each day, quiz scores, etc.
# =============================================================================

"""Starter code for assignment0: Setup, Git, Vercel."""

# ── Identity variables ────────────────────────────────────────────────────────
# Change "Your Name" to your real name.  The testing panel will check this.
student_name = "Your Name"

# DO NOT change assignment_label — it tells the dashboard which slot to fill.
assignment_label = "assignment0"


# ── Dashboard function ────────────────────────────────────────────────────────
def get_dashboard_payload():
    """Return dashboard-ready data for the Assignment 0 widget.

    This function MUST:
      - Stay named exactly `get_dashboard_payload` (no spaces, no capitals).
      - Return a dictionary with the keys "title", "values", and "labels".
      - Have at least 3 items in both lists, all different enough to be
        non-trivial (at least 2 distinct numbers in `values`).

    Steps for this assignment:
      1. Change student_name above to your name.
      2. Replace the empty lists with your own labels and values.
      3. Run the tests (Testing panel in Codespaces) — they should go green.
      4. Commit and push from the Source Control panel.
      5. Open a pull request on GitHub and merge it.
    """
    return {
        # The title appears as the widget heading on the live dashboard.
        # Make it descriptive — something that describes what your data is about.
        "title": "Setup, Git, Vercel",

        # Put at least 3 numbers here.  Use a comma between each one.
        # Example: [10, 25, 40, 15]
        "values": [],

        # Put at least 3 short text labels here — one label per number above.
        # The order matters: labels[0] goes with values[0], and so on.
        # Example: ["Week 1", "Week 2", "Week 3", "Week 4"]
        "labels": [],
    }

