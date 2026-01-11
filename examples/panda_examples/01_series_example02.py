# 02_series_forensic_artifacts.py
# Series of Forensic Artifacts
import pandas as pd

artifacts = [
    "System logs",
    "Network traffic logs",
    "File access logs",
    "Registry entries",
    "Browser history",
    "Deleted files",
]

# Create a Pandas Series from the list
artifacts_series = pd.Series(artifacts)

# Display the Series
print("Digital Artifacts:")
print(artifacts_series)
