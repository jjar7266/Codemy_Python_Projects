# Codemy.com: Instructor John Elder

# Import modules
import os # using to clear the screen
import random

# Clear the screen
os.system("cls")  # windows powershell clear command

# Generate a random number and assign it to a variable
number_to_guess = random.randint(1, 10)

# Get user input
print("Guess a number between 1 - 10")

# try/except block
try:
    guess = int(input("Enter your Guess: "))
    print(f"You guessed: {guess}")
except Exception as e:
    print("Something went wrong")
    




