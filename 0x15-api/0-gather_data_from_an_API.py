"""
    This script uses REST API nd returns information about
    an employee's todo list
"""
import sys
import requests


def get_data(e_id=None):
    """Fetches the data from the url"""
    user_data = requests.get("https://jsonplaceholder.typicode.com/users/{e_id}")
    user_data = user_data.json()
    print(user_data)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        get_data(sys.argv[1])
    else:
        print("Usage: 0-gather_data_from_an_API.py employee_id")
