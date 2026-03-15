#!/usr/bin/python3
"""
Displays all values in the states table of hbtn_0e_0_usa
where name matches the argument provided.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    # Get arguments from command line
    # sys.argv[4] is the state name we are searching for
    user = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]
    state_searched = sys.argv[4]

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
    
    # Create the query using .format() as required
    # BINARY is used to ensure case-sensitive matching
    query = "SELECT * FROM states WHERE name LIKE BINARY '{}' \
             ORDER BY states.id ASC".format(state_searched)
    
    cursor.execute(query)
    
    # Fetch and print results
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Clean up
    cursor.close()
    db.close()  
