import csv
import os
from datetime import datetime

FILE_NAME = "expenses.csv"

def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount", "Description"])

def add_expense():
    category = input("Enter category (Food/Travel/Bills/Other): ").strip().capitalize()
    try:
        amount = float(input("Enter amount (PKR): "))
    except ValueError:
        print("Invalid amount! Please enter a number.\n")
        return
    desc = input("Enter short description: ").strip()
    date = datetime.now().strftime("%Y-%m-%d")

    with open(FILE_NAME, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, desc])
    print("Expense added successfully!\n")

def view_summary():
    if not os.path.exists(FILE_NAME):
        print("No records found.\n")
        return

    total = 0
    category_totals = {}

    with open(FILE_NAME, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            amt = float(row["Amount"])
            cat = row["Category"]
            total += amt
            category_totals[cat] = category_totals.get(cat, 0) + amt

    print("\n--- EXPENSE SUMMARY ---")
    for cat, amt in category_totals.items():
        print(f"{cat}: PKR {amt:.2f}")
    print(f"Total Spending: PKR {total:.2f}\n")

def main():
    initialize_file()
    while True:
        print("1. Add Expense | 2. View Summary | 3. Exit")
        choice = input("Choose an option: ").strip()
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_summary()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice!\n")

if __name__ == "__main__":
    main()
