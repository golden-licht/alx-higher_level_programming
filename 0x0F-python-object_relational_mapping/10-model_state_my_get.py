#!/usr/bin/python3

"""
When run as a script, prints the state from states table, given the state name.
First and second argument should be mysql username and password.
Third argument is the name of the database.
Fourth argument is the name of the state name.
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_state import State

if __name__ == "__main__":
    username, password, database, name = argv[1:]
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(username, password, database))
    Session = sessionmaker(bind=engine)
    session = Session()

    state_found = False
    for instance in session.query(State).filter(State.name == name):
        state_found = True
        print("{}: {}".format(instance.id, instance.name))
    if (not state_found):
        print("Not found")

    session.close()
