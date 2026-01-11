# parse_nginx.py
# Parse Nginx page and extract information
import requests
from bs4 import BeautifulSoup

url = "http://localhost:8080"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

# Example: Print Page Title
print("Page Title:", end=" ")
print(soup.title.text)

# Example: Print All Links of the Page
print("All Links of the Page:")
for link in soup.find_all("a"):
    print(link.get("href"))

# Example: Print All Form Actions
print("Form Actions:")
for form in soup.find_all("form"):
    print(form.get("action"))
