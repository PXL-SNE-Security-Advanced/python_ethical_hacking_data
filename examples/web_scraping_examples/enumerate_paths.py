# enumerate_paths.py
import requests

paths = ["/", "/login", "/admin", "/test", "/index.html"]

for path in paths:
    url = "http://localhost:8080" + path
    r = requests.get(url)
    print(path, r.status_code)
