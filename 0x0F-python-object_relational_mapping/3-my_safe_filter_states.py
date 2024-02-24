#!/usr/bin/python3
"""
A script takes in an argument and
displays all values in the states
where `name` matches the argument
from the database `hbtn_0e_0_usa`.
This time the script is safe from
MySQL injections!
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """
    Access the database and get the states
    from the database.
    """
    db = MySQLdb.connect(host="localhost", port=3306,
                            user=argv[1], passwd=argv[2], db=argv[3])

    cursor = db.cursor()
    cursor.execute(
        "SELECT * FROM states WHERE name LIKE \
                    BINARY %(name)s ORDER BY states.id ASC", {'name': argv[4]})

    states = cursor.fetchall()

    for state in states:
        print(state)
