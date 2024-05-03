#!/usr/bin/python3

"""
When run as a script, prints all cities with their states from cities table.
First and second argument should be mysql username and password.
Third argument is the name of the database.
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_state import State
from model_city import City

if __name__ == "__main__":
    username, password, database = argv[1:]
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(username, password, database))
    Session = sessionmaker(bind=engine)
    session = Session()

    for city, state in session.query(
            City, State).filter(City.state_id == State.id):
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
