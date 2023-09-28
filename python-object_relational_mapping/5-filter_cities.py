#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    # Check for the correct number of command-line arguments
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(sys.argv[0]))
        sys.exit(1)

    # Command-line arguments
    username, password, database, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    try:
        # Connect to the MySQL server
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
        )
        cursor = db.cursor()

        # Execute the SQL query to select cities of the specified state and sort by id
        cursor.execute("SELECT GROUP_CONCAT(cities.name SEPARATOR ', ') "
                       "FROM cities JOIN states ON cities.state_id = states.id "
                       "WHERE states.name = %s "
                       "ORDER BY cities.id ASC", (state_name,))

        # Fetch the result
        result = cursor.fetchone()

        if result[0]:
            print(result[0])

    except MySQLdb.Error as e:
        print("MySQL Error: {}".format(e))
        sys.exit(1)

    finally:
        # Close the database connection
        if db:
            db.close()
