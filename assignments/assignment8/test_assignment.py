import importlib.util
import pathlib
import unittest


def load_student_module():
    student_file = pathlib.Path(__file__).with_name("student_code.py")
    spec = importlib.util.spec_from_file_location("student_code", student_file)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def assert_valid_payload(tc, payload):
    """Shared check: the widget data must be present and non-trivial."""
    tc.assertIsInstance(payload, dict, "get_dashboard_payload() must return a dict")
    for key in ("title", "values", "labels"):
        tc.assertIn(key, payload, f"payload is missing the '{key}' key")

    title, values, labels = payload["title"], payload["values"], payload["labels"]
    tc.assertIsInstance(title, str)
    tc.assertTrue(title.strip(), "title must be a non-empty string")
    tc.assertIsInstance(values, list, "values must be a list")
    tc.assertIsInstance(labels, list, "labels must be a list")
    tc.assertGreaterEqual(len(values), 3, "values needs at least 3 numbers")
    tc.assertEqual(len(values), len(labels), "values and labels must be the same length")
    for value in values:
        tc.assertTrue(
            isinstance(value, (int, float)) and not isinstance(value, bool),
            "every item in values must be a number",
        )
    tc.assertGreaterEqual(len(set(values)), 2, "at least two values must be different")
    for label in labels:
        tc.assertTrue(
            isinstance(label, str) and label.strip(),
            "every label must be a non-empty string",
        )


class StudentCodeTests(unittest.TestCase):
    def setUp(self):
        self.module = load_student_module()

    def test_savings_inherits_from_account(self):
        self.assertTrue(issubclass(self.module.SavingsAccount, self.module.Account))

    def test_balance_is_inherited(self):
        # __init__ comes from Account, so this should set balance to 100.
        account = self.module.SavingsAccount(100)
        self.assertEqual(account.balance, 100)

    def test_kind_is_overridden(self):
        account = self.module.SavingsAccount(100)
        self.assertEqual(account.kind(), "savings")

    def test_add_interest(self):
        account = self.module.SavingsAccount(100)
        account.add_interest(0.10)
        self.assertAlmostEqual(account.balance, 110)
        account2 = self.module.SavingsAccount(200)
        account2.add_interest(0.05)
        self.assertAlmostEqual(account2.balance, 210)

    def test_payload_is_valid(self):
        assert_valid_payload(self, self.module.get_dashboard_payload())


if __name__ == "__main__":
    unittest.main()
