#!/usr/bin/python3
"""top_ten Function"""
import requests
import json


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    data = requests.get(url,
                        headers={
                            "User-Agent": "linux:0x16.api.advanced:v1.0.0"
                            },
                        params={"limit": 10}, allow_redirects=False
                        )
    data = data.json()
    try:
        children = data['data']['children']
        for child in children:
            print(child['data']['title'])
    except Exception:
        print("None")
