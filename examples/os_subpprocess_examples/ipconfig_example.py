# ipconfig_example.py
import os
import subprocess

# Check which os is being used and run whoami accordingly


# Linux
if os.name == "posix":
    subprocess.run(["ip", "addr"])

# Windows
if os.name == "nt":
    subprocess.run(["ipconfig"], shell=True)