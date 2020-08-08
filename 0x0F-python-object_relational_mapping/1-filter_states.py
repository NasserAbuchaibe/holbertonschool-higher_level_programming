#!/usr/bin/python3
import MySQLdb
import sys


def filterStates():
    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()

    cur.execute('SELECT * FROM states WHERE name LIKE "N%" ORDER BY id ASC')
    dataRow = cur.fetchall()
    for row in dataRow:
        print(row)

    db.close()
    cur.close()


if __name__ == '__main__':
    filterStates()
