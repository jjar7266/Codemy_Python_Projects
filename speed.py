# Codemy.com - Instructor John Elder
# Course: Python Projects
# speed.py
# project build date: Jan 8, 2026

# Import modules

import os
import time
import random
import msvcrt   # Windows-only keyboard capture

# ------------------------------------------------------------
# 1. Clear the terminal screen
# ------------------------------------------------------------
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# ------------------------------------------------------------
# 2. A pool of sentences for the typing test
# ------------------------------------------------------------
SENTENCES = [
    "Python is an easy to learn programming language.",
    "The quick brown fox jumps over the lazy dog.",
    "Typing speed tests help improve accuracy and focus.",
    "Clean code is easier to read, maintain, and debug.",
    "Practice makes progress, not perfection."
]


# ------------------------------------------------------------
# 3. Pick a random sentence from the pool
# ------------------------------------------------------------
def get_random_sentence():
    return random.choice(SENTENCES)


# ------------------------------------------------------------
# 4. Show the intro screen and instructions
# ------------------------------------------------------------
def show_intro(sentence):
    clear_screen()
    print("--- Typing Speed Test ---")
    print("Type the following sentence exactly as shown:\n")
    print(sentence)
    print("\nStart typing when you're ready...")
    print("(Timer begins on your FIRST keystroke)")
    print("(Do NOT press Enter to finish — just type the sentence)")


# ------------------------------------------------------------
# 5. Capture keystrokes until the full sentence is typed
#    - Timer starts on first keystroke
#    - Timer stops when typed == target_sentence
#    - Backspace works
#    - Enter is ignored
# ------------------------------------------------------------
def capture_typed_sentence(target_sentence):
    typed = ""          # What the user has typed so far
    start_time = None   # Timer starts on first keystroke

    while True:
        # Check if a key was pressed
        if msvcrt.kbhit():
            char = msvcrt.getwch()  # Read one character

            # Start timer on FIRST keystroke
            if start_time is None:
                start_time = time.time()

            # Handle BACKSPACE
            if char == '\b':
                if len(typed) > 0:
                    typed = typed[:-1]          # Remove last character
                    print("\b \b", end="", flush=True)  # Erase on screen
                continue

            # Ignore ENTER (we don't use it in this version)
            if char == '\r':
                continue

            # Add the typed character
            typed += char
            print(char, end="", flush=True)

            # STOP when the typed text EXACTLY matches the target
            if typed == target_sentence:
                end_time = time.time()
                return typed, start_time, end_time


# ------------------------------------------------------------
# 6. Calculate Words Per Minute (WPM)
# ------------------------------------------------------------
def calculate_wpm(sentence, start_time, end_time):
    elapsed_seconds = end_time - start_time
    elapsed_minutes = elapsed_seconds / 60
    word_count = len(sentence.split())
    return word_count / elapsed_minutes


# ------------------------------------------------------------
# 7. Calculate accuracy (word-by-word comparison)
# ------------------------------------------------------------
def calculate_accuracy(target, typed):
    target_words = target.split()
    typed_words = typed.split()

    correct = 0
    for t, u in zip(target_words, typed_words):
        if t == u:
            correct += 1

    return (correct / len(target_words)) * 100


# ------------------------------------------------------------
# 8. Main program loop
# ------------------------------------------------------------
def main():
    while True:
        # Pick a sentence and show instructions
        sentence = get_random_sentence()
        show_intro(sentence)

        # Capture typing with first-keystroke timer
        typed, start_time, end_time = capture_typed_sentence(sentence)

        # Calculate results
        wpm = calculate_wpm(sentence, start_time, end_time)
        accuracy = calculate_accuracy(sentence, typed)

        # Show results
        print("\n\n--- Results ---")
        print(f"Speed: {wpm:.1f} WPM")
        print(f"Accuracy: {accuracy:.1f}%")

        # Ask to retry
        again = input("\nTry again? (y/n): ").lower()
        if again != "y":
            print("Goodbye!")
            break


# ------------------------------------------------------------
# 9. Run the program
# ------------------------------------------------------------
if __name__ == "__main__":
    main()