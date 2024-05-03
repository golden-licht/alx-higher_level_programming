#!/usr/bin/python3

"""
When run as a script, lists all states that contain the letter a.
First and second argument should be mysql username and password.
Third argument is the name of the database.
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_state import State

if __name__ == "__main__":
    username, password, database = argv[1:]
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(username, password, database))
    Session = sessionmaker(bind=engine)
    session = Session()

    for instance in session.query(State).filter(
            State.name.like('%a%')).order_by(State.id):
        print("{}: {}".format(instance.id, instance.name))

    session.close()
