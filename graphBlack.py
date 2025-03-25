import pandas as pd
import matplotlib.pyplot as plt

# Load data from run.csv
run_df = pd.read_csv("run.csv")

# Specify the column index (3rd column since indexing starts from 0) and skip the header (start from row 1)
column_index = 2  # Index 2 corresponds to column C
column_data = run_df.iloc[1:, column_index]

# Calculate the frequency of each value in the column
column_counts = column_data.value_counts()

# Sort the counts by index
column_counts = column_counts.sort_index()

# Create the line graph
plt.plot(column_counts.index, column_counts.values, marker='o', linestyle='-')

# Add labels and title
plt.xlabel("No of fines")
plt.ylabel("Frequency")
plt.title("Number of Blacklisted Cars Running")

# Show the plot
plt.grid(False)
plt.show()
