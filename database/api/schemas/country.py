import json
from typing import List

from pydantic import BaseConfig, BaseModel


class Country(BaseModel):
    id: int
    names: List[str]
    politique: float
    human_rights: float
    work: float
    societal: float

    class Config(BaseConfig):
        orm_mode = True

    def __hash__(self):
        return hash(json.dumps(self.dict()))

    def __eq__(self, other: "Country"):
        return json.dumps(self.dict()) == json.dumps(other.dict())
