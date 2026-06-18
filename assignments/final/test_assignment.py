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

    def test_grade_label_branching(self):
        self.assertEqual(self.module.grade_label(95), "A")
        self.assertEqual(self.module.grade_label(85), "B")
        self.assertEqual(self.module.grade_label(72), "C")
        self.assertEqual(self.module.grade_label(40), "F")

    def test_count_active_days_loop(self):
        self.assertEqual(self.module.count_active_days([1000, 5000, 8000], 4000), 2)
        self.assertEqual(self.module.count_active_days([5, 6, 7], 5), 3)

    def test_average_function(self):
        self.assertEqual(self.module.average([2, 4, 6]), 4)
        self.assertEqual(self.module.average([]), 0)

    def test_total_items_data_structure(self):
        self.assertEqual(self.module.total_items({"a": 2, "b": 3}), 5)
        self.assertEqual(self.module.total_items({}), 0)

    def test_parse_numbers_error_handling(self):
        self.assertEqual(self.module.parse_numbers(["10", "x", "20"]), [10, 20])
        self.assertEqual(self.module.parse_numbers([]), [])

    def test_wallet_class(self):
        wallet = self.module.Wallet("Sam")
        self.assertEqual(wallet.owner, "Sam")
        self.assertEqual(wallet.balance, 0)
        wallet.deposit(30)
        self.assertEqual(wallet.balance, 30)

    def test_rewards_wallet_inheritance(self):
        self.assertTrue(issubclass(self.module.RewardsWallet, self.module.Wallet))
        wallet = self.module.RewardsWallet("Sam")
        wallet.deposit(50)               # inherited from Wallet
        self.assertEqual(wallet.balance, 50)
        self.assertEqual(wallet.reward_points(), 5)

    def test_square_lambda(self):
        self.assertEqual(self.module.square(4), 16)
        self.assertEqual(self.module.square(6), 36)

    def test_base_points_decorator(self):
        self.assertEqual(self.module.base_points(3), 35)   # 3*10 + 5 bonus
        self.assertEqual(self.module.base_points(0), 5)

    def test_payload_is_valid(self):
        assert_valid_payload(self, self.module.get_dashboard_payload())


if __name__ == "__main__":
    unittest.main()
