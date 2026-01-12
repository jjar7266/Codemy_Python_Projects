# Codemy.com - Instructor John Elder

# Course: Python Projects

# filez_manager.py

# project build date: Jan 11, 2026

# Code written by Jose "Joe" Ruiz

# Modified instructors code to be more Pythonic and readable

# Import modules

import os

# Clear the terminal screen (Windows uses 'cls', others use 'clear)

def clear_screen():
    # Decide which command to run based on the operating system

    command = 'cls' if os.name == 'nt' else 'clear'

    # Run the command in the terminal

    os.system(command)


# Check if a directory exists

def validate_path(path):
    # Return True if the directory exists, False otherwise

    return os.path.isdir(path)


# Build a full file path from directory + filename

def build_full_path(directory, filename):
    # Joins the directory and filename safely for any OS

    return os.path.join(directory, filename)


# Create a new file and save text into it

def create_file():
    # Ask the user for the text they want to save

    text = input("Enter the text you want to save in the file: ")

    # Ask for the filename (example: notes.txt)

    filename = input("Enter the filename (e.g., myfile.txt): ")

    # Ask for the directory where the file should be saved

    directory = input("Enter the file location (directory path): ")

    # Make sure the directory actually exists

    if not validate_path(directory):
        print("That directory does not exist. Please try again.")
        return  # Exit the function early
    
    # Build the full path: directory + filename

    full_path = build_full_path(directory, filename)

    # Write the text to the file

    try:
        with open(full_path, "w") as file:
            file.write(text)
        print(f"File '{filename}' saved successfully at {directory}.")
    except Exception as e:
        # Catch unexpected errors (permissions, invalid characters, etc.)

        print("Something went wrong while saving the file.")
        print(f"Error: {e}")


# Open an existing file and display its contents

def read_file():
    # Ask for the filename the user wants to open

    filename = input("Enter the filename to open (e.g., myfile.txt): ")

    # Ask for the directory where the file is located

    directory = input("Enter the file location (directory path): ")

    # Make sure the directory exists

    if not validate_path(directory):
        print("That directory does not exist. Please try again.")
        return
    
    # Build the full path to the file

    full_path = build_full_path(directory, filename)

    # Try to open and read the file

    try:
        with open(full_path, "r") as file:
            contents = file.read()
        print("\nFile contents:")
        print(contents)
    except FileNotFoundError:
        print("That file does not exist in the specified directory.")
    except Exception as e:
        print("Something went wrong while reading the file.")
        print(f"Error: {e}")


# Show the main menu options to the user

def show_menu():
    print("\n--- File Manager ---")
    print("1. Create and save a file")
    print("2. Open and read a file")
    print("3. Quit")


# Main program loop

def main():
    while True:
        clear_screen()     # Keep the interface clean

        show_menu()        # Display the menu options

        choice = input("Choose an option (1/2/3): ")

        # Option 1: Create and save a file

        if choice == "1":
            create_file()
            input("\nPress Enter to continue...")  # Pause before returning to menu

        # Option 2: Open and read a file

        elif choice == "2":
            read_file()
            input("\nPress Enter to continue...")  # Pause before returniing to menu

        # Option 3: Quit the program

        elif choice == "3":
            print("Goodbye!")
            break  # Exit the loop and end the program

        # Handle invalid menu choices

        else:
            print("Invalid choice. Please enter 1, 2, 3.")
            input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()

