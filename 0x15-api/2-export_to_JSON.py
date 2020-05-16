#!/usr/bin/python3
"""
fetch data from
an api and stored into
json file
"""


import json


if __name__ == "__main__":
    import requests
    import sys
    id = sys.argv[1]
    res = requests.get(
            'https://jsonplaceholder.typicode.com/users/' + id)
    name = res.json()['name']
    data = requests.get(
            'https://jsonplaceholder.typicode.com/users/'+id+'/todos')
    stored = str(id) + '.json'
    mydata = {}
    with open (stored, "w") as f:
        for i in data.json():
            my_dict = {}
            my_dict['tast'] = i['title']
            my_dict['username'] = name
            my_dict['completed'] = i['completed']
        mydata[str(id)] = my_dict
        json.dump(mydata, f)
    
