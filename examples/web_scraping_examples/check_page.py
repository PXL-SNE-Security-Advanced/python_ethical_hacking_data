# check_page.py
# Function to check if a page exists
import requests

def check_page(url):
    r = requests.get(url)
    return r.status_code

# Example usage
print("Checking login page status codes:")
print(check_page("http://localhost:8080/login"))

print("Checking index page status codes:")
print(check_page("http://localhost:8080/index.html"))