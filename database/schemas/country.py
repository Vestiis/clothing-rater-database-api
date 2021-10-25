from sqlalchemy import ARRAY, Column, Float, Integer, String

from database.db import Base


class Country(Base):
    __tablename__ = "country"

    id = Column(Integer(), primary_key=True)
    names = Column(ARRAY(String))
    politique = Column(Float())
    human_rights = Column(Float())
    work = Column(Float())
    societal = Column(Float())
