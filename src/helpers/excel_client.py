import pandas as pd
import requests
from io import BytesIO


class ExcelClient:
    @staticmethod
    def download_excel_from_url(excel_url):
        """
        Downloads an Excel file from the specified URL and loads it into a pandas ExcelFile object.

        :param excel_url: The URL pointing to the Excel file.
        :return: A pandas ExcelFile object containing the downloaded Excel content.
        """
        response = requests.get(excel_url)
        response.raise_for_status()  # Raises an HTTPError for bad responses

        # Load the Excel file into memory
        excel_file = pd.ExcelFile(BytesIO(response.content))
        return excel_file
