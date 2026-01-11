with open("example.log", "r", encoding="utf-8", errors="ignore") as f:
    for line in f:
        print(line.strip())
