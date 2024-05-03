#!/usr/bin/python3

# Next, write a script 14-model_city_fetch_by_state.py that prints all City objects from the database hbtn_0e_14_usa:

#     Your script should take 3 arguments: mysql username, mysql password and database name
#     You must use the module SQLAlchemy
#     You must import State and Base from model_state - from model_state import Base, State
#     Your script should connect to a MySQL server running on localhost at port 3306
#     Results must be sorted in ascending order by cities.id
#     Results must be display as they are in the example below (<state name>: (<city id>) <city name>)
#     Your code should not be executed when imported

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

    for city, state in session.query(City, State).filter(City.state_id == State.id):
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
