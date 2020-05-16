#!/usr/bin/python3
"""
fetch data from
an api
"""

if __name__ == "__main__":
    import requests
    import sys
    id = sys.argv[1]
    res = requests.get(
            'https://jsonplaceholder.typicode.com/users/' + id)
    name = res.json()['name']
    data = requests.get(
            'https://jsonplaceholder.typicode.com/users/'+id+'/todos')
    total = len(data.json())
    number = 0
    for i in data.json():
        if i['completed'] is True:
            number += 1
    print("Employee {} is done with tasks({}/{}):".format(name, number, total))
    for task in data.json():
        if task['completed'] is True:
            print("\t {}".format(task['title']))
