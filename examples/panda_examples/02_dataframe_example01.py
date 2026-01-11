# 02_dataframe_example01.py
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

'''
Digital Forensic Artifacts:
               Artifact  Found  Size (KB)  Type
0           System logs   True       1000   txt
1  Network traffic logs   True       2500  pcap
2      File access logs  False        800   txt
3      Registry entries   True       1200   reg
4       Browser history   True       1500  html
5         Deleted files  False       2000   dat
'''