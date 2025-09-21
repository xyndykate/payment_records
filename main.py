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

# Function to notify when a payment is recorded
def notify_payment(record):
    print(f"Payment recorded for Apartment {record['apartment']}: Amount {record['amount']} on {record['date']}")

# Function to print all payment records
def print_records():
    if not payment_records:
        print("No payment records found.")
    else:
        print("Payment Records:")
        for record in payment_records:
            print(f"Apartment {record['apartment']}: Amount {record['amount']} on {record['date']}")

# Main menu loop
def main():
    while True:
        print("\n--- Internet Subscription Payment Records ---")
        print("1. Record a Payment")
        print("2. Print All Records")
        print("3. Exit")
        choice = input("Choose an option (1-3): ")
        if choice == "1":
            record_payment()
        elif choice == "2":
            print_records()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()