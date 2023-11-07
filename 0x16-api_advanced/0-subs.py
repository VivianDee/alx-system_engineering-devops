#!/usr/bin/python3
"""This script queries the Reddit API and returns the number of subscribers"""
import requests
import json


def number_of_subscribers(subreddit):
    """Gets the number of reddit subscribers"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    data = requests.get(url,
                        headers={
                            "User-Agent": "linux:0x16.api.advanced:v1.0.0"
                            }, allow_redirects=False)
    data = data.json()
    try:
        return data['data']['subscribers']
    except Exception:
        return 0
