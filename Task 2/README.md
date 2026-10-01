# Task 2: Fetching Data using the `requests` Library

## 📌 Objective
This task demonstrates how to interact with external APIs using Python's `requests` library. We use the JSONPlaceholder API, which is a free fake API for testing and prototyping.

## 🛠️ How to Run
1. Ensure you have the `requests` library installed (`pip install requests`).
2. Run the script using: `python task2_api_requests.py`

## 📸 Screenshots

### Code in VS Code
![VS Code Screenshot](PASTE_YOUR_CODE_SCREENSHOT_LINK_HERE)

### Terminal Output
![Terminal Output](PASTE_YOUR_OUTPUT_SCREENSHOT_LINK_HERE)

## 📖 Explanation of the Code
* **API Request:** The script uses `requests.get()` to send an HTTP GET request to the JSONPlaceholder `/posts` endpoint.
* **Status Code Check:** It checks if `response.status_code == 200` to verify the request was successful.
* **Data Parsing:** The `response.json()` method is used to convert the JSON response into a Python list of dictionaries.
* **Data Display:** A `for` loop iterates through the first 3 items in the list and prints the `id`, `title`, and `body` of each post.
* **Exception Handling:** A `try-except` block is used to catch `requests.exceptions.RequestException`, which handles network errors like timeouts or no internet connection.

## 💡 Insights/Learnings
* Gained hands-on experience in consuming REST APIs using Python.
* Learned how to parse JSON responses into usable Python data structures.
* Understood the importance of checking HTTP status codes and handling network exceptions gracefully.
