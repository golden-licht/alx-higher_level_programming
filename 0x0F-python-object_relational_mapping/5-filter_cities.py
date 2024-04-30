#!/usr/bin/python3

"""
When run as a script, lists all cities found in a state, which
is passed as an argument

first and second argument should be mysql username and password.
third argument is the name of the database.
and the fourth is the state name.
"""

from sys import argv
import MySQLdb

if __name__ == '__main__':
    username, password, database, state_name = argv[1:]
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        password=password,
        database=database)
    cursor = db.cursor()

    cursor.execute("""SELECT cities.name
                   FROM cities, states
                   WHERE cities.state_id = states.id
                   AND states.name = %s""", (state_name,))

    all_rows = cursor.fetchall()
    len = len(all_rows) - 1

    for row in all_rows:
        print(row[0], end=', ' if len else '')
        len -= 1
    print()
