#!/usr/bin/python3

"""
When run as a script, changes the name of the state with id = 2 to New Mexico.
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
    state_with_id_2 = session.query(State).filter_by(id=2).first()
    state_with_id_2.name = "New Mexico"

    session.commit()
    session.close()
