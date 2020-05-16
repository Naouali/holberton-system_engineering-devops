#!/usr/bin/python3
"""
fetch data from
an api
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
    my_list = []
    mydic = {}
    myotherdic = {}
    myfile = str(id) + '.json'
    for i in data.json():
        mydic['task'] = (i['title'])
        mydic['competed'] = i['completed']
        mydic['username'] = name
        my_list.append(mydic)
    myotherdic[str(id)] = my_list
    with open(myfile, "w") as f:
        json.dump(myotherdic, f)
