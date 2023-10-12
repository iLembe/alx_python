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
        completed_tasks = [task for task in todos_data if task["completed"]]
        total_tasks = len(todos_data)

        print(f"Employee {employee_name} is done with tasks ({len(completed_tasks)}/{total_tasks}):")

        for task in completed_tasks:
            print(f"\t{task['title']}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python 0-gather_data_from_an_API.py <employee_id>")
    else:
        employee_id = sys.argv[1]
        gather_employee_data(employee_id)

