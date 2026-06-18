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

    def test_mean_and_modularization(self):
        self.assertEqual(self.module.mean([2, 4, 6]), 4)
        self.assertEqual(self.module.mean([]), 0)
        self.assertEqual(self.module.below_average_count([1, 2, 3, 4]), 2)
        self.assertEqual(self.module.below_average_count([5, 5, 5]), 0)

    def test_price_total(self):
        self.assertEqual(self.module.price_total({"a": 2, "b": 3}), 5)
        self.assertEqual(self.module.price_total({}), 0)

    def test_parse_floats(self):
        self.assertEqual(self.module.parse_floats(["1.5", "oops", "2.0"]), [1.5, 2.0])
        self.assertEqual(self.module.parse_floats([]), [])

    def test_tally_class(self):
        tally = self.module.Tally()
        self.assertEqual(tally.count, 0)
        tally.bump()
        tally.bump()
        self.assertEqual(tally.count, 2)

    def test_resettable_tally_inheritance(self):
        self.assertTrue(issubclass(self.module.ResettableTally, self.module.Tally))
        tally = self.module.ResettableTally()
        tally.bump()                 # inherited from Tally
        self.assertEqual(tally.count, 1)
        tally.reset()                # added by ResettableTally
        self.assertEqual(tally.count, 0)

    def test_cube_lambda(self):
        self.assertEqual(self.module.cube(2), 8)
        self.assertEqual(self.module.cube(3), 27)

    def test_base_points_decorator(self):
        self.assertEqual(self.module.base_points(3), 35)   # 3*10 + 5 bonus
        self.assertEqual(self.module.base_points(0), 5)

    def test_count_failures_debugged(self):
        self.assertEqual(self.module.count_failures([True, False, True]), 1)
        self.assertEqual(self.module.count_failures([False, False]), 2)
        self.assertEqual(self.module.count_failures([]), 0)

    def test_payload_is_valid(self):
        assert_valid_payload(self, self.module.get_dashboard_payload())


if __name__ == "__main__":
    unittest.main()
