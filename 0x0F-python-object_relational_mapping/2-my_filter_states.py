#!/usr/bin/python3

""" When run as a script, lists all states with a name that matches with the
one passed as argument

first and second argument should be mysql username and password.
third argument is the name of the database.
fourth argument is the state name to be searched.
"""


from sys import argv
from MySQLdb import _mysql
from MySQLdb.constants import FIELD_TYPE

if __name__ == "__main__":
    username, password, database, state_name = argv[1:]
    # to convert mysql types to python types
    my_conv = {FIELD_TYPE.LONG: int, FIELD_TYPE.VAR_STRING: str}

    db = _mysql.connect(
        conv=my_conv,
        host='localhost',
        port=3306,
        user=username,
        password=password,
        database=database)
    db.query("""SELECT * FROM states
                  WHERE BINARY name = '{}'
                  ORDER BY id ASC""".format(state_name))
    result = db.store_result()
    # fetch all the rows
    all_rows = result.fetch_row(maxrows=0)

    for row in all_rows:
        print(row)
