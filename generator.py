# Codemy.com - Instructor John Elder

# generator.py : password generator

# Modified instructors code to be more Pythonic and readable

# Import modules
import random
import string
import os

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

def validate_flow():
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

# Prompt the user
def password_generator():
    SAFE_SYMBOLS = "!@#$%^*_-+=?"

    # MAIN INPUT LOOP

    while True:
        clear_screen()
        print("=== Password Generator ===")
        print("Type 'q' at any time to quit.\n")

        # Ask for length

        length_input = input("Enter desired password length (minimum 8): ").strip()

        # Allow quitting

        if wants_to_quit(length_input):
            return
        
        # Validate length input

        if not length_input.isdigit():
            print("Length must be a number.")
            input("Press Enter to continue...")
            continue  # Stay inside generator, ask again

        length = int(length_input)

        # Validate minimum length

        if length < 8:
            print("Password length must be at least 8.")
            input("Press Enter to continue...")
            continue  # Stay inside generator, ask again

        if length > 64:
            print("Password length must not exceed 64 characters.")
            input("Press Enter to try again...")
            continue  # Stay inside generator, ask again

        # Ask how many uppercase letters
        while True:
            upper_input = input("How many uppercase letters? (minimum 1): ").strip()

            if wants_to_quit(upper_input):
                return
            
            if not upper_input.isdigit():
                print("Please enter a number.")
                input("Press Enter to try again...")
                continue

            upper_count = int(upper_input)

            if upper_count < 1:
                print("You must include at least 1 uppercase letter.")
                input("Press Enter to try again...")
                continue
            
            break

        # Ask how many lowercase letters
        while True:
            lower_input = input("How many lowercase letters? (minimum 1): ").strip()

            if wants_to_quit(lower_input):
                return
            
            if not lower_input.isdigit():
                print("Please enter a number.")
                input("Press Enter to try again...")
                continue

            lower_count = int(lower_input)

            if lower_count < 1:
                print("You must include at least 1 lowercase letter.")
                input("Press Enter to try again...")
                continue

            break

        # Ask how many digits
        while True:
            digit_input = input("How many digits? (minimum 1): ").strip()

            if wants_to_quit(digit_input):
                return
            
            if not digit_input.isdigit():
                print("Please enter a number")
                input("Press Enter to try again...")
                continue

            digit_count = int(digit_input)

            if digit_count < 1:
                print("You must include at least 1 digit.")
                input("Press Enter to try again...")
                continue

            break

        # Ask how many symbols
        while True:
            symbol_input = input("How many special characters? (minimum 1): ").strip()

            if wants_to_quit(symbol_input):
                return
            
            if not symbol_input.isdigit():
                print("Please enter a number.")
                input("Press Enter to try again...")
                continue

            symbol_count = int(symbol_input)

            if symbol_count < 1:
                print("You must include at leat 1 special character.")
                input("Press Enter to try again...")
                continue

            break

        # Validate the total count
        
        total_required = upper_count + lower_count + digit_count + symbol_count

        if total_required > length:
            print(f"The total you selected ({total_required}) does not match the password length ({length}).")
            print("Please try again.")
            input("Press Enter to continue...")
            continue  # restart the entire generator loop

        # If total_required < length, that's ok - we will fill the rest randomly
        remaining = length - total_required

        # Build the password
        while True:
            password_chars = []

            # Add the exact number of uppercase letters
            password_chars.extend(random.choice(string.ascii_uppercase) for _ in range(upper_count))

            # Add the exact number of lowercase letters
            password_chars.extend(random.choice(string.ascii_lowercase) for _ in range(lower_count))

            # Add the exact number of digits
            password_chars.extend(random.choice(string.digits) for _ in range(digit_count))

            # Add the exact number of symbols
            password_chars.extend(random.choice(SAFE_SYMBOLS) for _ in range(symbol_count))

            # Fill the remaining characters (if any)
            remaining = length - (upper_count + lower_count + digit_count + symbol_count)

            if remaining > 0:
                # Build a pool of all allowed characters
                pool = (
                    string.ascii_uppercase +
                    string.ascii_lowercase +
                    string.digits +
                    SAFE_SYMBOLS
                )
                password_chars.extend(random.choice(pool)for _ in range(remaining))

            # Shuffle the final list so the guaranteed characters aren't grouped

            random.shuffle(password_chars)

            # Join into the final password string

            final_password = "".join(password_chars)

            print("\nYour generated password:")
            print(final_password)

            again = input("\nGenerate again with the same settings? (y/n): ").strip().lower()

            if wants_to_quit(again) or again != "y":
                return  # exit generator and go back to main menu

def main():
    clear_screen()  # Clears immediately when program starts

    while True:
        clear_screen()
        print("=== Password Tool ===")
        print("1. Validate a password")
        print("2. Generate a password")
        print("q. Quit\n")

        choice = input("Choose an option: ").strip().lower()

        if wants_to_quit(choice):
            clear_screen()
            print("Goodbye !!")
            break

        if choice == "1":
            validate_flow()
        elif choice == "2":
            password_generator()
        else:
            print("Invalid choice.")
            input("Press Enter to continue...")

if __name__ == "__main__":
   main()




