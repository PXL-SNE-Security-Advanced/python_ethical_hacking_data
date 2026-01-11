# 02_dataframe_example03.py
import pandas as pd

# Define the column names (investigation names)
columns = ['Investigation_1', 'Investigation_2', 'Investigation_3', 'Investigation_4', 'Investigation_5']

# Define the row names (digital forensic artifacts)
artifacts = ['System logs', 'Network traffic logs', 'File access logs', 'Registry entries', 'Browser history', 'Deleted files']

# Define the presence of each artifact in each investigation
data = [
    [True, True, True, False, True],
    [True, False, True, True, True],
    [True, True, False, True, False],
    [False, True, True, True, True],
    [True, True, False, True, True],
    [False, True, True, True, False]
]

# Create a DataFrame using the defined columns, rows, and data
forensic_df = pd.DataFrame(data, index=artifacts, columns=columns)

# Display the DataFrame
print("Digital Forensic Artifacts:")
print(forensic_df)

'''
Digital Forensic Artifacts:
                      Investigation_1  Investigation_2  Investigation_3  Investigation_4  Investigation_5
System logs                      True             True             True            False             True
Network traffic logs             True            False             True             True             True
File access logs                 True             True            False             True            False
Registry entries                False             True             True             True             True
Browser history                  True             True            False             True             True
Deleted files                   False             True             True             True            Fals
'''