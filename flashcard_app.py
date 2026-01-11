# Codemy.com - Instructor John Elder

# Course: Python Projects

# flashcard_app.py

# project build date: Jan 10, 2026

# Modified instructors code to be more Pythonic and readable
 
# Import modules

import os  # Used for clearing the termianl screen
import random  # Used to generate random numbers for math problems


# ================================================================

# FUNCTION: clear_screen()

# PURPOSE:  Clears the terminal window for a clean UI experience

# DETAILS:  Uses 'cls' for Windows and 'clear' for Mac/Linux

# ================================================================

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# ================================================================

# FUNCTION: show_menu()

# PURPOSE:  Displays the main menu options to the user

# DETAILS:  Called at the start of each loop iteration in main()

# ================================================================

def show_menu():
    clear_screen()  # [STEP] Clear screen before showing menu

    # [DISPLAY] Main menu header and options

    print("--- Math Flashcard App ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quit")
    print()  # Blank line for spacing

# ==================================================================

# FUNCTION: get_menu_choice()

# PURPOSE: Handles user input and ensures valid menu selection

# DETAILS: Loops until user enters a number between 1 and 5

# RETURNS: A string representing the user's valid choice

# ==================================================================

def get_menu_choice():
    while True:  # [LOOP] keep asking until valid input is received

        choice = input("Choose an option (1-5): ").strip()  # [INPUT] Get user choice

        # [VALIDATION] Check if input is one of the allowed menu numbers

        if choice in {"1", "2", "3", "4", "5"}:
            return choice  # [RETURN] Valid choice returned to caller
        
        # [ERROR] If invalid, show message and loop again

        print("Invalid choice. Please enter a number 1-5.")

# ======================================================================

# FUNCTION: run_addition()

# PURPOSE:  Handles the entire Addition flashcard session

# DETAILS:  Generates random addition problems, checks answers,

#           and loops until the user choosed to return to menu

# ======================================================================

def run_addition():
    while True:  # [SESSION LOOP] Keeps giving problems until user exits

        # ==============================================================

        # [STEP 1] Generate two random numbers for the addition problem

        # ==============================================================

        num1 = random.randint(1, 20)  # First number (1-20)
        num2 = random.randint(1, 20)  # Second number (1-20)
        correct_answer = num1 + num2  # Store correct answer

        # ===============================================================

        # [STEP 2] Display the problem to the user

        # ===============================================================

        print(f"\nWhat is {num1} + {num2}?")

        # ==============================================================

        # [STEP 3] Get the user's anwer

        # ==============================================================

        user_input = input("Your answer (or 'm' for menu): ").strip()

        # [OPTION] Allow user to return to main menu

        if user_input.lower() == "m":
            break  # Exit the addition session and return to menu

        # ===============================================================

        # [STEP 4] Validate numeric input

        # ===============================================================

        if not user_input.isdigit():
            print("Please enter a valid number.")
            continue  # Restart loop with a new problem

        user_answer = int(user_input)

        # ================================================================

        # [STEP 5] Check correctness and give feedback

        # =================================================================

        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(f"Incorrect. The correct answer is {correct_answer}.")

        # ==================================================================

        # [STEP 6] Ask if user wants another problem

        # ==================================================================

        again = input("Try another: (y/n): ").strip().lower()
        if again != "y":
            break  # Exit session and return to menu







