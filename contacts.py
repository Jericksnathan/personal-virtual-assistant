import os

CONTACTS_FILE = "data/contacts.txt"

def load_contacts():
    if not os.path.exists(CONTACTS_FILE):
        return []
    with open(CONTACTS_FILE, 'r') as f:
        lines = f.readlines()
        return [line.strip().split(',') for line in lines]

def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as f:
        for contact in contacts:
            f.write(','.join(contact) + '\n')

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")

    contacts = load_contacts()
    contacts.append([name, phone, email])
    save_contacts(contacts)
    print("Contact added successfully.")

def view_contacts():
    contacts = load_contacts()
    if not contacts:
        print("No contacts found.")
        return
    print("\nYour Contacts:")
    for idx, (name, phone, email) in enumerate(contacts, 1):
        print(f"{idx}. Name: {name}, Phone: {phone}, Email: {email}")

def search_contact():
    search = input("Enter name to search: ")
    contacts = load_contacts()
    found = False
    for name, phone, email in contacts:
        if search.lower() in name.lower():
            print(f"Found - Name: {name}, Phone: {phone}, Email: {email}")
            found = True
    if not found:
        print("Contact not found.")

def delete_contact():
    name = input("Enter the name of contact to delete: ")
    contacts = load_contacts()
    new_contacts = [c for c in contacts if c[0].lower() != name.lower()]
    if len(new_contacts) == len(contacts):
        print("No contact found to delete.")
    else:
        save_contacts(new_contacts)
        print("Contact deleted successfully.")

def contacts():
    while True:
        print("\n📞 Contact Manager")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Back to Main Menu")

        choice = input("Select: ")
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            break
        else:
            print("Invalid choice.")
