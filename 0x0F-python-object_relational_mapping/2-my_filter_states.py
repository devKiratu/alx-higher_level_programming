#!/usr/bin/python3
"""
This script takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    user, passwd, db, state = argv[1:]
    conn = MySQLdb.connect(
            host="localhost", port=3306, user=user, passwd=passwd, db=db,
            charset="utf8")
    cur = conn.cursor()
    cur.execute(
                "SELECT * FROM states\
                 WHERE name LIKE BINARY '{}'".format(state)
                )
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()
