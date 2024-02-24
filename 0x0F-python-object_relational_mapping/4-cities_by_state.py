#!/usr/bin/python3
"""
A script that lists all cities from
the database `hbtn_0e_4_usa`.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Access database and get the cities
    from the database.
    """

    db = MySQLdb.connect(host="localhost", port=3306,
                            user=argv[1], passwd=argv[2], db=argv[3])

    with db.cursor() as cursor:
        cursor.execute("SELECT cities.id, cities.name, states.name \
                                FROM cities JOIN states ON cities.state_id \
                                = states.id ORDER BY cities.id ASC")
        states = cursor.fetchall()

    if states is not None:
        for state in states:
            print(state)
