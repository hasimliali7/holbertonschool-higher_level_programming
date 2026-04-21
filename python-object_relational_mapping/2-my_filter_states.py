#!/usr/bin/python3
"""
Displays all values in the states table of hbtn_0e_0_usa
where name matches the argument.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    # 4 arqumenti götürürük
    db_user = sys.argv[1]
    db_password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Bazaya qoşuluruq
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=db_user,
        passwd=db_password,
        db=db_name
    )

    cursor = db.cursor()

    # Tapşırığın tələbinə uyğun olaraq .format() istifadə edirik
    # BINARY istifadə edirik ki, böyük-kiçik hərf fərqinə (case-sensitive) baxsın
    query = "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id ASC".format(state_name)
    cursor.execute(query)

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
