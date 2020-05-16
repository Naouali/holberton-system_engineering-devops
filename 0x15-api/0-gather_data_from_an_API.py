#!/usr/bin/python3
"""
fetch data from
an api
"""

if __name__ == "__main__":
    import requests
    import sys
    id = sys.argv[1]
    data = requests.get(
        'https://jsonplaceholder.typicode.com/users/' + id)
    name = data.json()["name"]
    todo = requests.get(
        'https://jsonplaceholder.typicode.com/users/'+name+'/todos')
    total = len(todo.json())
    number = 0
    for i in todo.json():
        if i['competed'] is True:
            number += 1
    print('Employee {} is done with tasks({}/{}):'.format(name, number, total))
    for task in todo.json():
        if task['completed'] is True:
            print("\t {}".format(task['title']))
