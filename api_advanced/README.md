# Reddit API Scripts

## Overview

This project consists of several Python scripts that interact with the Reddit API to fetch and analyze data from subreddits. The scripts demonstrate how to access various aspects of Reddit, such as retrieving subreddit information, listing top posts, and counting keyword occurrences in post titles.

## Scripts

### 0-subs.py

**Purpose**: Fetches the list of subscribed subreddits for the authenticated user
python3 0-subs.py

### 1-top_ten.py
Purpose: Retrieves the titles of the top ten hot posts from a given subreddit.
python3 1-top_ten.py <subreddit>

### 2-recurse.py
Purpose: Recursively fetches the hot posts from a given subreddit, handling pagination.
python3 2-recurse.py <subreddit>

### 3-count.py
Purpose: Counts occurrences of specified keywords in the titles of hot articles from a given subreddit.
python3 3-count.py <subreddit> '<list of keywords>'

