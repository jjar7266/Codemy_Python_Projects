# Codemy.com - Instructor John Elder

# Course: Python Projects

# anagram.py

# project build date: Jan 8, 2026

# Modified instructors code to be more Pythonic and readable

# Import modules

import json  # We import json so Python can read .json files
import os  # used to run system-level commands like clearing the screen

# Helper Function: clear_screen()

# Purpose:

#  - Clears the terminal so the program looks clean
#  - Makes the UI easier to read for the user
#  - Works on both Windows and Mac/Linux
# -----------------------------------------------------------------------

def clear_screen():
    """Clear the terminal screen."""

    # os.name tells us what operating system Python is running on.
    #
    # 'nt' means Windows. Anything else is usually Mac or Linux.
    #
    # We use a conditional expresstion to choose the correct command:
    #  - 'cls' clears the screen on Windows
    #  - 'clear' clears the screen on Mac/Linux
    #
    # os.system() runs the command as if you typed it in the terminal.
    os.system('cls' if os.name == 'nt' else 'clear')

# -----------------------------------------------------------------------
# Helper Function: pause()
# Purpose:
#  - Pauses the program until the user presses Enter
#  - Gives the user time to read output before the screen clears
# ------------------------------------------------------------------------

def pause():
    """Pause the program until the user presses Enter."""

    # input() waits for the user to type something.
    #
    # We don't care what they type - pressing Enter is enough.
    #
    # The \n adds a blank line before the message for readability.

    input("\nPress Enter to continue...")

# ------------------------------------------------------------------------

# Helper Function: load_words_from_json()
#
# Purpose:
#
#  - Open the JSON dictionary file (words_dictionary.json)
#  - Read all the words stored as keys in the JSON object
#  - Convert those keys into a clean list of lowercase words
#  - Return that list so the rest of the program can use it
#
# Why this matters:
#  - This is the foundation of the entire anagram app
#  - Without a word list, we cannot build the anagram base
#  - Keeping this is a helper makes the code modular and testable
# -----------------------------------------------------------------------

def load_words_from_json(filename):
    """Load a JSON word dictionary and return a list of words."""

    try:
        # Open the JSON file in read mode.
        #
        # 'with open(...)' automatically closes the file when done.

        with open(filename, "r") as f:

            # json.load() reads the entire JSON file
            #
            # and converts it into a Python dictionary.
            #
            # 
            #
            # Example

            """{
                  "apple": 1,
                  "banana": 1,
                  "cat": 1

                }
            """
            #

            data = json.load(f)

            # The words we want are the KEYS of the dictionary.
            #
            # data.keys() returns something like:
            #
            #  dict_keys(["apple", "banana", "cat"])
            #
            # We convert that into a list AND lowercase everything
            #
            # to keep the program consistent.

            return [word.lower() for word in data.keys()]
        
    except Exception as e:
        # This catches any other unexpected errors.

        print(f"Error loading dictionary: {e}")
        return []
    
# -----------------------------------------------------------------------

# Helper Function: build_anagram_base()
#
# Purpose:
#
#  - Take a list of words (loaded from the JSON dictionary)
#  - Convert each word into a "signature"
#
#      Example:
#          "listen" -> "eilnst"
#          "silent" -> "eilnst"
#          "enlist" -> "eilnst"
#
#  - Use the signature as a KEY in a dictinoary
#  - Store all words that share that signature in a LIST
#
# Why this matters:
#  - This creates a FAST lookup table for anagrams
#  - Instead of scanning 400,000 words every time,
#    we can find anagrams in 0(1) time (instant)
# -----------------------------------------------------------------------

def build_anagram_base(word_list):
    """Build a dictionary where sorted letters map to lists of anagrams."""

    # This dictionary will hold:
    #
    # key  -> sorted letters (signature)
    #
    # value  -> list of words that match that signature
    #
    # Example entry:
    #
    # "eilnst": ["listen", "silent", "enlist"]

    anagram_base = {}

    # Loop through every word in the dictionary

    for word in word_list:

        # Create the "signature" by sorting the letters alphabetically.
        # 
        # ''.join() turns the list of letters back into a string.
        #
        # Example:
        # 
        # word = "evil"

        key = ''.join(sorted(word))

        # If this signature doesn't exist yet, create a new list

        if key not in anagram_base:
            anagram_base[key] = []

        # Add the word to the list for this signature

        anagram_base[key].append(word)

    # Return the completed lookup table

    return anagram_base

# -----------------------------------------------------------------------

# Helper Function: find_anagrams()
#
# Purpose:
#
#  - Take a user-entered word
#  - Convert it into its "signature" (sorted letters)
#  - Look up that signature in the anagram_base dictionary
#  - Return all matching anagrams (if any)
#
# Why this matters:
#
#  - This is the function the user interacts with
#  - It uses the anagram_base we built earlier
#  - It keeps the lookup logic clean and reusable
# ------------------------------------------------------------------------

def find_anagrams(user_word, anagram_base):
    """Return a list of anagrams for the given word."""

    # Convert the user's word to lowercase to match the dictionary format

    word = user_word.lower()

    # Create the signature by sorting the letters alphabetically
    # 
    # Example:
    #   "evil" -> "eilv"

    key = ''.join(sorted(word))

    # if the signature exists in the anagram base,
    # return the list of matching words.
    #
    # If not found, return an empty list.
    # This keeps the function predictable and safe.

    return anagram_base.get(key, [])

# -----------------------------------------------------------------------
#
# Helper Function: show_menu()
#
# Purpose:
#   - Display the main menu options to the user
#   - Keeps the UI clean and consistent
#
# -----------------------------------------------------------------------

def show_menu():
    """Display the main menu options."""

    print("========================================")
    print("         ANAGRAM FINDER (v1.0)")
    print("========================================\n")

    print("1) Find anagrams for a word")
    print("2) Show total number of words loaded")
    print("3) Show total number of anagram groups")
    print("Q) Quit")
    print()

    # -------------------------------------------------------------------

# main()
#
# Purpose:
# 
#  - Load the dictionary file
#  - Build the anagram lookup table 
#  - Ask the user for a word
#  - Find and display all anagrams
#  - Pause and exit
#
# This is the "director" of the entire program.
# ------------------------------------------------------------------------

def main():
    # Clear the screen at the start for a clean UI

    clear_screen()

    # -------------------------------------------------------------------
    #
    # Step 1: Load the dictionary file
    #
    # -------------------------------------------------------------------

    print("Loading dictionary... please wait.")
    
    # Call our helper to load the JSON file

    words = load_words_from_json("words_dictionary.json")

    # If loading failed, words will be an empty list

    if not words:
        print("\nError: Could not load dictionary. Exiting program.")
        pause()
        return  # Exit main()

    print(f"Loaded {len(words)} words successfully!\n")

    # -------------------------------------------------------------------

    # Step 2: Build the anagram base (signature dictionary)

    # -------------------------------------------------------------------

    print("Building anagram base... this may take a moment.")

    anagram_base = build_anagram_base(words)

    print("Anagram base ready!\n")
    pause()

    # -------------------------------------------------------------------

    # Step 3: Main program loop

    # -------------------------------------------------------------------

    while True:
        clear_screen()
        show_menu()

        choice = input("Choose an option: ").strip().lower()

        # ---------------------------------------------------------------
        
        # Option 1: Find anagrams
        
        # ----------------------------------------------------------------

        if choice == "1":
            clear_screen()
            user_word = input("Enter a word to find its anagrams: ").strip()

            # If the user enters nothing, exit gracefully

            if not user_word:
                print("\nNo word entered. Exiting program.")
                pause()
                continue

            results = find_anagrams(user_word, anagram_base)

            clear_screen()
            print("========================================")
            print("         ANAGRAM FINDER (v1.0)")
            print("========================================\n")

            filtered = [w for w in results if w != user_word.lower()]

            if filtered:
                for w in filtered:
                    print(f" - {w}")
            else:
                print("No anagrams found.")

            print()
            pause()

        # --------------------------------

        # Option 2: Show word count

        # --------------------------------

        elif choice == "2":
            clear_screen()
            print(f"Total words loaded: {len(words)}")
            pause()

        # ---------------------------------

        # Option 3: Show anagram group count

        # ----------------------------------

        elif choice == "3":
            clear_screen()
            print(f"Total anagram groups: {len(anagram_base)}")
            pause()

        # ----------------------------------

        # Option Q: Quit

        # ----------------------------------

        elif choice == "q":
            clear_screen()
            print("Goodbye!")
            pause()
            break

        # -----------------------------------

        # Invalid input

        # -----------------------------------

        else: 
            print("\nInvalid choice.")
            pause()

if __name__ == "__main__":
    main()
            



    