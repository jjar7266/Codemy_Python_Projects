# Codemy.com - Instructor John Elder

# Course: Python Projects

# word_count.py

# Modified instructors code to be more Pythonic and readable

"""
A basic word and character count app:
that will count the words in any given sentence.
and also count the number of characters with spaces
and without spaces.
"""

# Import modules
import os

def clear_screen():
    # Detect the OS and run the appropriate command

    os.system('cls' if os.name == 'nt' else 'clear')


class WordCounter:
    """Counts words and characters in a sentence."""

    def __init__(self, text: str):
        # Store the sentence inside the object

        # This becomes accessible as self.text

        self.text = text

    def count_words(self) -> int:
        # Split the text on whitespace and count the resulting list

        return len(self.text.split())
    
    def count_chars_with_spaces(self) -> int:
        # Count every character exactly as typed, including spaces

        return len(self.text)
    
    def count_chars_without_spaces(self) -> int:
        # Remove spaces first, then count the remaining characters

        return len(self.text.replace(" ", ""))
    

# FUNCTION: main()

#  * Display a simple title
#  * Ask the user for a sentence
#  * Create a WordCounter object
#  * Print the results using the class methods

def main():
    clear_screen()  # Clear the terminal before showing anything

    # Print a simple header

    print("Word Count Intro")
    print("-" * 30)

    # Ask the user for a sentence
    # .strip() removes leading/trailing spaces

    sentence = input("Enter a sentence: ").strip()

    # Create a WordCounter object with the user's sentence

    counter = WordCounter(sentence)

    # Display the results using the class methods

    print(f"\nWord Count: {counter.count_words()}")
    print(f"Character count (including spaces): {counter.count_chars_with_spaces()}")
    print(f"Character count (excluding spaces): {counter.count_chars_without_spaces()}")


# STANDARD PYTHON ENTRY POINT

if __name__ == "__main__":
    main()



