# review2: Review: OOP/Advanced

## Starter workflow (GUI-only)
- Edit only `student_code.py` in Codespaces.
- Run `test_assignment.py` from the **Testing panel**.
- Commit and sync from the **Source Control panel**.
- Open and merge your pull request on the GitHub website.
- Do not use terminal commands.

## Learning target
Reviews everything from assignments 4–10 with one small task each: `average` + `above_average_count` (functions), `total_items` (dict), `parse_numbers` (try/except), `Counter` + `ResettableCounter` (classes + inheritance), the `square` lambda, `base_points` with `@add_bonus` (decorators), and fixing the bug in `count_passes` (debugging). Then fill `get_dashboard_payload()` with non-trivial values. The widget unlocks when every test in `test_assignment.py` passes.

## Worked example (different data)
`above_average_count([1, 2, 3, 4])` → `2`; a `ResettableCounter` after `add(4)` then `reset()` has `count` `0`.
