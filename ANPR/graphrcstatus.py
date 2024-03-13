import pandas as pd
import matplotlib.pyplot as plt

# Load data from run.csv
run_df = pd.read_csv("run.csv", header=None, skiprows=1)

# Count the occurrences of each vehicle status in column I
status_counts = run_df[8].value_counts()

# Create a pie chart
plt.figure(figsize=(6, 6))
plt.pie(status_counts, labels=status_counts.index, autopct='%1.1f%%', startangle=140, colors=['green', 'red'])
plt.title("Vehicle RC Status ")
plt.axis('equal')  # Equal aspect ratio ensures that the pie chart is circular.
plt.show()
