#!/usr/bin/python3

"""This module defines the State class representing states in the database."""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class State(Base):
    """
    A class to represent a state entity in the database.

    Attributes:
    - id: The unique identifier for the state.
    - name: The name of the state.
    """
    __tablename__ = 'states'

    id = Column(Integer, autoincrement="auto", unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
