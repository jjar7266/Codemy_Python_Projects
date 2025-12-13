# Codemy.com - Instructor John Elder
# Rock, Paper, Scissors game

# Tkinter GUI APP

# Import modules
import tkinter as tk
from tkinter import PhotoImage
import random

class RPSGame:

    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors")
        
        self.choices = ["Rock", "Paper", "Scissors"]

        # Load images

        self.rock_img = PhotoImage(file="images/rock.png")
        self.paper_img = PhotoImage(file="images/paper.png")
        self.scissors_img = PhotoImage(file="images/scissors.png")

        # Title label

        self.label = tk.Label(root, text="Choose Rock, Paper, or Scissors")
        self.label.pack(pady=10)

        # Frame for image buttons

        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=10)

        tk.Button(self.button_frame, image=self.rock_img, command=lambda: self.play("Rock")).grid(row=0, column=0, padx=10)
        tk.Button(self.button_frame, image=self.paper_img, command=lambda: self.play("Paper")).grid(row=0, column=1, padx=10)
        tk.Button(self.button_frame, image=self.scissors_img, command=lambda: self.play("Scissors")).grid(row=0, column=2, padx=10)

        # Labels to show chosen images

        self.user_choice_label = tk.Label(root)
        self.user_choice_label.pack(pady=5)

        self.computer_choice_label = tk.Label(root)
        self.computer_choice_label.pack(pady=5)

        # Result text

        self.result_label = tk.Label(root, text="", font=("Arial", 14))
        self.result_label.pack(pady=20)

        # Play again button (hidden at first)

        self.play_again_button = tk.Button(root, text="Play Again", command=self.reset_game)
        # Not packed yet


    def play(self, user_choice):
        computer_choice = random.choice(self.choices)

        # Determine result

        if user_choice == computer_choice:
            result = "It's a tie!"
        elif (
            (user_choice == "Rock" and computer_choice == "Scissors") or
            (user_choice == "Paper" and computer_choice == "Rock") or
            (user_choice == "Scissors" and computer_choice == "Paper")
        ):
            result = "You win!"
        else:
            result = "You lose!"

        # Show User's Choice Image

        if user_choice == "Rock":
            self.user_choice_label.config(image=self.rock_img)
        elif user_choice == "Paper":
            self.user_choice_label.config(image=self.paper_img)
        else:
            self.user_choice_label.config(image=self.scissors_img)

        # Show Computer's Choice Image

        if computer_choice == "Rock":
            self.computer_choice_label.config(image=self.rock_img)
        elif computer_choice == "Paper":
            self.computer_choice_label.config(image=self.paper_img)
        else:
            self.computer_choice_label.config(image=self.scissors_img)

        # Update Result Text

        self.result_label.config(
            text=f"You chose {user_choice}\nComputer chose {computer_choice}\n{result}"
        )

        # Show Play Again button

        self.play_again_button.pack(pady=10)

    def reset_game(self):
        # Clear images

        self.user_choice_label.config(image="")
        self.computer_choice_label.config(image="")

        # Clear text

        self.result_label.config(text="")

        # Hide Play Again button

        self.play_again_button.pack_forget()

# Run the game

root = tk.Tk()
game = RPSGame(root)
root.mainloop()
