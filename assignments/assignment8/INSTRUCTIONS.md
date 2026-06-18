# assignment8: Advanced OOP

## Starter workflow (GUI-only)
- Edit only `student_code.py` in Codespaces.
- Run `test_assignment.py` from the **Testing panel**.
- Commit and sync from the **Source Control panel**.
- Open and merge your pull request on the GitHub website.
- Do not use terminal commands.

## Learning target
Write `SavingsAccount(Account)` that inherits from the provided `Account` class, overrides `kind()` to return `"savings"`, and adds `add_interest(rate)`. Then fill `get_dashboard_payload()` with non-trivial values. The widget unlocks when every test in `test_assignment.py` passes.

## Worked example (different data)
`SavingsAccount(100).kind()` → `"savings"`; after `add_interest(0.10)`, the balance becomes `110`.
