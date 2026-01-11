# hash_string.py
import hashlib

text = "hello".encode()
print(hashlib.sha256(text).hexdigest())
