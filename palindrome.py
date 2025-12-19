# Codemy.com - Instructor John Elder

# palindrome.py

# Modified instructors code to be more Pythonic and readable

# Import modules
import os
import time

# Change this value to control how long the program waits before clearing
PAUSE_SECONDS = 2

def is_palindrome(text: str) -> bool:
    # Normalized: lowercase and keep only letters/numbers

    cleaned = ''.join(ch.lower() for ch in text if ch.isalnum())
    print(f"[DEBUG] Cleaned text: {cleaned}")  # debug print
    
    return cleaned == cleaned[::-1]

def run_checker():
    print("Palindrome Checker")
    print("Type 'q' to quit.\n")
    count = 0  # track how many inputs processed

    while True:
        text = input("Enter text: ").strip()
        if text.lower() == 'q':
            print("Goodbye !")
            break

        if is_palindrome(text):
            print("YES, it's a palindrome\n")
        else:
            print("NO, not a palindrome\n")

        count += 1

        # Clear screen every 3 inputs
        if count % 3 == 0:
            time.sleep(PAUSE_SECONDS)  # wait before clearing

            os.system("cls")  # use "clear on Linux/macOS"

            print("Palindrome Checker")
            print("Type 'q' to quit.\n")

if __name__ == "__main__":
    run_checker()
