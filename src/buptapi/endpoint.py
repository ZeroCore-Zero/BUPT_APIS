from typing import Optional, Type
from buptapi.service import Service

class Endpoint:
    def __init__(self, path: str) -> None:
        self.path = path

    def __get__(self, obj: Optional[Service], owner: Type[Service]) -> str:
        base = obj if obj is not None else owner
        return base.BASEURI + self.path
