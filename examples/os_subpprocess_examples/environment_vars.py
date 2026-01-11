# environment_vars.py
import os

# Get specific variable
print(os.environ.get("HOME"))  # Linux
print(os.environ.get("PATH"))  # Windows
