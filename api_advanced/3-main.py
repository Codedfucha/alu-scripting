#!/usr/bin/python3
"""
3-main
"""
import sys

# Import the function from 3-count.py
if __name__ == '__main__':
    count_words = __import__('3-count').count_words

    # Check that at least a subreddit and one keyword are provided
    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".format(sys.argv[0]))
    else:
        result = count_words(sys.argv[1], [x for x in sys.argv[2].split()])
