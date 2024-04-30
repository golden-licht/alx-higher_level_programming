#!/usr/bin/python3

""" When run as a script, lists all states with a name that matches with the
one passed as argument

first and second argument should be mysql username and password.
third argument is the name of the database.
fourth argument is the state name to be searched.
"""


from sys import argv
import MySQLdb
from MySQLdb.constants import FIELD_TYPE

if __name__ == "__main__":
    username, password, database, state_name = argv[1:]

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        password=password,
        database=database)
    cursor = db.cursor()
    cursor.execute("""SELECT * FROM states
                  WHERE BINARY name = %s
                  ORDER BY id ASC""", (state_name,))
    # fetch all the rows
    all_rows = cursor.fetchall()

    for row in all_rows:
        print(row)
