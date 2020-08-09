#!/usr/bin/python3
""" Get all states """
import MySQLdb
from sys import argv


if __name__ == '__main__':
    """Get all states"""
    conn = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                                password=argv[2], db=argv[3])
    cur = conn.cursor()

    cur.execute("SELECT cities.name FROM cities INNER JOIN states ON\
                 cities.state_id = states.id WHERE states.name=%s\
                 ORDER BY cities.id ASC", (argv[4],))
    rows = cur.fetchall()
    list_cities = []
    for row in rows:
        list_cities.append(row[0])
    print(', '.join(list_cities))
    cur.close()
    conn.close()
