from typing import Optional
from abc import ABC

class Service(ABC):
    BASEURI: str = ""

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        if cls.BASEURI == "":
            raise TypeError(f"{cls.__name__} must define a non-empty BASEURI")

    def __init__(self, baseuri: Optional[str] = None) -> None:
        self.BASEURI = baseuri or self.BASEURI
