import requests

def fetch_hot_articles(subreddit, after=None):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {'after': after}  # Add after parameter for pagination
    headers = {'User-Agent': 'Mozilla/5.0'}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code != 200:
        print("Error fetching data:", response.text)
        return None

    return response.json()

def count_words(subreddit, word_list):
    word_count = {word.lower(): 0 for word in word_list}  # Initialize counts
    after = None

    def recurse():
        nonlocal after
        data = fetch_hot_articles(subreddit, after)

        if not data or 'data' not in data:
            print("Invalid subreddit or error in request.")
            return

        articles = data['data']['children']
        after = data['data'].get('after')

        for article in articles:
            title = article['data']['title']
            title_words = title.lower().split()

            for word in word_count.keys():
                word_count[word] += title_words.count(word)

        if after:
            recurse()  # Recursive call for pagination

    recurse()

    # Prepare results for printing
    results = {word: count for word, count in word_count.items() if count > 0}
    sorted_results = sorted(results.items(), key=lambda x: (-x[1], x[0]))

    for word, count in sorted_results:
        print(f"{word}: {count}")
