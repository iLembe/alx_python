"""
This script gathers employee data from the JSONPlaceholder API and exports the tasks for a specific employee to a CSV file.

Usage:
python 1-export_to_CSV.py <employee_id>

Requirements:
- Records all tasks that are owned by this employee
- Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
- File name must be: USER_ID.csv
"""

import csv
import requests
import sys

def gather_employee_data(employee_id):
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

    try:
        # Fetch data
        employee_response = requests.get(employee_url)
        todos_response = requests.get(todos_url)

        # Check for errors
        employee_response.raise_for_status()
        todos_response.raise_for_status()

        employee_data = employee_response.json()
        todos_data = todos_response.json()

        if not employee_data:
            print("Employee not found.")
            return

        employee_name = employee_data["name"]

        # Create a CSV file for the employee
        with open(f"{employee_id}.csv", mode="w", newline="") as csv_file:
            fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()

            for task in todos_data:
                writer.writerow({
                    "USER_ID": employee_id,
                    "USERNAME": employee_name,
                    "TASK_COMPLETED_STATUS": task["completed"],
                    "TASK_TITLE": task["title"]
                })

        print(f"Data exported to {employee_id}.csv")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python 1-export_to_CSV.py <employee_id>")
    else:
        employee_id = sys.argv[1]
        gather_employee_data(employee_id)
