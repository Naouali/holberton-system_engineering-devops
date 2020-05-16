#!/usr/bin/python3
"""
module to fetch data
and store in csv file
"""


import requests
import sys
import csv

if __name__ == "__main__":

    id = sys.argv[1]
    data = requests.get('https://jsonplaceholder.typicode.com/users/' + id)
    name = data.json()['username']
    data = requests.get(
            'https://jsonplaceholder.typicode.com/users/'+id+'/todos')
    f = (id + '.csv')
    l = []
    with open(f, "w") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in data.json():
            l.append(id)
            l.append(name)
            l.append(task['completed'])
            l.append(task['title'])
            writer.writerow(l)
            l.clear()
