from typing import Optional

from pydantic import BaseConfig, BaseModel


class Material(BaseModel):
    name: str
    description: Optional[str]
    is_recyclable: Optional[float]
    has_plant_based_fibers: Optional[str]
    has_animal_based_fibers: Optional[str]
    is_synthetic: Optional[str]
    is_semi_synthetic: Optional[str]
    is_artificial: Optional[str]
    health_harmfulness: Optional[float]
    skin_friendlyness: Optional[float]

    class Config(BaseConfig):
        orm_mode = True
