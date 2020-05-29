#!/usr/bin/python3
"""
module to fetch
reddit api
subreddits
subscibres
"""


import requests


def number_of_subscribers(subreddit):
    """
    function to return number
    of subsciber of a giben
    subreddit
    """
    headers = {'user-agent': 'linux'}
    api = 'https://api.reddit.com/r/'
    data = requests.get(api + subreddit + '/about', headers=headers)
    res = data.json()
    try:
        res = res['data']['subscribers']
    except:
        res = 0
    return res
