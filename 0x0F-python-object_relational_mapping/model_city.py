#!/usr/bin/python3


"""This module defines the City class representing cities in the database."""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey

Base = declarative_base()


class City(Base):
    """
    A class to represent a city entity in the database.

    Attributes:
    - id: The unique identifier for the city.
    - name: The name of the city.
    - state_id: Foreign key to states.id.
    """
    __tablename__ = 'cities'

    id = Column(Integer, autoincrement=True, unique=True,
                nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
