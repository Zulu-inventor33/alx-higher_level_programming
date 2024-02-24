#!/usr/bin/python3
"""
A script that lists all states with
a `name` starting with the letter `N`
from the database `hbtn_0e_0_usa`.
"""

import MySQLdb
from sys import argv

"""
Access the database and get the states
from the database.
"""

if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", port=3306,
                            user=argv[1], passwd=argv[2], db=argv[3])
    cursor = db.cursor()

    cursor.execute(
        "SELECT * FROM states WHERE name LIKE BINARY 'N%' \
                ORDER BY states.id ASC")

    states = cursor.fetchall()

    for state in states:
        print(state)
