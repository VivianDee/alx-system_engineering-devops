#!/usr/bin/python3
"""The recurse Function"""
import requests
import json


def recurse(subreddit, hot_list=[], after="", count=0):
    """Returns titles of the hot posts in subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    data = requests.get(url,
                        headers={
                            "User-Agent": "linux:0x16.api.advanced:v1.0.0"
                            },
                        params={"after": after, "count": count},
                        allow_redirects=False
                        )
    data = data.json()
    try:
        children = data['data']['children']
        after = data['data']['after']
        count = data['data']['dist']
        for child in children:
            hot_list.append(child['data']['title'])

        if after:
            recurse(subreddit, hot_list, after, count)
        else:
            return hot_list
    except Exception:
        print("None")
