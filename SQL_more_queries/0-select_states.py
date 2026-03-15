#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa.
Usage: ./0-select_states.py <mysql username> \
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

    # Create a cursor object to execute queries
    cursor = db.cursor()
    
    # Execute the SQL query
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    
    # Fetch all the rows
    rows = cursor.fetchall()
    
    # Display results
    for row in rows:
        print(row)

    # Close cursor and connection
    cursor.close()
    db.close()
