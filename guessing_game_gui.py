# Codemy.com - Instructor John Elder
# Tkinter GUI Guessing Game

# Modified instructors code to be more Pythonic and readable
# Class and Functions

# Import modules

import tkinter as tk
import random

class GuessingGame:

    def __init__(self, root):
        self.root = root
        self.root.title("Guessing Game")
        self.root.geometry("500x350")

        self.number_to_guess = random.randint(1, 10)
        self.number_of_guesses = 0

        self.label = tk.Label(root, text="I'm thinking of a number between 1 and 10.")
        self.label.pack(pady=10)

        self.entry = tk.Entry(root)
        self.entry.pack(pady=5)

        self.button = tk.Button(root, text="Guess", command=self.check_guess)
        self.button.pack(pady=5)

        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=10)

        self.play_again_button = tk.Button(root, text="Play Again", command=self.reset_game)
        
    def check_guess(self):
        guess_text = self.entry.get()

        if not guess_text.isdigit():
            self.result_label.config(text="Please enter a valid number.")
            self.entry.delete(0, tk.END)  # Clear invalid input
            return
        
        guess = int(guess_text)
        self.number_of_guesses += 1

        self.entry.delete(0, tk.END)      # Clear after every guess

        if guess < self.number_to_guess:
            self.result_label.config(text="Too low, try again.")
        elif guess > self.number_to_guess:
            self.result_label.config(text="Too high, try again.")
        else:
            self.result_label.config(
                text=f"Correct! The number was {self.number_to_guess}.\n"
                     f"You guessed it in {self.number_of_guesses} tries."
            )
            self.button.config(state="disabled")
            self.play_again_button.pack(pady=5)  # show button now

    def reset_game(self):
        self.number_to_guess = random.randint(1, 10)
        self.number_of_guesses = 0
        self.entry.delete(0, tk.END)
        self.result_label.config(text="")
        self.button.config(state="normal")
        self.play_again_button.pack_forget()     # hide button again

root = tk.Tk()
game = GuessingGame(root)
root.mainloop()


