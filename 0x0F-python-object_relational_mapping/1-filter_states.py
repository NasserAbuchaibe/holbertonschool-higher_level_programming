#!/usr/bin/python3
""" Filter states """
import MySQLdb
from sys import argv


if __name__ == '__main__':
    """  MySQLdb. """
    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()

    cur.execute('SELECT * FROM states WHERE name LIKE "N%" ORDER BY id ASC')
    dataRow = cur.fetchall()
    for row in dataRow:
        print(row)

    db.close()
    cur.close()
