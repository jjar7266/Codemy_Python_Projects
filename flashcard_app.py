# Codemy.com - Instructor John Elder

# Course: Python Projects

# flashcard_app.py

# project build date: Jan 10, 2026

# Code written by Jose "Joe" Ruiz

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

# =======================================================================

# FUNCTION: run_subtraction()

# PURPOSE: Handles the entire Subtraction flashcard session

# DETAILS: Generates random subtraction problems, ensures the result

#          is never negative, checks answers, and loops until the 

#          user chooses to return to the menu.

# ========================================================================

def run_subtraction():
    while True:  # [SESSION LOOP] Keeps giving problems until user exits

        # --------------------------------------------------------------

        # [STEP 1] Generate two random numbers (1-20)

        #          Ensure subtraction never goes negative

        # ---------------------------------------------------------------

        num1 = random.randint(1, 20)
        num2 = random.randint(1, 20)

        # Ensure num1 is the Larger number

        if num2 > num1:
            num1, num2 = num2, num1

        correct_answer = num1 - num2

        # ---------------------------------------------------------------

        # [STEP 2] Display the problem

        # ----------------------------------------------------------------

        print(f"\nWhat is {num1} - {num2}?")

        # ----------------------------------------------------------------

        # [STEP 3] Get user input

        # -----------------------------------------------------------------

        user_input = input("Your answer (or 'm' for menu): ").strip()

        # Allow returning to menu

        if user_input.lower() == "m":
            break

        # ------------------------------------------------------------------

        # [STEP 4] Validate numeric input

        # -------------------------------------------------------------------

        if not user_input.isdigit():
            print("Please enter a valid number.")
            continue

        user_answer = int(user_input)

        # ------------------------------------------------------------------

        # [STEP 5] Check correctness

        # ------------------------------------------------------------------

        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(f"Incorrect. The correct answer is {correct_answer}.")

        # ------------------------------------------------------------------

        # [STEP 6] Ask if user wants another problem 

        # ------------------------------------------------------------------

        again = input("Try another: (y/n): ").strip().lower()
        if again != "y":
            break

# ======================================================================

# FUNCTION: run_multiplication()

# PURPOSE: Handles the entire Multiplication flashcard session

# DETAILS: Generates random multiplication problems (1-12), checks

#          answers, and loops until the user chooses to return to menu.

# ========================================================================

def run_multiplication():
    while True:  # [SESSION LOOP] Keeps giving problems until user exits

        # --------------------------------------------------------------

        # [STEP 1] Generate two random numbers (1-12)

        # ---------------------------------------------------------------

        num1 = random.randint(1, 12)
        num2 = random.randint(1, 12)
        correct_answer = num1 * num2

        # --------------------------------------------------------------

        # [STEP 2] Display the problem

        # ---------------------------------------------------------------

        print(f"\nWhat is {num1} x {num2}?")

        # ----------------------------------------------------------------

        # [STEP 3] Get user input

        # -----------------------------------------------------------------

        user_input = input("Your answer (or 'm' for menu): ").strip()

        # Allow returning to menu

        if user_input.lower() == "m":
            break

        # ------------------------------------------------------------------

        # [STEP 4] Validate numeric input

        # -------------------------------------------------------------------

        if not user_input.isdigit():
            print("Please enter a valid number.")
            continue

        user_answer = int(user_input)

        # --------------------------------------------------------------

        # [STEP 5] Check correctness

        # ---------------------------------------------------------------

        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(f"Incorrect. The correct answer is {correct_answer}.")

        # -----------------------------------------------------------------

        # [STEP 6] Ask if user wants another problem

        # ------------------------------------------------------------------

        again = input("Try another: (y/n): ").strip().lower()
        if again != "y":
            break

# =======================================================================

# FUNCTION: run_division()

# PURPOSE: Handles the entire Division flashcard session

# DETAILS: Generates clean divsion problems that always divide evenly.

#          Uses the pattern: answer * divisor = dividend.

#          Loops until the user chooses to return to the menu.

# ======================================================================

def run_division():
    while True:  # [SESSION LOOP] Keeps giving problems until user exits

        # ---------------------------------------------------------------

        # [STEP 1] Generate a clean division problem

        #          Pick the correct answer first (1-12)

        #          Pick a divisor (1-12)

        #          Multiply to get the dividend

        # ----------------------------------------------------------------

        correct_answer = random.randint(1, 12)
        num2 = random.randint(1, 12)
        num1 = correct_answer * num2  # Ensures clean division

        # -----------------------------------------------------------------

        print(f"\nWhat is {num1} / {num2}?")

        # -----------------------------------------------------------------

        # [STEP 3] Get user input

        # ------------------------------------------------------------------

        user_input = input("Your answer (or 'm' for menu): ").strip()

        # Allow returning to menu

        if user_input.lower() == "m":
            break

        # ------------------------------------------------------------------

        # [STEP 4] Validate numeric input

        # ------------------------------------------------------------------

        if not user_input.isdigit():
            print("Please enter a valid number.")
            continue

        user_answer = int(user_input)

        # ------------------------------------------------------------------

        # [STEP 5] Check correctness

        # ------------------------------------------------------------------

        if user_answer == correct_answer:
            print("Correct!")
        else:
            print("Incorrect. The correct answer is {correct_answer}.")

        # -------------------------------------------------------------------

        # [STEP 6] Ask if user wants another problem

        # ---------------------------------------------------------------

        again = input("Try another: (y/n): ").strip().lower()
        if again != "y":
            break

# =======================================================================

# FUNCTION: main()

# PURPOSE: Controls the overall flow

# DETAILS: Show the menu, gets user choice, and calls the 

#          appropriate flashcard module. Loops until user quits.

# ========================================================================

def main():
    while True:  # [APP LOOP] Runs until user chooses to quit

        show_menu()  # Display menu options

        choice = get_menu_choice()  # Get validated user input

        # --------------------------------------------------------------

        # [ROUTING] Call the correct module based on user choice

        # --------------------------------------------------------------

        if choice == "1":
            run_addition()
            input("\nReturning to main menu... Press Enter to continue.")

        elif choice == "2":
            run_subtraction()
            input("\nPress Enter to return to menu.")

        elif choice == "3":
            run_multiplication()
            input("\nPress Enter to return to menu.")

        elif choice == "4":
            run_division()
            input("\nPress Enter to return to menu.")

        elif choice == "5":
            print("\nGoodbye!")
            break  # Exit the program



if __name__ == "__main__":
    main()











