# assignment6: File I/O, Error Handling

## Starter workflow (GUI-only)
- Edit only `student_code.py` in Codespaces.
- Run `test_assignment.py` from the **Testing panel**.
- Commit and sync from the **Source Control panel**.
- Open and merge your pull request on the GitHub website.
- Do not use terminal commands.

## Learning target
Finish `parse_numbers(lines)` so it converts text lines to ints and uses try / except to skip the ones that aren't numbers, then fill `get_dashboard_payload()` with non-trivial values. The widget unlocks when every test in `test_assignment.py` passes.

## Worked example (different data)
`parse_numbers(["10", "x", "20"])` → `[10, 20]` (the `"x"` line is skipped).
