import json
from typing import Dict
from dub import Dub


class DubCoClient:
    def __init__(self, api_key: str):
        """
        Initializes the DubCoClient with a given API key.

        :param api_key: The API key to authenticate with dub.co.
        """
        self.d_client = Dub(token=api_key)

    def get_link_info(self, link_id: str) -> Dict:
        """
        Fetches information about a specific link using its ID.

        :param link_id: The ID of the link to retrieve information for.
        :return: A dictionary containing the link's information.
        :raises: Raises an exception if the request fails or returns an unexpected result.
        """
        res = self.d_client.links.get(request={"link_id": link_id})

        if not res:
            raise Exception("Failed to retrieve link information.")

        return json.loads(res.json())

    def update_link_url(self, link_id: str, new_url: str) -> Dict:
        """
        Updates the URL for a specific link using its ID.

        :param link_id: The ID of the link to update.
        :param new_url: The new URL to associate with the link.
        :return: A dictionary containing the updated link's information.
        :raises: Raises an exception if the update fails.
        """
        res = self.d_client.links.update(
            link_id=link_id,
            request_body={"url": new_url},
        )

        if not res:
            raise Exception("Failed to update the link URL.")

        return json.loads(res.json())
