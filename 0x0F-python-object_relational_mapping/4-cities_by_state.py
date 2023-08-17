#!/usr/bin/python3
"""
This script lists all cities and their states from the database hbtn_0e_4_usa
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    user, passwd, db = argv[1:]
    conn = MySQLdb.connect(
            host="localhost", port=3306, user=user, passwd=passwd, db=db,
            charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT c.id, c.name, s.name\
                FROM cities c\
                JOIN states s ON c.state_id=s.id\
                ORDER BY c.id")
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()
