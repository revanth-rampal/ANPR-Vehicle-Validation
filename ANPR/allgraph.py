import pandas as pd
import matplotlib.pyplot as plt
import datetime

# Load data from run.csv
run_df = pd.read_csv("run.csv", header=None, skiprows=1)

# Convert the "Fitness Upto" column (column E) to datetime format
run_df[4] = pd.to_datetime(run_df[4])  # Let pandas infer the format

# Convert the "Insurance Upto" column (column F) to datetime format
run_df[5] = pd.to_datetime(run_df[5])  # Let pandas infer the format

# Convert the "Pollution Cert Validity" column (column N) to datetime format
run_df[13] = pd.to_datetime(run_df[13])  # Let pandas infer the format

# Get today's date
current_date = datetime.datetime.now().date()

# Calculate the number of vehicles with expired fitness and valid fitness
count_expired_fitness = (run_df.iloc[:, 4].dt.date < current_date).sum()
count_valid_fitness = len(run_df) - count_expired_fitness

# Calculate the number of vehicles with expired insurance and active insurance
count_expired_insurance = (run_df.iloc[:, 5].dt.date < current_date).sum()
count_active_insurance = len(run_df) - count_expired_insurance

# Calculate the number of vehicles with expired pollution certificate and active pollution certificate
count_expired_pollution = (run_df.iloc[:, 13].dt.date < current_date).sum()
count_active_pollution = len(run_df) - count_expired_pollution

# Create subplots for multiple graphs
fig, axs = plt.subplots(2, 2, figsize=(12, 8))

# Line Plot for Blacklisted Cars
column_index = 2  # Index 2 corresponds to column C
column_data = run_df.iloc[1:, column_index]
column_counts = column_data.value_counts().sort_index()
axs[0, 0].plot(column_counts.index, column_counts.values, marker='o', linestyle='-')
axs[0, 0].set_xlabel("No of fines")
axs[0, 0].set_ylabel("Frequency")
axs[0, 0].set_title("Number of Blacklisted Cars Running")

# Bar Plot for Insurance Status
axs[0, 1].bar(["Expired Insurance", "Active Insurance"], [count_expired_insurance, count_active_insurance], color=['red', 'green'])
axs[0, 1].set_xlabel("Insurance Status")
axs[0, 1].set_ylabel("Number of Vehicles")
axs[0, 1].set_title(f"Insurance Status of Vehicles Running\nTotal Expired: {count_expired_insurance} | Total Active: {count_active_insurance}")

# Bar Plot for Fitness Status
axs[1, 0].bar(["Expired Fitness", "Valid Fitness"], [count_expired_fitness, count_valid_fitness], color=['red', 'green'])
axs[1, 0].set_xlabel("Fitness Status")
axs[1, 0].set_ylabel("Number of Vehicles")
axs[1, 0].set_title(f"Fitness of Vehicles Running\nTotal Expired: {count_expired_fitness} | Total Valid: {count_valid_fitness}")

# Pie Chart for Vehicle Status
status_counts = run_df[8].value_counts()
axs[1, 1].pie(status_counts, labels=status_counts.index, autopct='%1.1f%%', startangle=140, colors=['green', 'red'])
axs[1, 1].set_title(" Vehicle RC Status")
axs[1, 1].axis('equal')

# Adjust layout and show the combined plot
plt.tight_layout()
plt.show()
