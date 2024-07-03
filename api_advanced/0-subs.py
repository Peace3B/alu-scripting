#!/usr/bin/python3
"""
Script that queries subscribers on a given Reddit subreddit.
"""

import requests
import sys

def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please pass a subreddit as an argument.")
    else:
        print("{:d}".format(number_of_subscribers(sys.argv[1])))
