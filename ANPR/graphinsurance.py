import pandas as pd
import matplotlib.pyplot as plt
import datetime

# Load data from run.csv
run_df = pd.read_csv("run.csv", header=None, skiprows=1)

# Convert the "Insurance Upto" column (column F) to datetime format
run_df[5] = pd.to_datetime(run_df[5], format='%Y-%m-%d')  # Use the correct format here

# Get today's date
current_date = datetime.datetime.now().date()

# Calculate the number of vehicles with expired insurance and active insurance
count_expired_insurance = (run_df.iloc[:, 5].dt.date < current_date).sum()
count_active_insurance = len(run_df) - count_expired_insurance

# Plotting a bar graph
plt.bar(["Expired Insurance", "Active Insurance"], [count_expired_insurance, count_active_insurance], color=['red', 'lightgreen'])
plt.xlabel("Insurance Status")
plt.ylabel("Number of Vehicles")
plt.title(f"Insurance Status of Vehicles Running\nTotal Expired: {count_expired_insurance} | Total Active: {count_active_insurance}")
plt.show()
