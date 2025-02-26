import os

from helpers.excel_client import ExcelClient
from helpers.dub_co_client import DubCoClient
from helpers.spin_wheel_helper import StringHelper
from helpers.meal_sheet_parser import MealSheetParser
from constants import MEALS


def main():
    excel_url = os.getenv("FOOD_MENU_SHEET_PUBLIC_URL")

    client = ExcelClient()
    excel_file = client.download_excel_from_url(excel_url)

    parser = MealSheetParser()
    meal_items = parser.parse_meals(excel_file, MEALS)

    d_client = DubCoClient(api_key=os.getenv("DUB_API_KEY"))
    for meal, items in meal_items.items():
        link_id = os.getenv(f"{meal.upper()}_LINK_ID")
        url = StringHelper.generate_spin_wheel_url(group=meal, items=items)
        print(f"\n{meal} Link ID: {link_id}")

        link_info = d_client.get_link_info(link_id)
        current_url = link_info["url"]
        print(f"Current URL: {current_url}")
        print(f"New URL: {url}")
        # Update the link only when it is changed
        if current_url != url:
            print(f"Updating URL: {url}")
            link_info = d_client.update_link_url(link_id, url)
        else:
            print("Skipping URL update, no change needed")


if __name__ == "__main__":
    main()
