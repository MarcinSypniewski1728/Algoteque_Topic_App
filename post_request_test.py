# File to test error handling and logging.

import requests

# Define the URL of the Flask app
URL = "http://127.0.0.1:5000/build_quote"
URL_BAD = "http://127.0.0.1:5000/bad_path"

# Define the JSON payload
data = {
    "topics": {
        "reading": 20,
        "math": 50,
        "science": 30,
        "history": 15,
        "art": 10
    }
}

data_empty = {}

# Send the POST request
response = requests.post(URL, json=data)
response_empty = requests.post(URL, json=data_empty)
response_bad = requests.post(URL_BAD, json=data)

# Print the response status code
print(f"Status Code: {response.status_code}")
print(f"Status Code: {response_empty.status_code}")
print(f"Status Code: {response_bad.status_code}")
