#!/usr/bin/python3
"""
    Export data in the JSON format
"""

import json
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


def export_to_JSON(data, todo):
    """Exports data in the JSON format"""
    dictionary = {}
    count = -1

    for task in todo:
        e_id = task.get("userId")
        if e_id not in dictionary.keys():
            dictionary[e_id] = []
            count += 1

        username = data[count].get("name")
        task_completed_status = task.get("completed")
        task_title = task.get("title")

        sub_dictionary = {
                "task": task_title,
                "completed": task_completed_status,
                "username": username
                }

        dictionary[e_id].append(sub_dictionary)

    json_obj = json.dumps(dictionary)

    with open("todo_all_employees.json", 'w') as f:
        f.write(json_obj)


if __name__ == "__main__":
    data, todo = fetch_data()
    export_to_JSON(data, todo)
