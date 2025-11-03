import glob
import pandas as pd

# Use glob to get all CSV files in the 'data' folder
csv_files = glob.glob("data/*.csv")

# Read and combine them
dataframes = [pd.read_csv(file) for file in csv_files]

# Merge into one DataFrame
merged_df = pd.concat(dataframes, ignore_index=True)

# Show first few rows
print(merged_df.head())