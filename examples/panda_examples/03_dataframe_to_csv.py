# 03_dataframe_to_csv.py
import pandas as pd

# Define the data as a 2-dimensional list
data = [
    ['System logs', True, 1000, 'txt'],
    ['Network traffic logs', True, 2500, 'pcap'],
    ['File access logs', False, 800, 'txt'],
    ['Registry entries', True, 1200, 'reg'],
    ['Browser history', True, 1500, 'html'],
    ['Deleted files', False, 2000, 'dat']
]

# Define column names
columns = ['Artifact', 'Found', 'Size (KB)', 'Type']

# Create a DataFrame from the 2-dimensional list and column names
forensic_df = pd.DataFrame(data, columns=columns)

# Display the DataFrame
print("Digital Forensic Artifacts:")
print(forensic_df)

# Specify the CSV file name
filename = 'forensic_artefacts.csv'

# Write the DataFrame to a CSV file
# index=False means do not write row indices (header)
forensic_df.to_csv(filename, index=False)

print(f'Data written to {filename}')