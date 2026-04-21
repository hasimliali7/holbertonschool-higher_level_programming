#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa.
Usage: ./0-select_states.py <mysql username> <mysql password> <database name>
"""
import MySQLdb
import sys


if __name__ == "__main__":
    # Argumentləri götürürük
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Bazaya qoşuluruq
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    # Cursor yaradırıq (sorguları icra etmək üçün)
    cursor = db.cursor()

    # SQL sorğusunu icra edirik
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Bütün nəticələri götürürük
    rows = cursor.fetchall()

    # Nəticələri çap edirik
    for row in rows:
        print(row)

    # Bağlantıları bağlayırıq
    cursor.close()
    db.close()
