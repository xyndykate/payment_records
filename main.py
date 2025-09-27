
# Import necessary modules for file and CSV operations
import csv
import os

# Path to the CSV file where payment records are stored
CSV_FILE = r'C:\Users\ADMIN\OneDrive\Documents\g_xy\internet_subscription\records.csv'


# Save a payment record to the CSV file
def save_record(apartment, amount, date):
    # Ensure the folder for the CSV file exists
    os.makedirs(os.path.dirname(CSV_FILE), exist_ok=True)
    file_exists = os.path.isfile(CSV_FILE)
    # Open the CSV file in append mode
    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        # Write header if file is new
        if not file_exists:
            writer.writerow(['Apartment', 'Amount', 'Date'])  # header
        # Write the new record
        writer.writerow([apartment, amount, date])


# Print all payment records from the CSV file
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
        # Print table header
        print(f"{'Apartment':<10} {'Amount':<10} {'Date':<12}")
        print("-" * 32)
        # Print each record in formatted columns
        for row in records:
            print(f"{row['Apartment']:<10} {row['Amount']:<10} {row['Date']:<12}")


# Delete payment records for a given apartment number from the CSV file
def delete_record(apartment_number):
    # Check if the CSV file exists
    if not os.path.isfile(CSV_FILE):
        print("No records to delete.")
        return

    records = []  # List to hold records not being deleted
    deleted = False  # Flag to track if any record was deleted
    # Read all records from the CSV file
    with open(CSV_FILE, mode='r', newline='') as file:
        reader = csv.reader(file)
        header = next(reader, None)
        for row in reader:
            # Keep records that do not match the apartment number
            if row[0] != apartment_number:
                records.append(row)
            else:
                deleted = True

    # Write back only the records that were not deleted
    with open(CSV_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        if header:
            writer.writerow(header)
        writer.writerows(records)

    # Print result of deletion
    if deleted:
        print(f"Record(s) for Apartment {apartment_number} deleted.")
    else:
        print(f"No record found for Apartment {apartment_number}.")


# Prompt user for payment details and save the record
def record_payment():
    # Validate apartment number input
    while True:
        apartment_number = input("Enter apartment number (1-17): ")
        # Accept numbers 1-17 or codes like A1, B2, etc.
        if apartment_number.isdigit() and 1 <= int(apartment_number) <= 17:
            break
        elif (
            apartment_number.upper().startswith(("A", "B", "C", "D"))
            and apartment_number[1:].isdigit()
        ):
            break
        print("Invalid apartment number. Please enter a number between 1 and 17.")
    # Validate payment amount input
    while True:
        amount = input("Enter payment amount: ")
        if amount.isdigit() and int(amount) > 0:
            break
        print("Invalid amount. Please enter a positive number.")
    # Get payment date (no validation here, but could be added)
    date = input("Enter payment date (YYYY-MM-DD): ")
    # Save the record to the CSV file
    save_record(apartment_number, amount, date)
    print(f"Payment recorded for Apartment {apartment_number}: Amount {amount} on {date}")


# Main menu loop for user interaction
def main():
    while True:
        print("\n--- Internet Subscription Payment Records ---")
        print("1. Record a Payment")
        print("2. Print All Records")
        print("3. Delete a Record")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")
        # Handle user choice
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

# Entry point for the program
if __name__ == "__main__":
    main()