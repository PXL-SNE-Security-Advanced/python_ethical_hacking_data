# base64_example.py
import base64

text = "admin:password123"
encoded = base64.b64encode(text.encode()).decode()
print("Encoded:", encoded)

decoded = base64.b64decode(encoded).decode()
print("Decoded:", decoded)
