import pandas as pd

# Load data from details.xlsx starting from row A2
details_df = pd.read_excel("details.xlsx", header=None, skiprows=1)

# Load data from data.csv starting from row A3
data_df = pd.read_csv("data.csv", header=None, skiprows=2)

# Specify the column index for matching values in details.xlsx
details_column_index = 0  # Assuming it's the first column

# Specify the column index for matching values in data.csv
data_column_index = 0  # Assuming it's the first column

# Extract the values for comparison
details_values = details_df.iloc[:, details_column_index].tolist()
data_values = data_df.iloc[:, data_column_index].tolist()

# Find matching values
matching_values = set(details_values).intersection(data_values)

# Filter details dataframe for matching values
matching_details_df = details_df[details_df.iloc[:, details_column_index].isin(matching_values)]

# Save matching values and all columns from details.xlsx to run.csv
matching_details_df.to_csv("run.csv", index=False, header=False)  # Exclude header

print("Matching data and all columns from details.xlsx saved to run.csv")
