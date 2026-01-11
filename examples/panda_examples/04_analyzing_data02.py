# 04_analyse_data02.py
import pandas as pd

# Load the CSV file into a pandas DataFrame
df = pd.read_csv('forensic_artefacts_full.csv')

# Calculate total entries
total_entries = len(df)

# Find the most frequent 'Type'
most_frequent_type = df['Type'].mode()[0]

# Calculate the number of unique 'Type' values
number_of_unique_types = df['Type'].nunique()

# Find the maximum 'Size (KB)'
max_size_kb = df['Size (KB)'].max()

# Find the minimum 'Size (KB)'
min_size_kb = df['Size (KB)'].min()

# Print the analysis results
print(f"Total Entries: {total_entries}")
print(f"Most Frequent Type: {most_frequent_type}")
print(f"Number of Unique Types: {number_of_unique_types}")
print(f"Maximum Size (KB): {max_size_kb} KB")
print(f"Minimum Size (KB): {min_size_kb} KB")

# Total Entries: 6
# Most Frequent Type: txt
# Number of Unique Types: 5
# Maximum Size (KB): 2500 KB
# Minimum Size (KB): 800 KB