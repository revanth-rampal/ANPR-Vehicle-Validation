import pandas as pd
import matplotlib.pyplot as plt
import datetime

# Load data from run.csv
run_df = pd.read_csv("run.csv", header=None, skiprows=1)

# Convert the "Fitness Upto" column (column E) to datetime format
run_df[4] = pd.to_datetime(run_df[4], format='%Y-%m-%d')  # Use the correct format here

# Get today's date
current_date = datetime.datetime.now().date()

# Calculate the number of vehicles with expired fitness and valid fitness
count_expired_fitness = (run_df.iloc[:, 4].dt.date < current_date).sum()
count_valid_fitness = len(run_df) - count_expired_fitness

# Plotting a bar graph
plt.bar(["Expired Fitness", "Valid Fitness"], [count_expired_fitness, count_valid_fitness], color=['red', 'lightgreen'])
plt.xlabel("Fitness Status")
plt.ylabel("Number of Vehicles")
plt.title(f"Fitness of Vehicles Running\nTotal Expired: {count_expired_fitness} | Total Valid: {count_valid_fitness}")
plt.show()
