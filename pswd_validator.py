# Codemy.com - Instructor John Elder

# pswd_validator.py

# Modified instructors code to be more Pythonic and readable

import os
import string

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def wants_to_quit(text):
    return text.strip().lower() in ("q", "quit", "exit")

def validate_password(password):
    """ Return True if password meets all rules, else False."""
    errors = []

    if len(password) < 8:
        errors.append("Password must be at least 8 characters long.")

    if not any(char.isdigit() for char in password):
        errors.append("Password must contain at least one digit (0-9).")

    if not any(char.isupper() for char in password):
        errors.append("Password must contain at least one uppercase letter (A-Z).")
            
    if not any(char.islower() for char in password):
        errors.append("Password must contain at least one lowercase letter (a-z).")

    if not any(char in string.punctuation for char in password):
        errors.append("Must contain at least one special character (!, @, #, $, etc.)")
            
    return errors

def show_rules():
    print("Password Rules:")
    print("1. Must be at least 8 characters long.")
    print("2. Must contain at least one digit (0-9).")
    print("3. Must contain at least one lowercase letter (a-z).")
    print("4. Must contain at least one uppercase letter (A-Z).")
    print("5. Must contain at least one special character (!, @, #, $, etc.)")
    print("\nType 'q' at any time to quit.\n")

def main():
    while True:
        clear_screen()
        show_rules()
    
        pwd = input("Enter a password to validate: ")

        if wants_to_quit(pwd):
            clear_screen()
            print("Goodbye !!")
            break

        errors = validate_password(pwd)

        if not errors:
            print("✅ Password is strong!")
        else:
            print("❌ Password is NOT valid. Issues found:")
            for error in errors:
                print(f"   - {error}")

        again = input("Would you like to check another password? (y/n): ").strip().lower()

        if wants_to_quit(again) or again.strip().lower() != "y":
            clear_screen()
            print("Goodbye !!")
            break

if __name__ == "__main__":
    main()