# 02_dataframe_example02.py
import pandas as pd

# Define a dictionary with digital forensic artifacts and their presence in different investigations
data = {
    'Investigation_1': [True, True, True, False, True, False],
    'Investigation_2': [True, False, True, True, True, True],
    'Investigation_3': [True, True, False, True, False, True],
    'Investigation_4': [False, True, True, True, True, True],
    'Investigation_5': [True, True, True, True, True, False]
}

# Create a DataFrame from the dictionary
forensic_df = pd.DataFrame(data, index=['System logs', 'Network traffic logs', 'File access logs', 'Registry entries', 'Browser history', 'Deleted files'])

# Display the DataFrame
print("Digital Forensic Artifacts:")
print(forensic_df)

'''
Digital Forensic Artifacts:
                      Investigation_1  Investigation_2  Investigation_3  Investigation_4  Investigation_5
System logs                      True             True             True            False             True
Network traffic logs             True            False             True             True             True
File access logs                 True             True            False             True             True
Registry entries                False             True             True             True             True
Browser history                  True             True            False             True             True
Deleted files                   False             True             True             True            False
'''