import re

from crawler.api_client import APIClient
from crawler.connections import IBGEConnection


class APIClientIBGE(APIClient):
    def __init__(self, uf=None, city=None):
        super().__init__(IBGEConnection)
        self.states = self.get_states(uf)
        self.cities = self.get_cities(self.states["id"], city) if self.states else []

    def get_states(self, uf=None):
        """
        Request in states list
        """
        data_response = self.http_request(IBGEConnection.URL_STATES, "get")

        return (
            next((item for item in data_response if item["nome"] == uf), None)
            if uf
            else data_response
        )

    def get_cities(self, uf, city=None):
        """
        Request in cities list
        """
        data_response = self.http_request(
            IBGEConnection.URL_CITIES.format(uf=uf), "get"
        )

        return self.search_city(city, data_response) if city else data_response

    def search_city(self, city, data=None):
        data_response = data if data else self.cities
        return next(
            (
                item
                for item in data_response
                if re.search(item["nome"], city, re.IGNORECASE)
            ),
            None,
        )
