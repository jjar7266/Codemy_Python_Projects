# Codemy.com - Instructor John Elder
# guessing_game.py

# Modified instructors code to be more Pythonic and readable
 
# Import modules
import os
import random

# Clear the terminal screen
def clear():
    os.system('cls')

# Play game function
def play_game():
    clear()

    number_to_guess = random.randint(1, 10)
    number_of_guesses = 0
    correct = False

    print("Welcome to the guessing Game!")
    print("I'm thinking of a number between 1 and 10")

    while not correct:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Invalid input - pleae your guess: ")
            continue

        number_of_guesses += 1
        
        if guess < number_to_guess:
            print("Too low, try again.")
        elif guess > number_to_guess:
            print("Too high, try again.")
        else:
            print(f"Correct! The number was {number_to_guess}.")
            print(f"You guessed it in {number_of_guesses} tries.")
            correct = True

    play_again()

def play_again():
    answer = input("Play again? (y/n): ").lower()

    if answer == "y":
        play_game()
    else:
        print("Thanks for playing!")

play_game()


