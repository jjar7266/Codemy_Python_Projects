# Codemy.com - Instructor John Elder

# Course: Python Projects

# subprocesser.py

# project build date: Jan 12, 2026

# Code written by Jose "Joe" Ruiz

# Modified instructors code to be more Pythonic and readable

# Import modules

import os
import subprocess
import sys

# ===================================================

# clear_screen()

# ==================================================

# This helper function clears the terminal window.
# It checks which operating system you're on:
# - "nt" means Windows -> use the "cls" command
# - otherwise (Mac/Linux) -> use the "clear" command
# This keeps the menu clean every time it refreshes.

# ===================================================

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

# ================================================
# run_project(project_name)
# ================================================

# Launches one of your Python apps using the SAME
# interpreter as the launcher (via sys.executable),
# guaranteeing it runs inside your virtual environment.
#
# subprocess.run() waits for the app to finish before
# returning control to the launcher. This prevents
# input/output conflicts and ensures each app behaves
# normally in the terminal.
#
# cwd=os.getcwd() makes sure the app runs from the
# correct project folder, avoiding path issues.
#
# Any launch errors (missing file, bad path, etc.)
# are caught and printed cleanly.

# ================================================

def run_project(project_name):
    try:
        print(f"\nLaunching {project_name}...")
        subprocess.run(
            [sys.executable, project_name],  # use the venv's Python

            cwd=os.getcwd()                  # run from the correct folder

        )
        print(f"\nReturned from {project_name}...")
    except Exception as e:
        print(f"\nError launching {project_name}: {e}")

# ====================================================

# main()

# ====================================================

# This is the heart of the Subprocesser.
# It loads your list of .py files from requirements.txt,
# builds a dynamic menu, and handles user choices.

# ==========================================================

def main():

    # -------------------------------------------------------

    # Load the list of projects from requirements.txt

    # -------------------------------------------------------

    # We strip whitespace and ONLY keep lines ending in .py
    # This protects the menu from folders, junk files, etc.

    # --------------------------------------------------------
    
    with open("requirements.txt", encoding="utf-8") as f:
        projects = [
            line.strip()
            for line in f
            if line.strip().endswith(".py")
        ]

    # ---------------------------------------------------------

    # Main program loop

    # ----------------------------------------------------------

    # This loop keeps the menu running until the user
    # chooses the Quit option.

    # -----------------------------------------------------------

    while True:
        clear_screen()  # Keep the menu clean

        print(" --- Main Menu ---\n")

        # -------------------------------------------------------

        # Dynamically print each project as a menu option
        # enumerate() gives us:
        #   i = menu number (1, 2, 3...)
        #   project = filename from the list

        # --------------------------------------------------------

        for i, project in enumerate(projects, start=1):
            print(f"{i:>2}.  {project:<30}")

        # Add the Quit option at the end

        print(f"{len(projects) + 1:>2}.  {'Quit':<30}")

        # --------------------------------------------------------

        # Get user input

        # --------------------------------------------------------

        choice = input("\nChoose an option: ").strip()

        # Validate input: must be a number

        if not choice.isdigit():
            print("\nInvalid choice. Number only.")
            input("Press Enter to continue...")
            continue

        choice = int(choice)

        # --------------------------------------------------------

        # Quit option

        # ---------------------------------------------------------

        if choice == len(projects) + 1:
            print("\nGoodbye!")
            break

        # ---------------------------------------------------------

        # Valid project selection

        # --------------------------------------------------------

        if 1 <= choice <= len(projects):
            selected_project = projects[choice - 1]
            run_project(selected_project)
            input("\nPress Enter to return to the menu...")
        else:
            print("\nInvalid choice.")
            input("Press Enter to continue...")

# ======================================================================

# Standard Python entry point

# ======================================================================

# This ensures main() only runs when THIS file is executed,
# not when it's imported somewhere else.

# ======================================================================

if __name__ == "__main__":
    main()

