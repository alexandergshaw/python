# assignment10: CI/CD, Debugging

## Starter workflow (GUI-only)
- Edit only `student_code.py` in Codespaces.
- Run `test_assignment.py` from the **Testing panel**.
- Commit and sync from the **Source Control panel**.
- Open and merge your pull request on the GitHub website.
- Do not use terminal commands.

## CI/CD setup checklist (Week 13)
1. Open your repository on GitHub.
2. Click the **Actions** tab.
3. Enable workflows if prompted.
4. Open your pull request and verify checks appear in the PR checks section.
5. If a check fails, click the failed check name to read the log output in GitHub.
6. Return to Codespaces, fix `student_code.py`, run tests again from the Testing panel, and push a new commit.
7. Confirm checks pass before merging.

## Learning target
Practice debugging by reading test/check output and updating `get_dashboard_payload()` with valid, non-trivial values.

## Worked example (different data)
Worked example data: ci_status = ["pass", "fail", "pass"], retry_counts = [0, 1, 0].
