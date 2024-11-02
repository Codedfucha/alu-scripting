#!/usr/bin/python3
"""
This script retrieves the titles of the first 10 hot posts for a given subreddit.
"""

import requests

def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent":"my_reddit_bot/0.1"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        for post in posts[:10]:  # Get only the first 10 posts
            print(post['data']['title'])
    else:
        print("None")  # Handle invalid subreddit case
