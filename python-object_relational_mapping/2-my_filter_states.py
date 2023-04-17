#!/usr/bin/python3
"""
lists all the states in the table of a database
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    conn = MySQLdb.connect(
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    cur = conn.cursor()
    cur.execute("SELECT id, name FROM states where \
                BINARY name = '{}'".format(argv[4]))
    query_rows = cur.fetchall()
    for x in query_rows:
            print(x)
    cur.close()
    conn.close()
