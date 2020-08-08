#!/usr/bin/python3
import MySQLdb
import sys


def allstates():
    conn = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                                password=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()

    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()

if __name__ == '__main__':
    allstates()
