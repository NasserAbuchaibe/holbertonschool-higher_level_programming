#!/usr/bin/python3
""" Filter states """
import MySQLdb
from sys import argv


def filterEstates():
    """  MySQLdb. """
    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()

    cur.execute('SELECT * FROM states WHERE name LIKE\
                BINARY "N%" ORDER BY id ASC')
    states = cur.fetchall()
    for row in states:
        print(row)

    db.close()

if __name__ == '__main__':
    filterEstates()
