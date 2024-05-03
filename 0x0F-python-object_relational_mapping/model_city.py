#!/usr/bin/python3

# Write a Python file similar to model_state.py named model_city.py that contains the class definition of a City.

#     City class:
#         inherits from Base (imported from model_state)
#         links to the MySQL table cities
#         class attribute id that represents a column of an auto-generated, unique integer, can’t be null and is a primary key
#         class attribute name that represents a column of a string of 128 characters and can’t be null
#         class attribute state_id that represents a column of an integer, can’t be null and is a foreign key to states.id
#     You must use the module SQLAlchemy


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
