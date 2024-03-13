import csv

# Read the stest.csv file
with open('stest.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    data = list(reader)

# Get the column F data
column_f_data = [row[5] for row in data]

# Find non-repeated data in column F
non_repeated_data = []
for item in column_f_data:
    if column_f_data.count(item) == 1:
        non_repeated_data.append(item)

# Write non-repeated data to data.csv
with open('data.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Non-Repeated Data'])  # Write header
    for item in non_repeated_data:
        writer.writerow([item])

print("Non-repeated data has been written to data.csv.")
