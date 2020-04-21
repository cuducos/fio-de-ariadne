from datetime import date, datetime
from re import findall, sub, match
from typing import Optional


def to_color(text: str) -> str:
    mapping = {
        "castanho": "Castanhos",
        "castanhos": "Castanhos",
        "azul": "Azul",
        "azuis": "Azul",
        "morena": "Morena",
        "moreno": "Morena",
        "preto": "Preto",
        "pretos": "Preto",
        "loiros": "Loiro",
        "loiro": "Loiro",
        "ruivo": "Ruivo",
        "ruiva": "Ruivo",
        "ruivos": "Ruivo",
        "branco": "Branca",
        "branca": "Branca",
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


def to_age(value: str) -> Optional[int]:
    matches = match(r"\d{1,2}", value)
    return int(matches.group(0)) if matches else None
