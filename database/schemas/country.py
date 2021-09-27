from sqlalchemy import Column, Float, String

from database.db import Base


class Country(Base):
    __tablename__ = "country"

    name = Column(String(), primary_key=True)
    situation = Column(Float())
    corruption = Column(Float())
    poverty_rate = Column(Float())
    human_freedom_index = Column(Float())
    global_food_security_index = Column(Float())
    minimum_monthly_salary = Column(Float())
