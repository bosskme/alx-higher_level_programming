#!/usr/bin/python3
# Here is a script that lists all states from the hbtn_0e_0_usa db
# Using the MySQL module

import sys
import MySQLdb

def list_states(username, password, database):
    # Connect to the MySQL server
    db = MySQLdb.connect(host='localhost', port=3306, user=username, passwd=password, db=database)
    cursor = db.cursor()

    # Execute the query to retrieve all states
    query = "SELECT * FROM states ORDER BY id ASC"
    cursor.execute(query)

    # Fetch all the rows and display the results
    states = cursor.fetchall()
    for state in states:
        print(state)

    # Close the database connection
    cursor.close()
    db.close()

# Provide the MySQL credentials and database name as command-line arguments
if __name__ == '__main__':
    import sys

    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
    else:
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        list_states(username, password, database)
