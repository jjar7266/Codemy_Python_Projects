# Codemy.com - Instructor John Elder

# Course: Python Projects

# to_do_list.py

# Modified instructors code to be more Pythonic and readable

""" This is a simple command-line To-DO application.
It lets the user view tasks, add tasks, remove tasks,
and quit the program.
"""

import os  # needed to clear the terminal screen

# FUNCTION: clear_screen()
# Clears the terminal screen on Windows, macOS, and Linux.

def clear_screen():
    # Windows uses 'cls', macOS/Linux use 'clear'
    os.system('cls' if os.name == 'nt' else 'clear')


# FUNCTION: pause()
# Pauses the program so the user can read the output.

def pause():
    input("\nPress Enter to continue...")


# LIST STORAGE - This list will hold all the user's tasks.
# Starts empty until the user adds items.

todo_list = []


# Function: show_menu()
# Displays the main menu options to the user.
# Called every loop so the user can choose an action.

def show_menu():
    print("\n--- TO-DO LIST MENU ---")
    print("1. View To-Dos")  # Option to show all tasks
    print("2. Add To-Do")    # Option to add a new task
    print("3. Remove To-Do") # Option to delete a task
    print("4. Mark Task as Completed")  # Option to mark task as completed
    print("5. Quit")         # Option to exit the program


# FUNCTION: view-todos()
# Shows all tasks in the list.
# If the list is empty, it tells the user.

def view_todos():
    if not todo_list:  # Checks if the list is empty
        print("\nYour list is empty.")
    else:
        print("\nYour To-Dos: ")
        # enumerate() gives each task a number starting at 1

        for index, item in enumerate(todo_list, start=1):
            # Determine the status icon based on True/False

            status = "✔" if item["completed"] else "✘"
            print(f"{index}. [{status}] {item['task']}")  # Prints numbered tasks


# FUNCTION: add_todo()
# Asks the user for a new task and adds it to the list.

def add_todo():
    item = input("\nEnter a new to-do: ")  # User types a task
    todo_list.append({"task": item, "completed": False})                 # Adds task to list
    print(f"Added: {item}")                # Confirms addition


# FUNCTION: remove_todo()
# Shows the list, asks which task to remove,
# and deletes it safely using try/except.

def remove_todo():
    view_todos()  # Show tasks first so user knows the numbers

    if todo_list:  # Only allow removal if list is not empty
        try:
            # User enters the number of the task to remove
            num = int(input("\nEnter the number to remove: "))

            # pop(num - 1) removes the correct item (lists start at 0)
            removed = todo_list.pop(num - 1)
            print(f"Removed: {removed}['task]")  # Confirms removal

        except (ValueError, IndexError):
            # ValueError = user typed letters instead of numbers
            # IndexError = user typed a number not in the list
            print("Invalid selection.")


# FUNCTION: mark_completed()
# Lets the user choose a task and mark it as completed.

def mark_completed():
    view_todos()  # Show tasks so the user knows the numbers

    if todo_list:  # Only allow marking if list is not empty

        try:
            # Ask the user which task number to mark
            num = int(input("\nEnter the number to mark as completed: "))

            # Change the "completed" value to True
            todo_list[num -1]["completed"] = True

            # Confirm the action
            print(f"Marked as completed: {todo_list[num - 1]['task']}")

        except (ValueError, IndexError):
            # ValueError = user typed letters instead of numbers

            # IndexError = number not in the list

            print("Invalid selection.")



# MAIN PROGRAM LOOP
# This loop keeps the program running until the user quits.
# It shows the menu, gets the user's choice, and calls
# the correct function based on their input.

while True:
    clear_screen()  # Clears screen before showing menu

    show_menu()  # Display menu options

    choice = input("\nChoose an option: ")  # User picks 1-4

    if choice == "1":
        view_todos()   # Show tasks
        pause()

    elif choice == "2":
        add_todo()     # Add a task
        pause()

    elif choice == "3":
        remove_todo()  # Remove a task
        pause()

    elif choice == "4":
        mark_completed()
        pause()

    elif choice == "5":
        print("Goodbye!")  # Exit message
        break              # Stops the loop and ends program

    else:
        print("Invalid choice. Try again.")  # Handles bad input 
        pause()

