#!/usr/bin/python3
"""
Lists all states with a name starting with N from the database hbtn_0e_0_usa.
Usage: ./1-filter_states.py <mysql username> \
                             <mysql password> \
                             <database name>
"""
import MySQLdb
import sys


if __name__ == "__main__":
    # Get arguments from command line
    user = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        user=user,
        passwd=passwd,
        db=db_name,
        port=3306
    )

    # Create a cursor object
    cursor = db.cursor()
    
    # Execute the SQL query with filtering
    # BINARY ensures the 'N' is case-sensitive
    query = "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC"
    cursor.execute(query)
    
    # Fetch and print results
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Clean up
    cursor.close()
    db.close()
