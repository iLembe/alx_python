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
        user_id = employee_data["id"]
        completed_tasks = [task for task in todos_data if task["completed"]]

        # Prepare data for CSV
        csv_data = []
        for task in completed_tasks:
            task_title = task["title"]
            task_completed = "completed" if task["completed"] else "not completed"
            csv_data.append([user_id, employee_name, task_completed, task_title])

        # Write to CSV
        csv_filename = f"{user_id}.csv"
        with open(csv_filename, mode="w", newline="") as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
            csv_writer.writerows(csv_data)

        print(f"CSV file '{csv_filename}' has been created.")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python 1-export_to_CSV.py <employee_id>")
    else:
        employee_id = sys.argv[1]
        gather_employee_data(employee_id)
