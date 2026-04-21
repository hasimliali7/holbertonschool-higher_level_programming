#!/usr/bin/python3
"""
Lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    # Argumentləri götürürük
    db_user = sys.argv[1]
    db_password = sys.argv[2]
    db_name = sys.argv[3]

    # Bazaya qoşuluruq
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=db_user,
        passwd=db_password,
        db=db_name
    )

    # Cursor yaradırıq
    cursor = db.cursor()

    # SQL sorğusu: Adı 'N' ilə başlayanları ID-yə görə sıralayırıq
    # BINARY istifadə edirik ki, məhz böyük 'N' olduğunu dəqiqləşdirək
    query = "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC"
    cursor.execute(query)

    # Nəticələri götürürük
    rows = cursor.fetchall()

    # Nəticələri çap edirik
    for row in rows:
        print(row)

    # Bağlantıları bağlayırıq
    cursor.close()
    db.close()
