#!/usr/bin/python3
"""
    This script uses REST API nd returns information about
    an employee's todo list
"""
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


def display_progress(data, todo):
    """Displays the employee's TODO list progress"""
    completed_tasks = 0
    total_tasks = 0

    for task in todo:
        if task.get("completed"):
            completed_tasks += 1
        total_tasks += 1

    print("Employee {} is done with tasks({}/{}):".format(
        data.get("name"), completed_tasks, total_tasks))
    for task in todo:
        if task.get("completed"):
            print("\t {}".format(task.get("title")))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        data, todo = fetch_data(sys.argv[1])
        display_progress(data, todo)
    else:
        print("Usage: 0-gather_data_from_an_API.py employee_id")
