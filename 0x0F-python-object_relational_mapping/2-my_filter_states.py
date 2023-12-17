#!/usr/bin/python3
"""select state Module"""
import MySQLdb
import sys


if __name__ == "__main__":
    """lists all states with a name starting with N from the database"""
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'"
                   .format(sys.argv[4]))
    results = cursor.fetchall()
    for line in results:
        print(line)
    db.close()
