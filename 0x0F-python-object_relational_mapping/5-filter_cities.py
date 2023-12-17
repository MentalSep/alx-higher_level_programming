#!/usr/bin/python3
"""select state Module"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cursor = db.cursor()
    cursor.execute("SELECT cities.name FROM cities \
                   INNER JOIN states ON states.id=cities.state_id \
                   WHERE states.name = %s ORDER BY cities.id", (sys.argv[4],))
    results = cursor.fetchall()
    mylist = list(line[0] for line in results)
    print(*mylist, sep=", ")
    db.close()
