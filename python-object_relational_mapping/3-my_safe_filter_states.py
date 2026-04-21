#!/usr/bin/python3
"""
Wait, do you contain the same code as Task 2?
Yes, but this one is safe from MySQL injections!
"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    # SQL Injection-dan qorunmaq üçün %s istifadə edirik
    cursor.execute("SELECT * FROM states WHERE name=%s ORDER BY id ASC",
                   (sys.argv[4],))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
