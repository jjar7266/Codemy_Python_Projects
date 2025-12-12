# Codemy.com - Instructor John Elder
# Rock, Paper, Scissors game

# Modified instructors code to be more Pythonic and readable
 
# Import modules
import random
import os

def clear():
    os.system('cls')  # Windows-only, clear screen

def play_game():
    clear()
    print("Rock, Paper, Scissors!")
    print("----------------------")
    print("Choose: R = Rock, P = Paper, S = Scissors")

    valid_inputs = ["r", "p", "s"]

    user_input = input("Your choice: ").lower()

    while user_input not in valid_inputs:
        print("Invalid choice. Try again.")
        user_input = input("Choose R, P, or S: ").lower()

    # Convert single letter to full word

    if user_input == "r":
        user_choice = "rock"
    elif user_input == "p":
        user_choice = "paper"
    else:
        user_choice = "scissors"

    computer_choice = random.choice(["rock", "paper", "scissors"])

    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("\nIt's a tie!")
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("\nYou Win!")
    else:
        print("\nYou lose!")

    play_again()

def play_again():
    answer = input("\nPlay again? (y/n): ").lower()

    if answer == "y":
        play_game()
    else:
        print("Thanks for playing!")

play_game()
