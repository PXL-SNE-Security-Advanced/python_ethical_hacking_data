# 05_plots_data01.py
import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a pandas DataFrame
df = pd.read_csv('forensic_artefacts_full.csv')

# Histogram for 'Size (KB)'
plt.figure(figsize=(10, 6))
plt.hist(df['Size (KB)'], bins=10, color='skyblue', edgecolor='black')
plt.title('Distribution of Sizes (KB)')
plt.xlabel('Size (KB)')
plt.ylabel('Frequency')
plt.grid(axis='y', alpha=0.75)
plt.savefig('histogram_size_kb.png')
plt.show()
plt.close()  # Close the figure to free memory


# Bar Chart for the frequency of each 'Type'
type_counts = df['Type'].value_counts()
plt.figure(figsize=(10, 6))
type_counts.plot(kind='bar', color='orange', edgecolor='black')
plt.title('Frequency of Each Type')
plt.xlabel('Type')
plt.ylabel('Frequency')
plt.xticks(rotation=45)
plt.grid(axis='y', alpha=0.75)
plt.savefig('bar_chart_type_frequency.png')
plt.show()
plt.close()


# Pie Chart for the proportion of each 'Type'
plt.figure(figsize=(8, 8))
df['Type'].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=140)
plt.title('Proportion of Each Type')
plt.ylabel('')  # Hide the 'Type' label on the y-axis
plt.savefig('pie_chart_type_proportion.png')
plt.show()
plt.close()
