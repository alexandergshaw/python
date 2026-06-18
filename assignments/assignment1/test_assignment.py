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

    def test_temperature_label_cold(self):
        self.assertEqual(self.module.temperature_label(45), "cold")
        self.assertEqual(self.module.temperature_label(59), "cold")

    def test_temperature_label_warm(self):
        # 60 is the lower edge of "warm"; 79 is the top of "warm".
        self.assertEqual(self.module.temperature_label(60), "warm")
        self.assertEqual(self.module.temperature_label(72), "warm")
        self.assertEqual(self.module.temperature_label(79), "warm")

    def test_temperature_label_hot(self):
        # 80 is the lower edge of "hot".
        self.assertEqual(self.module.temperature_label(80), "hot")
        self.assertEqual(self.module.temperature_label(95), "hot")

    def test_payload_is_valid(self):
        assert_valid_payload(self, self.module.get_dashboard_payload())


if __name__ == "__main__":
    unittest.main()
