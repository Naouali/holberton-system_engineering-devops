#!/usr/bin/python3
"""
module to return
top 10 hot reddit posts
"""


import requests


def top_ten(subreddit):
    """
    return to 10 posts
    """
    headers = {'user-agent': 'linux'}
    url = 'https://api.reddit.com/r/' + subreddit
    res = requests.get(url, headers=headers)
    try:
        data = res.json()
    except:
        print("None")
        return
    for i in range(0, 10):
        try:
            print(data['data']['children'][i]['data']['title'])
        except:
            print('None')
            break
