# main.py
from auth import signup, login
from notes import notes
from calculator import calculator
from contacts import contacts
from expenses import expenses_menu
from reminders import reminder_menu
from password_gen import generate_password







def main():
    print("\nWelcome to Your Personal Virtual Assistant\n")
    while True:
        print("\n1. Signup")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            signup()
        elif choice == '2':
            username = login()
            if username:
                launch_assistant(username)
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

def launch_assistant(username):
    while True:
        print("\n📘 Assistant Menu")
        print("1. Notes")
        print("2. Calculator")
        print("3. Contacts")
        print("4. Reminders")
        print("5. Expenses")
        print("6. Password Generator")
        print("7. Logout")

        choice = input("Select: ")

        if choice == '1':
              notes(username)
        elif choice == '2':
              calculator()
        elif choice == '3':
              contacts()
        elif choice == '4':
             reminder_menu()
        elif choice == '5':
             expenses_menu()
        elif choice == '6':
             generate_password()
        elif choice == '7':
            print("Logged out.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
