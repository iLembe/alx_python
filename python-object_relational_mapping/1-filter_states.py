#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    # Check for the correct number of command-line arguments
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    # Command-line arguments
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    try:
        # Connect to the MySQL server
        db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
        cursor = db.cursor()

        # Execute the SQL query to select states starting with 'N'
        cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

        # Fetch all the rows
        rows = cursor.fetchall()

        # Display the results
        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print("MySQL Error: {}".format(e))
        sys.exit(1)

    finally:
        # Close the database connection
        if db:
            db.close()
