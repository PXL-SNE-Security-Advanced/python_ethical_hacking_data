# check_file_access.py
import os

file_path = "test.txt"

if os.access(file_path, os.R_OK):
    print("Readable")

if os.access(file_path, os.W_OK):
    print("Writable")
