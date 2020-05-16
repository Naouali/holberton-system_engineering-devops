#!/usr/bin/python3
"""
fetch data from
an api
"""


import urllib.request
import sys
with urllib.request.urlopen("https://jsonplaceholder.typicode.com/todos/"+
        sys.argv[1]) as response:
    html = response.read()
print(html)
print(type(html))
