import csv
import os

CSV_FILE = r'C:\Users\ADMIN\OneDrive\Documents\g_xy\internet_subscription\records.csv'

def save_record(apartment, amount, date):
    # Ensure the folder exists
    os.makedirs(os.path.dirname(CSV_FILE), exist_ok=True)
    file_exists = os.path.isfile(CSV_FILE)
    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(['Apartment', 'Amount', 'Date'])  # header
        writer.writerow([apartment, amount, date])

def print_records():
    if not os.path.isfile(CSV_FILE):
        print("No payment records found.")
        return
    with open(CSV_FILE, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        records = list(reader)
        if not records:
            print("No payment records found.")
            return
        print(f"{'Apartment':<10} {'Amount':<10} {'Date':<12}")
        print("-" * 32)
        for row in records:
            print(f"{row['Apartment']:<10} {row['Amount']:<10} {row['Date']:<12}")

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

def record_payment():
    while True:
        apartment_number = input("Enter apartment number (1-17): ")
        if apartment_number.isdigit() and 1 <= int(apartment_number) <= 17:
            break
        print("Invalid apartment number. Please enter a number between 1 and 17.")
    while True:
        amount = input("Enter payment amount: ")
        if amount.isdigit() and int(amount) > 0:
            break
        print("Invalid amount. Please enter a positive number.")
    date = input("Enter payment date (YYYY-MM-DD): ")
    save_record(apartment_number, amount, date)
    print(f"Payment recorded for Apartment {apartment_number}: Amount {amount} on {date}")

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