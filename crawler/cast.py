from datetime import date, datetime
from re import findall, sub
from typing import Optional


def to_color(text: str) -> str:
    mapping = {
        "castanho": "Castanhos",
        "azul": "Azul",
        "azuis": "Azul",
        "morena": "Morena",
        "moreno": "Morena",
    }

    words = set(word.lower() for word in findall(r"\w+", text))
    for key, value in mapping.items():
        if key in words:
            return value

    return text


def to_date(value: str) -> Optional[date]:
    value = sub(r"[^\d/]", "", value)
    try:
        return datetime.strptime(value, "%d/%m/%Y").date()
    except ValueError:
        return None
