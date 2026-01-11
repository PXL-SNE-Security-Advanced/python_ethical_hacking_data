# 04_analyse_data01.py
import pandas as pd

forensic_df = pd.read_csv('forensic_artefacts_full.csv')

# Display the DataFrame
print("\nDigital Forensic Artifacts head(2):\n")
print(forensic_df.head(2))

print("\nDigital Forensic Artifacts tail:\n")

print(forensic_df.tail(4))

print("\nDigital Forensic Artifacts Info:\n")

print(forensic_df.info())