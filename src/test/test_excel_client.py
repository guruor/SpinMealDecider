import unittest
from unittest.mock import patch, Mock
import pandas as pd
from helpers.excel_client import ExcelClient
from io import BytesIO


class TestExcelClient(unittest.TestCase):
    @patch("helpers.excel_client.requests.get")
    def test_download_excel_from_url(self, mock_get):
        # Create a simple Excel file in memory for testing
        test_data = pd.DataFrame({"label": [1, 2], "weight": [3, 4]})
        buffer = BytesIO()
        with pd.ExcelWriter(buffer) as writer:
            test_data.to_excel(writer, index=False, sheet_name="Dinner")

        buffer.seek(0)

        mock_response = Mock()
        mock_response.content = buffer.read()
        mock_get.return_value = mock_response

        excel_url = "https://docs.google.com/spreadsheets/d/1iPDiYfyYSbSvF8-asyWzj0Y-USQuPoa1PdjFIYevwCM/export?format=xlsx"
        excel_file = ExcelClient.download_excel_from_url(excel_url)

        # Read the 'Dinner' into a DataFrame and verify
        df = pd.read_excel(excel_file, sheet_name="Dinner")
        pd.testing.assert_frame_equal(df, test_data)
        mock_get.assert_called_once_with(excel_url)


if __name__ == "__main__":
    unittest.main()
