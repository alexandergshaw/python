# =============================================================================
#  ASSIGNMENT 7 — Object-Oriented Programming: Classes
#  File: assignments/assignment7/student_code.py
# =============================================================================
#
#  WHAT YOU'RE LEARNING THIS WEEK
#  ---------------------------------------------------------------------------
#  A CLASS is a blueprint for making objects that bundle data + behavior.
#
#      class Dog:
#          def __init__(self, name):   # runs when you create a Dog
#              self.name = name         # store data ON the object
#
#          def bark(self):              # a method = a function on the object
#              return self.name + " says woof"
#
#      rex = Dog("Rex")                 # make an instance
#      rex.name                         # "Rex"        (an attribute)
#      rex.bark()                       # "Rex says woof" (a method call)
#
#  KEY WORDS
#    __init__   the "constructor" -- sets up a new object's starting data
#    self       the object itself; every method's first parameter
#    attribute  a value stored on the object (self.name)
#    method     a function defined inside the class
#
#  YOUR TASK (two small things)
#  ---------------------------------------------------------------------------
#  1. Finish the `Wallet` class below.  It needs:
#        * __init__(self, owner): store the owner's name, and start `balance`
#          at 0.
#        * deposit(self, amount): add `amount` to the balance.
#        * can_afford(self, price): return True if the balance is at least the
#          price, otherwise False.
#
#  2. Fill in `get_dashboard_payload()` with at least 3 of your own numbers.
#
#  WORKED EXAMPLE (use different data, don't copy it)
#  ---------------------------------------------------------------------------
#      title  = "Account Activity"
#      labels = ["Deposit 1", "Deposit 2", "Deposit 3"]
#      values = [50, 20, 35]
# =============================================================================

"""Starter code for assignment7: OOP: Classes."""

# Change this to your real name.
student_name = "Your Name"

# Leave this exactly as-is.
assignment_label = "assignment7"


class Wallet:
    """A simple wallet that tracks an owner and a money balance."""

    def __init__(self, owner):
        """Set up a new wallet.

        Store the `owner` name on the object, and start `balance` at 0.
        (Hint: self.owner = owner, and set self.balance to 0.)
        """
        # TODO: save self.owner and set self.balance to 0.
        pass

    def deposit(self, amount):
        """Add `amount` to this wallet's balance."""
        # TODO: increase self.balance by amount.
        pass

    def can_afford(self, price):
        """Return True if the balance is at least `price`, else False."""
        # TODO: return whether self.balance is >= price.
        pass


def get_dashboard_payload():
    """Return the data for your Assignment 7 widget.

    Put your own numbers in `values` and a matching label for each one in
    `labels`.  Keep at least 3 items in each list, with at least 2 of the
    numbers different from one another.
    """
    my_labels = []   # e.g. ["Deposit 1", "Deposit 2", "Deposit 3"]
    my_values = []   # e.g. [50, 20, 35]

    return {
        "title": "OOP: Classes",
        "values": my_values,
        "labels": my_labels,
    }
