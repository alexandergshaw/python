# =============================================================================
#  ASSIGNMENT 9 — Advanced Python: Lambdas and Decorators
#  File: assignments/assignment9/student_code.py
# =============================================================================
#
#  WHAT YOU'RE LEARNING THIS WEEK
#  ─────────────────────────────────────────────────────────────────────────────
#  LAMBDA FUNCTIONS — A short, anonymous (nameless) function written in one
#  line.  Great for simple operations you only need once.
#
#  Syntax:
#      lambda parameters: expression
#
#  Examples:
#      double  = lambda x: x * 2
#      add     = lambda x, y: x + y
#      is_even = lambda n: n % 2 == 0
#
#      print(double(5))       # 10
#      print(add(3, 7))       # 10
#      print(is_even(4))      # True
#
#  Lambdas are especially useful as arguments to built-in functions:
#
#      numbers = [5, 2, 8, 1, 9, 3]
#      sorted_numbers = sorted(numbers)                     # [1, 2, 3, 5, 8, 9]
#
#      words = ["banana", "apple", "cherry", "date"]
#      sorted_by_length = sorted(words, key=lambda w: len(w))
#      # ["date", "apple", "banana", "cherry"]
#
#      data = [{"name": "Ana", "score": 92}, {"name": "Bo", "score": 85}]
#      sorted_data = sorted(data, key=lambda d: d["score"], reverse=True)
#      # sorted highest → lowest score
#
#  ── map() and filter() ───────────────────────────────────────────────────────
#  map(function, iterable) — applies a function to every item:
#      numbers  = [1, 2, 3, 4, 5]
#      doubled  = list(map(lambda x: x * 2, numbers))   # [2, 4, 6, 8, 10]
#
#  filter(function, iterable) — keeps only items where function returns True:
#      evens = list(filter(lambda x: x % 2 == 0, numbers))  # [2, 4]
#
#  DECORATORS — A function that WRAPS another function to add extra behavior,
#  without changing the original function's code.
#
#  How they work conceptually:
#      def my_decorator(func):
#          def wrapper(*args, **kwargs):
#              print("Before the function runs")
#              result = func(*args, **kwargs)            # call the real function
#              print("After the function runs")
#              return result
#          return wrapper                                 # return the wrapper
#
#      @my_decorator                  # this line applies the decorator
#      def say_hello():
#          print("Hello!")
#
#      say_hello()
#      # Output:
#      #   Before the function runs
#      #   Hello!
#      #   After the function runs
#
#  Common real-world decorators:
#      @staticmethod   — you already saw this in Assignment 8
#      @classmethod    — same
#      @property       — turn a method into a read-only attribute
#
#  YOUR TASK: Build a "transform pipeline" widget.
#  ─────────────────────────────────────────────────────────────────────────────
#  Start with a list of raw numbers.  Use lambdas + map/filter to transform
#  them (e.g., double them, keep only evens, square them).  Return the
#  original values and the transformed values for comparison.
#
#  WORKED EXAMPLE (use different data!):
#      values = [3, 6, 9, 12, 15]
#      doubled  = list(map(lambda x: x * 2, values))
#      evens    = list(filter(lambda x: x % 2 == 0, doubled))
#      → values: [sum(values), sum(doubled), sum(evens)]
#      → labels: ["Raw Total", "Doubled Total", "Even Doubled Total"]
# =============================================================================

"""Starter code for assignment9: Advanced Python: Lambdas/Decorators."""

# ── Identity variables ────────────────────────────────────────────────────────
student_name = "Your Name"
assignment_label = "assignment9"


# =============================================================================
#  OPTIONALLY DEFINE A DECORATOR HERE
#  ─────────────────────────────────────────────────────────────────────────────
#  You can define a decorator and apply it to a helper function to practice
#  the concept.  It doesn't need to change the output data — it could just
#  print a log message.
#
#  Example:
#      def log_call(func):
#          def wrapper(*args, **kwargs):
#              print(f"Calling {func.__name__}...")
#              return func(*args, **kwargs)
#          return wrapper
#
#      @log_call
#      def transform(values):
#          return list(map(lambda x: x ** 2, values))
# =============================================================================


# ── Dashboard function ────────────────────────────────────────────────────────
def get_dashboard_payload():
    """Return dashboard-ready data for the Assignment 9 widget.

    Your job:
      1. Define a list of raw numbers.
      2. Use at least ONE lambda with map() or filter() to transform them.
      3. Optionally apply a decorator to a helper function.
      4. Return comparison stats (raw vs. transformed) as values and labels.
    """
    # ── Raw input data ─────────────────────────────────────────────────────
    # Replace with your own numbers.
    # raw_values = [3, 6, 9, 12, 15]

    # ── Apply lambda transformations ───────────────────────────────────────
    # doubled  = list(map(lambda x: x * 2,      raw_values))
    # squared  = list(map(lambda x: x ** 2,     raw_values))
    # filtered = list(filter(lambda x: x > 10,  raw_values))

    # ── Compute summary stats ──────────────────────────────────────────────
    # raw_sum  = sum(raw_values)
    # dbl_sum  = sum(doubled)
    # sq_sum   = sum(squared)

    my_values = []
    my_labels = []

    return {
        "title": "Advanced Python: Lambdas/Decorators",
        "values": my_values,
        "labels": my_labels,
    }

