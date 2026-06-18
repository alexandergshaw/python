# assignment7: OOP: Classes

## Starter workflow (GUI-only)
- Edit only `student_code.py` in Codespaces.
- Run `test_assignment.py` from the **Testing panel**.
- Commit and sync from the **Source Control panel**.
- Open and merge your pull request on the GitHub website.
- Do not use terminal commands.

## Learning target
Finish the `Wallet` class (`__init__`, `deposit`, `can_afford`), then fill `get_dashboard_payload()` with non-trivial values. The widget unlocks when every test in `test_assignment.py` passes.

## Worked example (different data)
A new `Wallet("Sam")` starts with `balance` `0`; after `deposit(50)`, `can_afford(40)` → `True` and `can_afford(60)` → `False`.
