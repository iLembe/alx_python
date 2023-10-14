"""
Script to gather data for all employees from an API and export it to a JSON file.

Requirements:
- Records all tasks from all employees
- Format: { "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ], ... }
- File name must be: todo_all_employees.json
"""

import json
import requests

def gather_all_employee_data():
    base_url = "https://jsonplaceholder.typicode.com/users"
    all_employee_data = {}

    try:
        # Fetch data for all employees
        employee_response = requests.get(base_url)
        employee_response.raise_for_status()
        employees_data = employee_response.json()

        for employee in employees_data:
            employee_id = employee["id"]
            employee_name = employee["username"]

            todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
            todos_response = requests.get(todos_url)
            todos_response.raise_for_status()
            todos_data = todos_response.json()

            employee_tasks = []

            for task in todos_data:
                employee_tasks.append({
                    "username": employee_name,
                    "task": task["title"],
                    "completed": task["completed"]
                })

            all_employee_data[employee_id] = employee_tasks

        # Export data to JSON file
        with open("todo_all_employees.json", "w") as json_file:
            json.dump(all_employee_data, json_file, indent=4)

        print("Data exported to todo_all_employees.json")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    gather_all_employee_data()
