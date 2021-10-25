from sqlalchemy import ARRAY, Column, Float, Integer, String

from database.db import Base


class Material(Base):
    __tablename__ = "material"

    id = Column(Integer(), primary_key=True)
    names = Column(ARRAY(String))
    nature = Column(Float())
    destruction = Column(Float())
    water = Column(Float())
    env = Column(Float())
    treatment = Column(Float())
    benef = Column(Float())
    health = Column(Float())
    animal = Column(Float())
