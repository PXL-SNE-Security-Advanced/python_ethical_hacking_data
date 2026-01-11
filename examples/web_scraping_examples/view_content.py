# view_content.py
# View HTML content of local Nginx server
import requests

url = "http://localhost:8080"
response = requests.get(url)
print(response.text)
