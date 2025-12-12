# Codemy.com: Instructor John Elder
# guessing game

# Import modules
import os # using to clear the screen
import random

# Create our main game function
def game():
        
        # Create a variable to keep track the number of guesses
        number_of_guesses = 0
        correct = False
        
        # Clear the screen
        os.system("cls")  # windows powershell clear command

        # Generate a random number and assign it to a variable
        number_to_guess = random.randint(1, 10)

        # Get user input
        print("Guess a number between 1 - 10")

        # Create guessing loop
        while not correct:  # Pythonic: Modified instructors line of code

            # try/except block
            try:
                guess = int(input("Enter your Guess: "))
                print(f"You guessed: {guess}")
            except ValueError:
                print("Invalid input - please enter a number.")
                continue  # Let them try again without ending the game

            number_of_guesses += 1  # Increment once per guess

            # Create some logic to check the guess
            if guess < number_to_guess:
                 print("Too Low! - Try Again!")

            elif guess > number_to_guess:
                 print("Too High! - Try Again!")

            else:
                print(f"Correct! the number was {number_to_guess}.")
                print(f"you guessed it in {number_of_guesses} guesses!")
                # Set correct to TRUE
                correct = True
                

# call our game function
game()
