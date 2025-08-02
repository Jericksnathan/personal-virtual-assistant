import os
from datetime import datetime

REMINDER_FILE = "data/reminders.txt"

def load_reminders():
    if not os.path.exists(REMINDER_FILE):
        return []
    with open(REMINDER_FILE, 'r') as f:
        lines = f.readlines()
        return [line.strip().split('|') for line in lines]

def save_reminders(reminders):
    with open(REMINDER_FILE, 'w') as f:
        for r in reminders:
            f.write('|'.join(r) + '\n')

def add_reminder():
    date = input("Enter reminder date (YYYY-MM-DD): ")
    try:
        datetime.strptime(date, '%Y-%m-%d')  # Validate format
    except ValueError:
        print("Invalid date format.")
        return

    note = input("Enter reminder note: ")
    reminders = load_reminders()
    reminders.append([date, note])
    save_reminders(reminders)
    print("Reminder added.")

def view_reminders():
    reminders = load_reminders()
    if not reminders:
        print("No reminders found.")
        return

    print("\n📝 Your Reminders:")
    for idx, (date, note) in enumerate(reminders, 1):
        print(f"{idx}. Date: {date}, Note: {note}")

def delete_reminder():
    reminders = load_reminders()
    view_reminders()
    if not reminders:
        return

    try:
        idx = int(input("Enter reminder number to delete: ")) - 1
        if 0 <= idx < len(reminders):
            removed = reminders.pop(idx)
            save_reminders(reminders)
            print(f"Deleted reminder: {removed}")
        else:
            print("Invalid number.")
    except ValueError:
        print("Please enter a valid number.")

def reminder_menu():
    while True:
        print("\n🔔 Reminder Manager")
        print("1. Add Reminder")
        print("2. View Reminders")
        print("3. Delete Reminder")
        print("4. Back to Main Menu")

        choice = input("Select: ")

        if choice == '1':
            add_reminder()
        elif choice == '2':
            view_reminders()
        elif choice == '3':
            delete_reminder()
        elif choice == '4':
            break
        else:
            print("Invalid choice.")
