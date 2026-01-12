# Codemy.com - Instructor John Elder

# Course: Python Projects

# choose_adventure.py

# project build date: Jan 10, 2026

# Code written by Jose "Joe" Ruiz

# Modified instructors code to be more Pythonic and readable

# Import modules

import random
import os

# ====================================================================

# FUNCTION: clear_screen()

# PURPOSE: Clears the terminal screen (cross-platform)

# ====================================================================

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# ====================================================================

# FUNCTION: play_game()

# PURPOSE: Runs a single adventure session.

# DETAILS: User chooses directions (N/S/E/W). Each move has a random

#          chance of falling into a pit or reaching the castle.

# ======================================================================

def play_game():
    clear_screen()  # Clean start for each game

    print("Welcome to the Adventure Game!")
    print("You are on a quest to rescue the princess in the castle.")
    print("Navigate carefully using directions: N (North), S (South), E (East), W (West).")
    print("Each move has a chance of falling into a pit, so choose wisely!")
    print("Good luck on your adventure!\n")

    moves = 0  # Track how many safe moves the player makes

    while True:
        direction = input("Choose a direction (N/S/E/W): ").strip().lower()

        if direction not in ["n", "s", "e", "w"]:
            print("Invalid direction. Please choose N, S, E, or W.")
            continue

        # Random pit chance 

        if random.randint(1, 10) == 1:
            print(f"Oh no! You chose {direction.upper()} and fell into a pit. Game over!")
            print(f"You survived {moves} move(s).")
            break

        moves += 1  # Only increment if the player survives the move

        # Random win chance 

        if random.randint(1, 10) == 1:
            print("Congratulations! You have reached the castle and rescued the princess!")
            print(f"It took you {moves} move(s) to reach the castle.")
            break

        print(f"You moved {direction.upper()}. Keep going!")

# =======================================================================

# MAIN LOOP: Allows user to replay the game

# =======================================================================

while True:
    play_game()
    again = input("\nWould you like to play again? (y/n): ").strip().lower()

    if again != "y":
        clear_screen()
        print("Thanks for playing! Goodbye.")
        break

    clear_screen()  # Clean screen before starting a new game
