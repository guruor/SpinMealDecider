import zlib
import base64
import csv
from io import StringIO

from constants import SHEET_COLUMNS


class StringHelper:
    base_url = "https://unfair.spin-wheel.click"

    @staticmethod
    def compress(input_str: str) -> str:
        compressed_data = zlib.compress(input_str.encode("utf-8"))
        base64_bytes = base64.b64encode(compressed_data)
        base64_string = base64_bytes.decode("utf-8")

        # Transform the base64 string to URL-safe
        return base64_string.replace("+", "-").replace("/", "_").rstrip("=")

    @staticmethod
    def csv_stringify(items: list) -> str:
        if not items or len(items) == 0:
            return ""

        output = StringIO()
        writer = csv.DictWriter(output, fieldnames=SHEET_COLUMNS, extrasaction="ignore")
        writer.writerows(items)

        return output.getvalue().strip()

    @staticmethod
    def generate_spin_wheel_url(group: str, items: list) -> str:
        csv_data = StringHelper.csv_stringify(items)
        compressed_data = StringHelper.compress(csv_data)
        return f"{StringHelper.base_url}?group={group.replace(' ', '%20')}&data={compressed_data}"
