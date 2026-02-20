"""
Program Name: Lab 6 - User Login
Author: Kaleb Quinn
Purpose: simple user login system.
Date: 2026-02-20
"""

def main():
    # usernames and passwords
    users = {
        "guest": "guest",
        "gwalters": "S3curePass!",
        "alice": "Alice123",
        "bob": "BobPassword"
    }

    username = input("Enter username: ")

    if username not in users:
        print("User not found. Exiting.")
        return

    password = input("Enter password: ")

    if password != users[username]:
        print("Access Denied.")
        return

    # security level
    if username == "guest":
        security_level = "Guest access"
    else:
        security_level = "Security Level 1"

    print(f"Welcome, {username}. You have {security_level}.")

if __name__ == "__main__":
    main()