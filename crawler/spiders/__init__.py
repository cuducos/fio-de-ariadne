from re import IGNORECASE, match
from typing import Dict, Tuple
from unicodedata import category, normalize

from requests import get
from scrapy import Spider


class IbgeSpider(Spider):
    """Implements a `self.cities` dictionary with names for cities of a given
    state (defined by `self.abbr` in the class that inherits from this one) and
    a `normalize_city_and_state_for` method."""

    URL = "https://servicodados.ibge.gov.br/api/v1/localidades/estados/"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cities = {self.as_slug(city): city for city in self.get_cities()}

    @staticmethod
    def as_slug(value: str) -> str:
        cleaned = "".join(
            char for char in normalize("NFD", value.lower()) if category(char) != "Mn"
        )
        return cleaned.replace(" ", "-")

    @property
    def state(self) -> str:
        value = getattr(self, "abbr", None)
        if not value:
            msg = (
                "Para utilizar IbgeSpiderMixin é necessário configurar a "
                "varíavel `abbr` na classe do raspador."
            )
            raise NotImplementedError(msg)
        return value.upper()

    def get_state_id(self) -> int:
        self.logger.info(f"Getting state ID for {self.state} in IBGE web API")
        response = get(self.URL)
        for state in response.json():
            if not self.state == state["sigla"]:
                continue

            state_id = int(state["id"])
            break

        self.logger.info(f"Saving state ID for {self.state} as {state_id}")
        return state_id

    def get_cities(self) -> Tuple[str, ...]:
        state_id = self.get_state_id()
        self.logger.info(f"Getting city names for {self.state} in IBGE web API")
        response = get(f"{self.URL}{state_id}/municipios/")
        cities = tuple(city["nome"] for city in response.json())
        self.logger.info(f"Saving {len(cities)} cities from {self.state}")
        return cities

    def normalize_city_for(self, value: str) -> Dict[str, str]:
        slug = self.as_slug(value)
        matches = (match(city, slug, IGNORECASE) for city in self.cities)
        cities = sorted((m.group(0) for m in matches if m), key=len, reverse=True)

        if not cities:
            return {
                "last_seen_at_city": value,
                "last_seen_at_state": self.state,
            }

        city, *_ = cities
        return {
            "last_seen_at_city": self.cities[city],
            "last_seen_at_state": self.state,
        }
