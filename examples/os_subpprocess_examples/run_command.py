# run_command.py
import subprocess
import os

def run_command(cmd, use_shell=False):
    result = subprocess.run(cmd, shell=use_shell, capture_output=True, text=True)
    return result.stdout


# Example usage for Linux/Windows compatibility

# Linux
if os.name == "posix":
    print(run_command(["whoami"]))
    a
# Windows

if os.name == "nt":
    print(run_command(["whoami"], use_shell=True))
    
    