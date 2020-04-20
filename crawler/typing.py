from datetime import date
from typing import Callable, Optional, Union


FieldValue = Optional[Union[date, int, str]]
Cast = Callable[[str], FieldValue]
