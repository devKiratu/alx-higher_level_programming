#!/usr/bin/python3
"""
This script takes in the name of a state as an argument and lists all cities
of that state, using the database hbtn_0e_4_usa in an SQL Injection free way
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    user, passwd, db, state = argv[1:]
    conn = MySQLdb.connect(
            host="localhost", port=3306, user=user, passwd=passwd, db=db,
            charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT c.name\
                FROM cities c\
                JOIN states s ON c.state_id=s.id\
                WHERE s.name = %s\
                ORDER BY c.id", (state,))
    rows = cur.fetchall()
    cities = []
    for row in rows:
        c, = row
        cities.append(c)
    print(", ".join(cities))

    cur.close()
    conn.close()
