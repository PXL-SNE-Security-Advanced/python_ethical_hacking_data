# whoami_example.py
import os
import subprocess

# Check which os is being used and run whoami accordingly

# Linux
if os.name == "posix":
    subprocess.run(["whoami"])

# Windows
# shell=True is needed on Windows to run built-in commands
if os.name == "nt":
    subprocess.run(["whoami"], shell=True)
