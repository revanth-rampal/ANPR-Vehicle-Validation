import random
import csv
from datetime import date, timedelta

# Function to generate a random date
def random_date(start_date, end_date):
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return start_date + timedelta(days=random_days)

# List of Indian states (abbreviations)
indian_states = ["AP", "AR", "AS", "BR", "CG", "GA", "GJ", "HR", "HP", "JK", "JH", "KA",
                 "KL", "MP", "MH", "MN", "ML", "MZ", "NL", "OD", "PB", "RJ", "SK", "TN",
                 "TS", "TR", "UP", "UK", "WB"]

# Function to generate a random Indian car number plate
def generate_vehicle_number():
    state = random.choice(indian_states)
    district = str(random.randint(10, 99))
    letters = "".join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ", k=2))
    number = str(random.randint(1000, 9999))
    return f"{state} {district} {letters} {number}"

# Function to generate a random date in the future
def random_future_date():
    return random_date(date.today(), date.today() + timedelta(days=365*10))

# Function to generate a random insurance company name
def random_insurance_company():
    insurance_companies = ["ICICI LOMBARD", "New India Assurance", "United India Insurance",
                           "HDFC ERGO", "Bajaj Allianz", "Oriental Insurance", "Reliance General",
                           "Tata AIG", "SBI General", "Future Generali"]
    return random.choice(insurance_companies)

# Function to generate random car details
def generate_random_car_details():
    vehicle_number = generate_vehicle_number()
    blacklist_flag = random.choice(["yes", "no"])
    if blacklist_flag == "yes":
        num_fines = random.randint(1, 10)
    else:
        num_fines = 0
    color = random.choice(["Red", "Blue", "White", "Black", "Silver", "Green", "Yellow"])
    fitness_date = random_future_date()
    insurance_date = random_future_date()
    insurance_company = random_insurance_company()
    maker = random.choice(["HERO MOTOCORP LTD", "Maruti Suzuki", "Hyundai", "Tata Motors", "Honda", "Toyota"])
    rc_status = random.choice(["ACTIVE", "DEACTIVE"])
    registration_date = random_date(date(2010, 1, 1), date.today())
    rto = vehicle_number[:2]
    year_of_purchase = random.randint(2000, 2023)
    pollution_cert_validity = random_future_date()

    return [vehicle_number, blacklist_flag, num_fines, color, fitness_date, insurance_date,
            insurance_company, maker, rc_status, registration_date, rto, year_of_purchase,
            random.choice(["commercial", "personal"]), pollution_cert_validity]

# Generate random car details and write to CSV file
def generate_car_details_csv(file_name, num_entries):
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Vehicle Number", "Blacklist Flag", "No. of Fines", "Color", "Fitness Upto",
                         "Insurance Upto", "Insurance Comp", "Maker", "Rc Status", "Registration Date",
                         "RTO", "Year of Purchase", "Type of Car", "Pollution Cert Validity"])
        for _ in range(num_entries):
            writer.writerow(generate_random_car_details())

if __name__ == "__main__":
    file_name = "car_database.csv"
    num_entries =1000000 
    generate_car_details_csv(file_name, num_entries)
    print(f"CSV file '{file_name}' with {num_entries} random car details generated successfully.")


