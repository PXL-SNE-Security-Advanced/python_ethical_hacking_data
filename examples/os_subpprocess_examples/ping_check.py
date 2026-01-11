# ping_check.py
import subprocess
import os

host = "8.8.8.8"


# Linux
if os.name == "posix":
    subprocess.run(["ping", "-c", "2", host])

# Windows
if os.name == "nt":
    subprocess.run(["ping", "-n", "2", host], shell=True)