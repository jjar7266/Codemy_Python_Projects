# Codemy.com - Instructor John Elder
# Rock, Paper, Scissors game

# Tkinter GUI APP

# Import modules
import tkinter as tk
import random

class RPSGame:

    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors")
        self.root.geometry("400x300")

        self.choices = ["Rock", "Paper", "Scissors"]

        self.label = tk.Label(root, text="Choose Rock, Paper, or Scissors")
        self.label.pack(pady=10)

        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=10)

        tk.Button(self.button_frame, text="Rock", command=lambda: self.play("Rock")).grid(row=0, column=0, padx=10)
        tk.Button(self.button_frame, text="Paper", command=lambda: self.play("Paper")).grid(row=0, column=1, padx=10)
        tk.Button(self.button_frame, text="Scissors", command=lambda: self.play("Scissors")).grid(row=0, column=2, padx=10)

        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=20)

        self.play_again_button = tk.Button(root, text="Play Again", command=self.reset_game)
        
    def play(self, user_choice):
        computer_choice = random.choice(self.choices)

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
        
        self.result_label.config(
            text=f"You chose {user_choice}\nComputer chose {computer_choice}\n{result}"
        )

        self.play_again_button.pack(pady=10)

    def reset_game(self):
        self.result_label.config(text="")
        self.play_again_button.pack_forget()

root = tk.Tk()
game = RPSGame(root)
root.mainloop()
