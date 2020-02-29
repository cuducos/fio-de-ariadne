from datetime import date
from typing import Callable, Optional, Union


FieldValue = Optional[Union[str, date]]
Cast = Callable[[str], Optional[Union[str, date]]]
