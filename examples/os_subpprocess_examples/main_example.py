# main_example.py
import os
import subprocess


def main():
    print("Directory:", os.getcwd())
    print(
        "User:",
        subprocess.run(["whoami"], shell=True, capture_output=True, text=True).stdout,
    )


if __name__ == "__main__":
    main()
