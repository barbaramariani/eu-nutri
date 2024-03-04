import requests
from src.settings import FATSECRET_CLIENT_ID

class FatSecretIntegration:
    def __init__(self):
        self.client_id = FATSECRET_CLIENT_ID

    def get_food_items(self, food_items_response):
        params = {
            "method": "foods.search.v2",
            "search_expression": food_items_response,
            "format": "json"
        }

        headers = {
            "Authorization": f"Bearer {self.client_id}"
        }

        response = requests.get("https://platform.fatsecret.com/rest/server.api", params=params, headers=headers)

        if response.status_code == 200:
            response_json = response.json()

            food_items = [food["food_name"] for food in response_json["foods_search"]["results"]["food"]]

            return food_items
        else:
            raise Exception(f"Failed to get food items from FatSecret API: {response.status_code} {response.text}")
