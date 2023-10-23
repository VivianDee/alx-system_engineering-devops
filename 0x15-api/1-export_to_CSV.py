#!/usr/bin/python3
"""
    Export data in the CSV format
"""

import csv
import requests
import sys


def fetch_data(e_id=None):
    """Fetches the data from the url"""
    user_data = requests.get(
            "https://jsonplaceholder.typicode.com/users/{}".format(e_id))

    user_todos = requests.get(
            "https://jsonplaceholder.typicode.com/todos",
            params={"userId": e_id})

    user_data = user_data.json()
    user_todos = user_todos.json()

    return user_data, user_todos


def export_to_CSV(data, todo, e_id):
    """Exports data in the CSV format"""
    username = data.get("name")

    with open("{}.csv".format(e_id), 'w', newline="") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)

        for task in todo:
            task_completed_status = task.get("completed")
            task_title = task.get("title")
            writer.writerow(
                    [e_id, username, task_completed_status, task_title])


if __name__ == "__main__":
    if len(sys.argv) > 1:
        e_id = sys.argv[1]
        data, todo = fetch_data(e_id)
        export_to_CSV(data, todo, e_id)
    else:
        print("1-export_to_CSV.py employee_id")
