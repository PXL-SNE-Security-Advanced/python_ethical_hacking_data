# count_failed.py
count = 0

with open("example.log", "r", encoding="utf-8", errors="ignore") as f:
    for line in f:
        if "failed" in line.lower():
            count += 1

print("Lines containing 'failed':", count)
