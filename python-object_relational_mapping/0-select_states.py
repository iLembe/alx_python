import MySQLdb
import sys

if __name__ == "__main__":
    # Check if all three arguments are provided
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

    # Create a cursor object
    cursor = db.cursor()

    # Execute the SQL query to fetch all states
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the rows
    states = cursor.fetchall()

    # Print the results
    for state in states:
        print(state)

    # Close the cursor and database connection
    cursor.close()
    db.close()
