import os
from datetime import datetime

EXPENSES_FILE = "data/expenses.txt"

def load_expenses():
    if not os.path.exists(EXPENSES_FILE):
        return []
    with open(EXPENSES_FILE, 'r') as f:
        lines = f.readlines()
        return [line.strip().split(',') for line in lines]

def save_expenses(expenses):
    with open(EXPENSES_FILE, 'w') as f:
        for expense in expenses:
            f.write(','.join(expense) + '\n')

def add_expense():
    date = input("Enter date (YYYY-MM-DD) or press Enter for today: ")
    if not date:
        date = datetime.today().strftime('%Y-%m-%d')

    category = input("Enter category (e.g., Food, Travel, Bills): ")
    amount = input("Enter amount: ")
    description = input("Enter description: ")

    expenses = load_expenses()
    expenses.append([date, category, amount, description])
    save_expenses(expenses)
    print("Expense added successfully.")

def view_expenses():
    expenses = load_expenses()
    if not expenses:
        print("No expenses recorded.")
        return
    print("\n📒 Your Expenses:")
    for idx, (date, category, amount, description) in enumerate(expenses, 1):
        print(f"{idx}. Date: {date}, Category: {category}, Amount: ₹{amount}, Description: {description}")

def delete_expense():
    expenses = load_expenses()
    view_expenses()
    try:
        idx = int(input("Enter the expense number to delete: ")) - 1
        if 0 <= idx < len(expenses):
            removed = expenses.pop(idx)
            save_expenses(expenses)
            print(f"Deleted expense: {removed}")
        else:
            print("Invalid number.")
    except ValueError:
        print("Please enter a valid number.")

def show_summary():
    expenses = load_expenses()
    if not expenses:
        print("No expenses to summarize.")
        return

    total = 0
    category_totals = {}

    for date, category, amount, description in expenses:
        amt = float(amount)
        total += amt
        category_totals[category] = category_totals.get(category, 0) + amt

    print(f"\n💰 Total Spent: ₹{total}")
    print("📊 Breakdown by Category:")
    for cat, amt in category_totals.items():
        print(f"  - {cat}: ₹{amt}")

def expenses_menu():
    while True:
        print("\n💼 Expense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Summary")
        print("5. Back to Main Menu")

        choice = input("Select: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            delete_expense()
        elif choice == '4':
            show_summary()
        elif choice == '5':
            break
        else:
            print("Invalid choice.")
