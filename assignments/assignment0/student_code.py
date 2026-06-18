# =============================================================================
#  ASSIGNMENT 0 — Setup, Git, and Vercel
#  File: assignments/assignment0/student_code.py
# =============================================================================
#
#  HOW THIS WHOLE COURSE WORKS
#  ---------------------------------------------------------------------------
#  Every assignment has exactly ONE file you edit: this one, student_code.py.
#  Each assignment folder also has a test_assignment.py file (you do NOT edit
#  that one).  Those tests are the checklist your code has to pass.  When all
#  the tests for an assignment pass, that assignment "unlocks" and a widget
#  appears on the live dashboard.  Think of a widget as proof your code works.
#
#  WHAT YOU DO FOR ASSIGNMENT 0
#  ---------------------------------------------------------------------------
#  This first assignment is about getting set up, not about hard coding.  You
#  only need to do two small things:
#
#    1. Put your real name in `student_name` below.
#    2. Fill in `get_dashboard_payload()` with a little bit of made-up data.
#
#  WHAT IS A VARIABLE?
#  ---------------------------------------------------------------------------
#  A variable is a labelled box that holds a value.  You make one with `=`:
#
#      student_name = "Maya Chen"     # text (a "string") goes in quotes
#      lucky_number = 7               # a whole number (an "int")
#
#  WHAT IS A DICTIONARY?
#  ---------------------------------------------------------------------------
#  A dictionary holds named pieces of data inside curly braces { }.  Each
#  entry is a name (a "key") followed by a colon and a value:
#
#      pet = {"name": "Rex", "legs": 4}
#
#  The dashboard expects a dictionary with exactly these three keys:
#      "title"   a short heading for your widget (a non-empty string)
#      "values"  a list of numbers, e.g. [10, 25, 40]
#      "labels"  a list of short text labels, one per number
#
#  RULES FOR YOUR DATA (the tests check these, so read them!)
#  ---------------------------------------------------------------------------
#    * "values" and "labels" must EACH have at least 3 items.
#    * "values" and "labels" must have the SAME number of items.
#    * At least 2 of your numbers must be DIFFERENT from each other.
#    * Every label must be a non-empty piece of text.
#
#  WORKED EXAMPLE (make up your OWN data, don't copy this)
#  ---------------------------------------------------------------------------
#      title  = "Favorite Colors Survey"
#      labels = ["Red", "Blue", "Green", "Yellow"]
#      values = [12, 34, 8, 20]
# =============================================================================

"""Starter code for assignment0: Setup, Git, Vercel."""

# Change "Your Name" to your real name (keep the quotes).
student_name = "Your Name"

# Leave this exactly as-is -- it tells the dashboard which slot to fill.
assignment_label = "assignment0"


def get_dashboard_payload():
    """Return the data the dashboard widget will display.

    Replace the empty lists below with your own labels and numbers.  Pick
    anything you like: quiz scores, hours of sleep, songs played, etc.
    """
    return {
        # A short heading describing your data.
        "title": "My First Widget",

        # TODO: put at least 3 numbers here, e.g. [10, 25, 40]
        "values": [],

        # TODO: put one short label per number here, e.g. ["Mon", "Tue", "Wed"]
        "labels": [],
    }
