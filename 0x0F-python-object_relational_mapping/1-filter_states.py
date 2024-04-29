#!/usr/bin/python3

""" When run as a script, lists all states with a name starting with N from
the states tableof a database that is given as a third argument,
the first and second argument being username and password to access mysql """

from sys import argv
from MySQLdb import _mysql
from MySQLdb.constants import FIELD_TYPE

if __name__ == "__main__":
    username, password, database = [argv[1], argv[2], argv[3]]
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
                    WHERE BINARY name LIKE 'N%'
                    ORDER BY id ASC""")
    result = db.store_result()
    # fetch all the rows
    all_rows = result.fetch_row(maxrows=0)

    for row in all_rows:
        print(row)
