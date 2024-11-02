import requests

def recurse(subreddit, hot_list=[]):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        "User-Agent": "script:my_reddit_bot:v1.0 (by /u/beast-beat-20)"
    }
    
    # Make the API request
    response = requests.get(url, headers=headers)
    
    # Step 1: Check if the response status code is 200 (success)
    if response.status_code == 404:
        print("Invalid subreddit.")
        return None
    elif response.status_code != 200:
        print(f"Error: Received status code {response.status_code}")
        print("Response Text:", response.text)  # This will print the full response content
        return None

    # Step 2: Try to parse the JSON response and print it
    try:
        data = response.json()
        print("Response JSON:", data)  # This shows the complete JSON response from the API for inspection

        # Step 3: Check if the expected data exists in the response
        articles = data['data']['children'] if 'data' in data and 'children' in data['data'] else None
        
        if not articles:
            print("No articles found.")
            return None

        # Extract titles and add to hot_list
        for article in articles:
            hot_list.append(article['data']['title'])
        
        # Recursively request the next page if 'after' exists
        if data['data']['after']:
            return recurse(subreddit, hot_list)
        
    except Exception as e:
        print(f"Error processing response: {e}")
        return None

    return hot_list





        








        




        











    


    


    





    








        
        







        



 
        
   
     


