import requests

def fetch_posts():
    """
    Fetches data from JSONPlaceholder API and displays the first 3 posts.
    """
    # The free fake API for testing
    url = "https://jsonplaceholder.typicode.com/posts"
    
    print("Fetching data from JSONPlaceholder API...")
    
    try:
        # Send a GET request to the API
        response = requests.get(url, timeout=10)
        
        # Check if the request was successful (Status Code 200)
        if response.status_code == 200:
            data = response.json()
            
            print("Successfully fetched data!")
            print(f"Total posts fetched: {len(data)}")
            print("-" * 20)
            
            # Display the first 3 posts to keep the output clean
            print("First 3 posts:\n")
            for post in data[:3]:
                print(f"Post {post['id']}:")
                print(f"  ID: {post['id']}")
                print(f"  Title: {post['title']}")
                print(f"  Body: {post['body'][:100]}...") # Display first 100 chars of body
                print("-" * 20)
                
        else:
            # Handle non-200 status codes (e.g., 404, 500)
            print(f"Error fetching data: {response.status_code} - {response.text}")

    except requests.exceptions.RequestException as e:
        # Handle network errors (e.g., no internet connection)
        print(f"An error occurred while fetching data: {e}")

if __name__ == "__main__":
    fetch_posts()