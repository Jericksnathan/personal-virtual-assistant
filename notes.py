# notes.py
import os

NOTES_FILE = "data/notes.txt"
def notes(username):
    while True:
        print("\n📝 Notes Menu")
        print("1. Add Note")
        print("2. View Notes")
        print("3. Delete Note")
        print("4. Back")

        choice = input("Choose: ")

        if choice == '1':
            add_note(username)
        elif choice == '2':
            view_notes(username)
        elif choice == '3':
            delete_note(username)
        elif choice == '4':
            break
        else:
            print("Invalid option.")



def add_note(username):
    note = input("Enter your note: ")
    with open(NOTES_FILE, 'a') as f:
        f.write(f"{username}:{note}\n")
    print("Note saved!")

def view_notes(username):
    if not os.path.exists(NOTES_FILE):
        print("No notes found.")
        return
    
    with open(NOTES_FILE, 'r') as f:
        notes = f.readlines()
        user_notes = [n.strip().split(":", 1)[1] for n in notes if n.startswith(f"{username}:")]

    if user_notes:
        print("\nYour Notes:")
        for i, note in enumerate(user_notes, 1):
            print(f"{i}. {note}")
    else:
        print("You have no notes.")

def delete_note(username):
    if not os.path.exists(NOTES_FILE):
        print("No notes to delete.")
        return

    with open(NOTES_FILE, 'r') as f:
        notes = f.readlines()

    user_notes = [n for n in notes if n.startswith(f"{username}:")]

    if not user_notes:
        print("You have no notes to delete.")
        return

    print("\nYour Notes:")
    for i, note in enumerate(user_notes, 1):
        print(f"{i}. {note.strip().split(':', 1)[1]}")

    try:
        index = int(input("Enter the note number to delete: ")) - 1
        if 0 <= index < len(user_notes):
            to_delete = user_notes[index]
            notes.remove(to_delete)

            with open(NOTES_FILE, 'w') as f:
                f.writelines(notes)

            print("Note deleted!")
        else:
            print("Invalid selection.")
    except ValueError:
        print("Enter a valid number.")

