# simple_get.py
# Simple GET request to local Nginx server

import requests

url = "http://localhost:8080"
response = requests.get(url)

print(response.status_code)
