# =============================================================================
#  ASSIGNMENT 5 — Data Structures (Lists & Dictionaries)
#  File: assignments/assignment5/student_code.py
# =============================================================================
#
#  WHAT YOU'RE LEARNING THIS WEEK
#  ---------------------------------------------------------------------------
#  A DICTIONARY stores named pairs: each "key" maps to a "value".
#
#      cart = {"apples": 4, "milk": 1, "eggs": 12}
#
#      cart["apples"]          # 4        (look up a value by its key)
#      cart.keys()             # the names: apples, milk, eggs
#      cart.values()           # the numbers: 4, 1, 12
#
#  LOOPING OVER A DICTIONARY
#  ---------------------------------------------------------------------------
#      total = 0
#      for quantity in cart.values():   # quantity becomes 4, then 1, then 12
#          total = total + quantity
#      # total is now 17
#
#  HANDY: sorted(["banana", "apple"]) returns a NEW list in alphabetical order:
#  ["apple", "banana"].  You can pass it the keys of a dictionary.
#
#  YOUR TASK (three small things)
#  ---------------------------------------------------------------------------
#  1. Finish `total_items(cart)` -- add up all the quantities (the values) in
#     the dictionary and return the total.
#
#  2. Finish `item_names(cart)` -- return a list of the dictionary's keys,
#     sorted in alphabetical order.
#
#  3. Fill in `get_dashboard_payload()` with at least 3 of your own numbers.
#
#  WORKED EXAMPLE (use different data, don't copy it)
#  ---------------------------------------------------------------------------
#      title  = "My Grocery Cart"
#      labels = ["Apples", "Milk", "Eggs"]
#      values = [4, 1, 12]
# =============================================================================

"""Starter code for assignment5: Data Structures."""

# Change this to your real name.
student_name = "Alex Shaw"

# Leave this exactly as-is.
assignment_label = "assignment5"


def total_items(cart):
    """Add up all the quantities in a cart dictionary and return the total.

    `cart` maps item names to numbers, e.g. {"apples": 4, "milk": 1}.
    Add up the VALUES (the numbers) and return the total.  An empty cart
    should return 0.

    Examples (these are what the tests expect):
        total_items({"apples": 2, "milk": 3})  ->  5
        total_items({})                         ->  0
    """
    return sum(cart.values())


def item_names(cart):
    """Return the cart's item names (its keys) in alphabetical order.

    Examples (these are what the tests expect):
        item_names({"milk": 1, "apples": 2})  ->  ["apples", "milk"]
        item_names({})                          ->  []
    """
    return sorted(cart.keys())


def get_dashboard_payload():
    """Return the data for your Assignment 5 widget.

    Put your own numbers in `values` and a matching label for each one in
    `labels`.  Keep at least 3 items in each list, with at least 2 of the
    numbers different from one another.
    """
    my_labels = ["Apples", "Milk", "Eggs"]
    my_values = [4, 1, 12]

    return {
        "title": "Data Structures",
        "values": my_values,
        "labels": my_labels,
    }
