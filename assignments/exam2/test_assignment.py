import importlib.util
import pathlib
import unittest


class StudentCodeContractTests(unittest.TestCase):
    def setUp(self):
        student_file = pathlib.Path(__file__).with_name("student_code.py")
        spec = importlib.util.spec_from_file_location("student_code", student_file)
        module = importlib.util.module_from_spec(spec)
        assert spec.loader is not None
        spec.loader.exec_module(module)
        self.module = module

    def test_get_dashboard_payload_exists(self):
        self.assertTrue(callable(getattr(self.module, "get_dashboard_payload", None)))

    def test_get_dashboard_payload_shape(self):
        payload = self.module.get_dashboard_payload()
        self.assertIsInstance(payload, dict)
        self.assertIn("title", payload)
        self.assertIn("values", payload)
        self.assertIn("labels", payload)


if __name__ == "__main__":
    unittest.main()
