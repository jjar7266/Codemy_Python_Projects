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
        self.root.geometry("600x850")
        self.root.resizable(False, False)

        self.choices = ["Rock", "Paper", "Scissors"]

        # Scores

        self.player_score = 0
        self.computer_score = 0
        self.tie_score = 0

        # Match settings

        self.match_length = 3  # Best of 3

        # Load images

        self.rock_img = PhotoImage(file="images/rock.png")
        self.paper_img = PhotoImage(file="images/paper.png")
        self.scissors_img = PhotoImage(file="images/scissors.png")

        # Title label

        self.label = tk.Label(root, text="Choose Rock, Paper, or Scissors")
        self.label.pack(pady=10)

        # Scoreboard

        self.score_label = tk.Label(
            root,
            text="Player: 0   Computer: 0   Ties: 0",
            font=("Arial", 14)
        )
        self.score_label.pack(pady=5)

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

        # New match button (hidden at first)

        self.new_match_button = tk.Button(root, text="New Match", command=self.new_match)
        
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

        # Update scores

        if result == "It's a tie!":
            self.tie_score += 1
        elif result == "You win!":
            self.player_score += 1
        else:
            self.computer_score += 1

        # Refresh scoreboard

        self.score_label.config(
            text=f"Player: {self.player_score}  Computer: {self.computer_score}  Ties: {self.tie_score}"
        )

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

        # Check for match winner

        if self.player_score == self.match_length:
            self.result_label.config(text="You won the match!")
            self.end_match()
            return
        
        if self.computer_score == self.match_length:
            self.result_label.config(text="Computer won the match!")
            self.end_match()
            return
        
    def reset_game(self):
        # Clear images

        self.user_choice_label.config(image="")
        self.computer_choice_label.config(image="")

        # Clear text

        self.result_label.config(text="")

        # Hide Play Again button

        self.play_again_button.pack_forget()

    def end_match(self):
        # Disable choice buttons

        for widget in self.button_frame.winfo_children():
            widget.config(state="disabled")

        # Hide Play Again button

        self.play_again_button.pack_forget()

        # Show New Match button

        self.new_match_button.pack(pady=10)

    def new_match(self):
        # Reset scores

        self.player_score = 0
        self.computer_score = 0
        self.tie_score = 0

        # Update scoreboard

        self.score_label.config(
            text=f"Player: {self.player_score}   Computer: {self.computer_score}   Ties: {self.tie_score}"
        )

        # Clear images and text

        self.user_choice_label.config(image="")
        self.computer_choice_label.config(image="")
        self.result_label.config(text="")

        # Hide New Match button

        self.new_match_button.pack_forget()

        # Re-enable choice buttons

        for widget in self.button_frame.winfo_children():
            widget.config(state="normal")

# Run the game

root = tk.Tk()
game = RPSGame(root)
root.mainloop()
