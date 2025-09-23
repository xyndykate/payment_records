import csv
import os

CSV_FILE = r'C:\Users\ADMIN\OneDrive\Documents\g_xy\internet_subscription\records.csv'

def save_record(Apartment, amount, date):
    # Ensure the folder exists
    os.makedirs(os.path.dirname(CSV_FILE), exist_ok=True)
    file_exists = os.path.isfile(CSV_FILE)
    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(['Apartment', 'Amount', 'Date'])  # header
        writer.writerow([Apartment, amount, date])

def read_records():
    if not os.path.isfile(CSV_FILE):
        print('No records found.')
        return
    with open(CSV_FILE, mode='r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

def record_payment():
    apartment_number = input("Enter apartment number (1-17): ")
    amount = input("Enter payment amount: ")
    date = input("Enter payment date (YYYY-MM-DD): ")
    record = {
        "apartment": apartment_number,
        "amount": amount,
        "date": date
    }
    payment_records.append(record)
    notify_payment(record)
    # Save to CSV file for persistence
    save_record(apartment_number, amount, date)

def notify_payment(record):
    print(f"Payment recorded for Apartment {record['apartment']}: Amount {record['amount']} on {record['date']}")

def print_records():
    if not os.path.isfile(CSV_FILE):
        print("No payment records found.")
        return
    with open(CSV_FILE, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        records_found = False
        print("Payment Records:")
        for row in reader:
            records_found = True
            apartment = row.get('Apartment', '')
            amount = row.get('Amount', '')
            date = row.get('Date', '')
            print(f"Apartment {apartment}: Amount {amount} on {date}")
        if not records_found:
            print("No payment records found.")

def delete_record(apartment_number):
    # Read all records
    if not os.path.isfile(CSV_FILE):
        print("No records to delete.")
        return

    records = []
    deleted = False
    with open(CSV_FILE, mode='r', newline='') as file:
        reader = csv.reader(file)
        header = next(reader, None)
        for row in reader:
            if row[0] != apartment_number:
                records.append(row)
            else:
                deleted = True

    # Write back remaining records
    with open(CSV_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        if header:
            writer.writerow(header)
        writer.writerows(records)

    if deleted:
        print(f"Record(s) for Apartment {apartment_number} deleted.")
    else:
        print(f"No record found for Apartment {apartment_number}.")

# Internet Subscription Payment Records for 17 Apartments

# Data structure to hold payment records
payment_records = []

# Function to record a payment
def record_payment():
    apartment_number = input("Enter apartment number (1-17): ")
    amount = input("Enter payment amount: ")
    date = input("Enter payment date (YYYY-MM-DD): ")
    record = {
        "apartment": apartment_number,
        "amount": amount,
        "date": date
    }
    payment_records.append(record)
    notify_payment(record)
    # Save to CSV file for persistence
    save_record(apartment_number, amount, date)

# Function to notify when a payment is recorded
def notify_payment(record):
    print(f"Payment recorded for Apartment {record['apartment']}: Amount {record['amount']} on {record['date']}")

# Function to print all payment records
def print_records():
    if not os.path.isfile(CSV_FILE):
        print("No payment records found.")
        return
    with open(CSV_FILE, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        records_found = False
        print("Payment Records:")
        for row in reader:
            records_found = True
            apartment = row.get('Apartment', '')
            amount = row.get('Amount', '')
            date = row.get('Date', '')
            print(f"Apartment {apartment}: Amount {amount} on {date}")
        if not records_found:
            print("No payment records found.")

# Main menu loop
def main():
    while True:
        print("\n--- Internet Subscription Payment Records ---")
        print("1. Record a Payment")
        print("2. Print All Records")
        print("3. Delete a Record")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")
        if choice == "1":
            record_payment()
        elif choice == "2":
            print_records()
        elif choice == "3":
            apartment_number = input("Enter apartment number to delete: ")
            delete_record(apartment_number)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()