import csv
import os

FILENAME = "expenses.csv"

def load_expenses():
    expenses = []
    if os.path.exists(FILENAME):
        with open(FILENAME, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                row['Amount'] = float(row['Amount'])
                expenses.append(row)
    return expenses

def save_expenses(expenses):
    with open(FILENAME, 'w', newline='') as csvfile:
        fieldnames = ['Date', 'Category', 'Amount']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for expense in expenses:
            writer.writerow(expense)

def add_expense(expenses):
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (e.g., Food, Transport): ")
    while True:
        try:
            amount = float(input("Enter amount: "))
            break
        except ValueError:
            print("Please enter a valid number for amount.")
    expenses.append({'Date': date, 'Category': category, 'Amount': amount})
    print("Expense added!")

def show_summary(expenses):
    total = sum(exp['Amount'] for exp in expenses)
    summary = {}
    for exp in expenses:
        summary[exp['Category']] = summary.get(exp['Category'], 0) + exp['Amount']

    print("\n--- Expense Summary ---")
    print(f"Total spent: ${total:.2f}")
    print("By category:")
    for cat, amt in summary.items():
        print(f"  {cat}: ${amt:.2f}")
    print("-----------------------\n")

def main():
    expenses = load_expenses()

    while True:
        print("Personal Expense Tracker")
        print("1. Add expense")
        print("2. Show summary")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_expense(expenses)
            save_expenses(expenses)
        elif choice == '2':
            show_summary(expenses)
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
