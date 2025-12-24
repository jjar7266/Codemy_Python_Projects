# Codemy.com - Instructor John Elder

# Course: Python Projects

# hangman.py

# Modified instructors code to be more Pythonic and readable

# Import modules
import os
import random

WORDLIST_FOLDER = "wordlists"

# Create the folder if it doesn't exist

if not os.path.exists(WORDLIST_FOLDER):
    os.makedirs(WORDLIST_FOLDER)

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def load_default_words():
    if not os.path.exists("words.txt"):
        print("Error: words.txt not found in the project folder.")
        return []
    
    with open("words.txt", "r") as f:
        return [line.strip().lower() for line in f if line.strip()]
    
DEFAULT_WORDS = load_default_words()

class HangmanGame:

    def __init__(self, word_list, max_attempts=6):
        self.word_list = word_list
        self.secret_word = random.choice(word_list)
        self.guessed_letters = set()
        self.wrong_guesses = 0
        self.max_attempts = max_attempts 

    def display_board(self):
        clear_screen()

        # Build the word display with underscores

        display =""
        for letter in self.secret_word:
            if letter in self.guessed_letters:
                display += letter + " "
            else:
                display += "_ "

        print("\nWord: ", display.strip())
        print(f"Guessed letters: {', '.join(sorted(self.guessed_letters))}")
        print(f"Wrong guesses: {self.wrong_guesses} / {self.max_attempts}\n")

        # Show guessed letters in alphabetical order

        guessed = " ".join(sorted(self.guessed_letters))
        print(f"Guessed letters: {guessed}\n")

    def guess_letter(self, letter):
        letter = letter.lower().strip()

        # Validate input

        if len(letter) != 1 or not letter.isalpha():
            return "invalid"
        
        # Already guessed?

        if letter in self.guessed_letters:
            return "repeat"
        
        # Add to guessed letters

        self.guessed_letters.add(letter)

        # Correct guess?

        if letter in self.secret_word:
            return "correct"
        
        # Wrong guess

        self.wrong_guesses += 1
        return "wrong"
    
    def is_won(self):
        return all(letter in self.guessed_letters for letter in self.secret_word)
    
    def is_lost(self):
        return self.wrong_guesses >= self.max_attempts
    
    def play(self):
        while True:
            
            self.reset_game()
            self.run_single_game()

            choice = input("\nPlay again (y/n): ").strip().lower()
            if choice != "y":
                break

    def reset_game(self):
        self.secret_word = random.choice(self.word_list)
        self.guessed_letters = set()
        self.wrong_guesses = 0

    def run_single_game(self):
        print("\nStarting Hangman!\n")

        while not self.is_won() and not self.is_lost():
            self.display_board()
            guess = input("Enter a letter: ".strip().lower())

            result = self.guess_letter(guess)

            if result == "invalid":
                print("Pleae enter a single letter.")
            elif result == "repeat":
                print("You already guessed that letter.")
            elif result == "correct!":
                print("Good guess!")
            elif result == "wrong":
                print("Nope! That letter is not in the word.")

        # Game ended

        self.display_board()

        if self.is_won():
            print("🎉 You won!")
        else:
            print(f"💀 You lost! The word was: {self.secret_word}")









# Main game loop

def main_menu():
    clear_screen()

    while True:
        print("\n=== Hangman ===")
        print("1. Use default word list")
        print("2. Load custom word list")
        print("q. Quit")

        choice = input("Choose an option: ").strip().lower()

        if choice == "1":
            if not DEFAULT_WORDS:
                print("Default word list is empty or missing.")
                continue

            clear_screen()
            game = HangmanGame(DEFAULT_WORDS)
            game.play()

        elif choice == "2":
            print(f"\nCustom word lists must be inside the '{WORDLIST_FOLDER}' folder.")

            # List available .txt files

            files = [f for f in os.listdir(WORDLIST_FOLDER) if f.endswith(".txt")]

            if files:
                print("\nAvailable word lists:")
                for f in files:
                    print(" -", f)
            else:
                print("\n(No .txt files found in the folder.)")

            filename = input("\nEnter the filename (example: animals.txt): ").strip()
            full_path = os.path.join(WORDLIST_FOLDER, filename)

            if not os.path.exists(full_path):
                print("File not found in the wordlists folder.")
                continue

            with open(full_path, "r") as f:
                word_list = [line.strip().lower() for line in f if line.strip()]

            clear_screen()
            game = HangmanGame(word_list)
            game.play()

        elif choice == "q":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")



if __name__ == "__main__":
    main_menu()
