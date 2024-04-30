#!/usr/bin/python3

"""
When run as a script, lists cities with their corresponding states
first and second argument should be mysql username and password.
third argument is the name of the database.
"""

from sys import argv
import MySQLdb

if __name__ == '__main__':
    username, password, database = argv[1:]
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        password=password,
        database=database)
    cursor = db.cursor()

    cursor.execute("""SELECT cities.id, cities.name, states.name
                   FROM cities, states
                   WHERE cities.state_id = states.id""")

    all_rows = cursor.fetchall()
    for row in all_rows:
        print(row)
