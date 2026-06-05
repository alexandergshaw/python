# =============================================================================
#  ASSIGNMENT 6 — File I/O and Error Handling
#  File: assignments/assignment6/student_code.py
# =============================================================================
#
#  WHAT YOU'RE LEARNING THIS WEEK
#  ─────────────────────────────────────────────────────────────────────────────
#  FILE I/O (Input / Output)
#  ─────────────────────────────────────────────────────────────────────────────
#  "File I/O" means reading data FROM a file or writing data TO a file.
#  Python makes this easy with the built-in open() function.
#
#  ── Reading a file ───────────────────────────────────────────────────────────
#      with open("myfile.txt", "r") as f:   # "r" = read mode
#          contents = f.read()               # read everything as one string
#
#      with open("myfile.txt", "r") as f:
#          lines = f.readlines()             # read as a list of lines
#
#  The `with` keyword automatically closes the file when the block ends.
#  Always use `with open(...)` — never forget to close files!
#
#  ── Writing a file ───────────────────────────────────────────────────────────
#      with open("output.txt", "w") as f:   # "w" = write mode (overwrites)
#          f.write("Hello, file!\n")         # \n is a newline character
#
#      with open("output.txt", "a") as f:   # "a" = append mode (adds to end)
#          f.write("Another line\n")
#
#  ── Parsing CSV data ─────────────────────────────────────────────────────────
#  CSV (Comma-Separated Values) is the most common data format.  Each line is
#  a row; values within a row are separated by commas.
#
#      csv_text = "name,score\nAna,92\nBo,85\nCara,78"
#
#      lines = csv_text.strip().split("\n")   # split into rows
#      header = lines[0].split(",")           # ["name", "score"]
#      for line in lines[1:]:                 # skip the header row
#          parts = line.split(",")            # ["Ana", "92"]
#          name  = parts[0]
#          score = int(parts[1])              # convert string → int
#
#  ERROR HANDLING (try / except)
#  ─────────────────────────────────────────────────────────────────────────────
#  When something can go wrong (file not found, bad data format, division by
#  zero), Python raises an EXCEPTION.  If you don't handle it, your program
#  crashes.  Use try/except to catch errors and respond gracefully.
#
#      try:
#          result = 10 / 0              # ← this will raise ZeroDivisionError
#      except ZeroDivisionError:
#          print("Can't divide by zero!")
#          result = 0
#
#  You can catch multiple error types:
#      try:
#          value = int("not a number")
#      except ValueError as e:
#          print("Conversion failed:", e)
#      except Exception as e:
#          print("Unexpected error:", e)
#
#  Always use specific exception types when you know what might go wrong.
#  Using bare `except:` (no type) catches EVERYTHING including system exits —
#  usually not what you want.
#
#  YOUR TASK: Build a "CSV guardrails" widget.
#  ─────────────────────────────────────────────────────────────────────────────
#  IMPORTANT: Because this code runs in the BROWSER (no actual file system
#  access), simulate file I/O by storing your CSV data as a Python string and
#  parsing it exactly the way you would parse a real file.  This lets you
#  practice the same string-manipulation skills.
#
#  WORKED EXAMPLE (use different data!):
#      lines = ["name,amount", "Ana,23", "Bo,19", "Cara,31"]
#      → parse each line, convert amounts to int
#      → compute total, average, max
#      → values: [73, 24.33, 31]
#      → labels: ["Total", "Average", "Max"]
# =============================================================================

"""Starter code for assignment6: File I/O, Error Handling."""

# ── Identity variables ────────────────────────────────────────────────────────
student_name = "Your Name"
assignment_label = "assignment6"


# ── Dashboard function ────────────────────────────────────────────────────────
def get_dashboard_payload():
    """Return dashboard-ready data for the Assignment 6 widget.

    Your job:
      1. Define a multi-line CSV string (simulating a file's contents).
      2. Parse it line by line, extracting labels and numeric values.
      3. Wrap the parsing in try/except to handle bad rows gracefully
         (e.g., a row where the number column contains "N/A").
      4. Compute at least 3 summary stats from the parsed data.
      5. Return them in the payload.

    Remember: in a real program you'd use open() to read from disk.
    Here, store your CSV data in a string variable and call .split("\\n")
    to get the lines — the logic is identical to reading a real file.
    """
    # ── Simulate file contents as a string ────────────────────────────────
    # Replace with your own CSV data.  Use commas to separate columns.
    # csv_data = \"\"\"name,score
    # Ana,92
    # Bo,85
    # Cara,78
    # Dan,91
    # Eve,67\"\"\"

    # ── Parse the CSV ─────────────────────────────────────────────────────
    # lines  = csv_data.strip().split("\\n")
    # header = lines[0].split(",")        # skip the header row
    # names  = []
    # scores = []
    # for line in lines[1:]:
    #     try:
    #         parts = line.split(",")
    #         names.append(parts[0].strip())
    #         scores.append(float(parts[1].strip()))
    #     except (ValueError, IndexError) as e:
    #         print(f"Skipping bad row '{line}': {e}")

    # ── Compute summary statistics ─────────────────────────────────────────
    # total   = sum(scores)
    # average = total / len(scores) if scores else 0
    # highest = max(scores) if scores else 0

    my_values = []
    my_labels = []

    return {
        "title": "File I/O, Error Handling",
        "values": my_values,
        "labels": my_labels,
    }

