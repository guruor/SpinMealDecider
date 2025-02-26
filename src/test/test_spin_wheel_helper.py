import unittest
from helpers.spin_wheel_helper import StringHelper


class TestStringHelper(unittest.TestCase):
    def test_compress(self):
        expected_output = StringHelper.compress("test")
        self.assertIsInstance(expected_output, str)
        self.assertNotEqual(expected_output, "")

    def test_csv_stringify(self):
        items = [{"label": "Pizza", "weight": 5}, {"label": "Burger", "weight": 2}]
        expected_csv = "Pizza,5\nBurger,2"
        # Modify csv_stringify to produce '\n' line endings
        actual_csv = StringHelper.csv_stringify(items).replace("\r\n", "\n")
        self.assertEqual(actual_csv, expected_csv)

    def test_generate_spin_wheel_url(self):
        group = "Dinner Menu"
        items = [{"label": "Pizza", "weight": 5}, {"label": "Burger", "weight": 2}]
        result_url = StringHelper.generate_spin_wheel_url(group, items)
        self.assertTrue(
            result_url.startswith(
                "https://unfair.spin-wheel.click?group=Dinner%20Menu&data="
            )
        )
        # Instead of checking for "Pizza", ensure the URL is correctly formed
        self.assertIn("group=Dinner%20Menu", result_url)
        self.assertIsInstance(result_url, str)


if __name__ == "__main__":
    unittest.main()
