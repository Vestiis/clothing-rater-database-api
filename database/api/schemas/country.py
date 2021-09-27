from typing import Optional

from pydantic import BaseConfig, BaseModel


class Country(BaseModel):
    name: str
    situation: Optional[float]
    corruption: Optional[float]
    poverty_rate: Optional[float]
    human_freedom_index: Optional[float]
    global_food_security_index: Optional[float]
    minimum_monthly_salary: Optional[float]

    class Config(BaseConfig):
        orm_mode = True
