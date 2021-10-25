import json
from typing import List

from pydantic import BaseConfig, BaseModel


class Material(BaseModel):
    id: int
    names: List[str]
    nature: float
    destruction: float
    water: float
    env: float
    treatment: float
    benef: float
    health: float
    animal: float

    class Config(BaseConfig):
        orm_mode = True

    def __hash__(self):
        return hash(json.dumps(self.dict()))

    def __eq__(self, other: "Material"):
        return json.dumps(self.dict()) == json.dumps(other.dict())
