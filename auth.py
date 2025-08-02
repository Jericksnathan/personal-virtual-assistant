# auth.py
import os

DATA_PATH = "data/users.txt"

def signup():
    username = input("Enter new username: ")
    password = input("Enter new password: ")

    if not os.path.exists(DATA_PATH):
        open(DATA_PATH, 'w').close()

    with open(DATA_PATH, 'r') as f:
        users = f.readlines()
        for user in users:
            if user.split(',')[0] == username:
                print("Username already exists!")
                return False

    with open(DATA_PATH, 'a') as f:
        f.write(f"{username},{password}\n")
    print("Signup successful!")
    return True


def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    if not os.path.exists(DATA_PATH):
        print("No users found. Please sign up first.")
        return False

    with open(DATA_PATH, 'r') as f:
        users = f.readlines()
        for user in users:
            u, p = user.strip().split(',')
            if username == u and password == p:
                print("Login successful!")
                return username
                 
            
    print("Invalid credentials.")
    return False
