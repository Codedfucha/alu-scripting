#!/usr/bin/python3
""" This module defines a function to get the number of subscribers for a subreddit.""" 
import requests

def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers for a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'my-app/0.0.1'}
    
    response = requests.get(url, headers=headers, allow_redirects=False)
   
   if response.status_code == 200:
        data = response.json()
        return data.get("data", {}).get("subscribers", 0)
    else:
        return 0
