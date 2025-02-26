import pandas as pd

from constants import SHEET_COLUMNS


class MealSheetParser:
    @staticmethod
    def parse_meals(excel_file, meal_sheets):
        """
        Parses the specified meal sheets from an Excel file into a dictionary.

        :param excel_file: A pandas ExcelFile object containing the meal sheets.
        :param meal_sheets: A list of sheet names to be processed.
        :return: Dictionary containing meals with list of items and weights.
        """
        meal_items = {}

        for meal in meal_sheets:
            if meal in excel_file.sheet_names:
                df = pd.read_excel(excel_file, sheet_name=meal)
                df.fillna("", inplace=True)  # Fill NaNs with empty strings (if any)
                items = df.to_dict(orient="records")
                items_with_weights = [
                    {
                        SHEET_COLUMNS[0]: item[SHEET_COLUMNS[0]],
                        SHEET_COLUMNS[1]: item.get(SHEET_COLUMNS[1], 1),
                    }
                    for item in items
                ]
                meal_items[meal] = items_with_weights

        return meal_items
