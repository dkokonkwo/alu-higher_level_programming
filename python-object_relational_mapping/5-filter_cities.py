#!/usr/bin/python3
"""
lists all the cities that match state in the table of a database
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    conn = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    cur.execute("SELECT c.name FROM cities AS c \
                INNER JOIN states AS s ON c.state_id = s.id \
                WHERE s.name = '{}' \
                ORDER BY c.id ASC".format(argv[4]))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
