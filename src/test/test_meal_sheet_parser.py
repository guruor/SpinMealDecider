import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
from constants import SHEET_COLUMNS
from helpers.meal_sheet_parser import MealSheetParser


class TestMealSheetParser(unittest.TestCase):
    @patch("helpers.meal_sheet_parser.pd.read_excel")
    def test_parse_meals(self, mock_read_excel):
        # Create mock data frames for each required sheet
        breakfast_data = pd.DataFrame(
            {SHEET_COLUMNS[0]: ["Eggs", "Toast"], SHEET_COLUMNS[1]: [2, 1]}
        )

        lunch_data = pd.DataFrame(
            {SHEET_COLUMNS[0]: ["Sandwich", "Salad"], SHEET_COLUMNS[1]: [1, 1]}
        )

        # Assign return values to the mock
        mock_read_excel.side_effect = [breakfast_data, lunch_data]

        # Simulate the Excel file and meal sheets
        mock_excel_file = MagicMock()
        mock_excel_file.sheet_names = ["Breakfast", "Lunch"]

        meals = ["Breakfast", "Lunch"]

        expected_meal_items = {
            "Breakfast": [
                {"label": "Eggs", "weight": 2},
                {"label": "Toast", "weight": 1},
            ],
            "Lunch": [
                {"label": "Sandwich", "weight": 1},
                {"label": "Salad", "weight": 1},
            ],
        }

        # Parse the meals
        meal_items = MealSheetParser.parse_meals(mock_excel_file, meals)

        # Assertions
        self.assertEqual(meal_items, expected_meal_items)
        self.assertEqual(mock_read_excel.call_count, len(meals))
        mock_read_excel.assert_any_call(mock_excel_file, sheet_name="Breakfast")
        mock_read_excel.assert_any_call(mock_excel_file, sheet_name="Lunch")


if __name__ == "__main__":
    unittest.main()
