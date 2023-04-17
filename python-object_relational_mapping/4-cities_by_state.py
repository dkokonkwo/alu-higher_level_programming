#!/usr/bin/python3
"""
lists all the cities and states in the table of a database
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    conn = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    cur.execute("SELECT c.id, c.name, s.name FROM cities as c \
                INNER JOIN states as s ON c.state_id = s.id \
                ORDER BY c.id")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
