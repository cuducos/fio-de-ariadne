from abc import ABCMeta, abstractmethod
from re import findall
from typing import Iterable, List, Optional

from crawler.cast import to_age, to_color, to_date
from crawler.typing import Cast, FieldValue


class Parser(metaclass=ABCMeta):
    def __init__(self, labels: List[str], cast: Optional[Cast] = None) -> None:
        self.cast_method = cast
        self.labels = labels
        self.tokens = set(label.lower() for label in self.labels)

    @abstractmethod
    def parse(self, text: Iterable[str]) -> str:
        pass

    def cast(self, value: str) -> FieldValue:
        if not value:
            return None

        if not self.cast_method:
            return value

        return self.cast_method(value)

    def __str__(self) -> str:
        return f"{self.__class__.__name__}({self.labels})"

    def __call__(self, text: Iterable[str]) -> FieldValue:
        output = self.parse(text)
        return self.cast(output)


class WeakParser(Parser):
    def parse(self, text: Iterable[str]) -> str:
        for line in text:
            words = set(word.lower() for word in findall(r"\w+", line))
            if self.tokens & words:
                return line

        return ""


class ExactParser(Parser):
    def parse(self, text: Iterable[str]) -> str:
        for label in self.labels:
            label = f"{label}:"
            for line in text:
                line = line.strip()
                if not line.startswith(label):
                    continue

                content = line.replace(label, "", 1).strip()
                return content

        return ""


PARSERS = {
    "dob": ExactParser(["Data de nascimento", "Nasc."], cast=to_date),
    "mother": ExactParser(["Mãe", "Nome da Mãe"]),
    "father": ExactParser(["Pai", "Nome do Pai"]),
    "missing_since": ExactParser(["Desap.", "Data do desaparecimento"], cast=to_date),
    "last_seen_at": ExactParser(["Local", "Local do desaparecimento"]),
    "age_at_occurrence": ExactParser(
        ["Idade", "Idade na data do Desaparecimento"], cast=to_age
    ),
    "eyes": WeakParser(["olho", "olhos"], cast=to_color),
    "hair": WeakParser(["cabelo", "cabelos"], cast=to_color),
    "skin": WeakParser(["pele"], cast=to_color),
}
