import pandas as pd
import datetime

# Load data from run.csv
run_df = pd.read_csv("run.csv", header=None)

# Get current date
current_date = datetime.datetime.now().date()

# Select specific columns by indices (0-based indexing)
selected_columns = [0, 4, 5, 8, 13]

# Extract the selected columns
selected_data_df = run_df.iloc[:, selected_columns]

# Rename the columns
selected_data_df.columns = ["Vehicle Number", "Fitness", "Insurance", "Rc", "Pollution Cert Validity"]

# Check if the dates are expired or valid based on the current date
selected_data_df["Fitness"] = selected_data_df["Fitness"].apply(lambda x: "Expired" if pd.to_datetime(x).date() < current_date else "Valid")
selected_data_df["Insurance"] = selected_data_df["Insurance"].apply(lambda x: "Expired" if pd.to_datetime(x).date() < current_date else "Valid")
selected_data_df["Pollution Cert Validity"] = selected_data_df["Pollution Cert Validity"].apply(lambda x: "Expired" if pd.to_datetime(x).date() < current_date else "Valid")

# Save the selected and modified data to anprdoc.csv
selected_data_df.to_csv("anprdoc.csv", index=False)

print("Selected columns with date status saved to anprdoc.csv")
