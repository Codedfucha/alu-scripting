#!/usr/bin/python3
"""
This script retrieves the number of subscribers for a given subreddit using the Reddit API.
"""

import os
import requests
from dotenv import load_dotenv
import sys

# Load environment variables from .env file
load_dotenv()
REDDIT_CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
REDDIT_CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET")
REDDIT_USER_AGENT = os.getenv("REDDIT_USER_AGENT")

def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a subreddit.
    
    Args:
        subreddit (str): The name of the subreddit to check.
        
    Returns:
        int or None: The number of subscribers if successful, None otherwise.
    """
    # URL to get subreddit data
    url = f"https://oauth.reddit.com/r/{subreddit}/about.json"
    
    # Set up authentication for obtaining access token
    auth = requests.auth.HTTPBasicAuth(REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET)
    headers = {"User-Agent": REDDIT_USER_AGENT}

    try:
        # Obtain access token
        token_response = requests.post(
            "https://www.reddit.com/api/v1/access_token",
            auth=auth,
            data={"grant_type": "client_credentials"},
            headers=headers
        )
        token_response.raise_for_status()  # Raise error for bad responses

        # Extract access token and set authorization header
        access_token = token_response.json().get("access_token")
        headers["Authorization"] = f"bearer {access_token}"

        # Make request to get subreddit info
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise error for bad responses

        # Parse and return subscriber count
        result = response.json()
        subscriber_count = result["data"]["subscribers"]
        return subscriber_count

    except requests.exceptions.HTTPError as http_err:
        # Specific error for a nonexistent subreddit (404)
        if response.status_code == 404:
            print(f"Error: Subreddit '{subreddit}' does not exist.")
        else:
            print(f"HTTP error occurred: {http_err}")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    # Handle command-line input
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        subscribers = number_of_subscribers(subreddit)
        if subscribers is not None:
            print(f"Subscribers in '{subreddit}': {subscribers:,}")
        else:
            print(f"Unable to retrieve subscriber count for '{subreddit}'.")

