# Codemy.com - Instructor John Elder

# Course: Python Projects

# turtle_draw.py

# Modified instructors code to be more Pythonic and readable

# built on Jan 6, 2026

# Import modules

import turtle  # This lets us draw shapes visually in a separate window
import os      # Used to clear the terminal window


# FUNCTION: clear_screen()

def clear_screen():
    """Clears the terminal window for a clean UI."""
    os.system('cls' if os.name == 'nt' else 'clear')


# FUNCTION: pause()

def pause():
    """Pauses the program until the user presses Enter."""
    input("\nPress Enter to continue...")


# FUNCTION: get_size()

def get_size():
    """Ask the user for a size and return it as an integer."""
    while True:
        size = input("Enter the size of the shape (e.g., 50-200): ").strip()
        if size.isdigit():
            return int(size)
        else:
            print("Please enter a valid number.")


# Set up the drawing window

screen = turtle.Screen()  # Create a window for drawing

screen.title("Shape Drawing with Turtle")  # Set the window title

# Create a turtle object that will do the drawing

t = turtle.Turtle()        # This is our pen - it moves and draws


# FUNCTION: draw_square()

# Draws a square using the turtle

def draw_square(size):
    for _ in range(4):      # Repeat 4 times (4 sides)

        t.forward(size)      # Move forward 100 pixels

        t.right(90)         # Turn right 90 degrees


# FUNCTION: draw_circle()

# Draws a circle using the turtle

def draw_circle(size):
    t.circle(size)            # Draw a circle with radius 50


# FUNCTION: draw_triangle()

# Draws an equilateral triangle

def draw_triangle(size):
    for _ in range(3):       # Repeat 3 times (3 sides)

        t.forward(size)       # Move forward 100 pixels

        t.left(120)          # Turn left 120 degrees to make equal angles


# FUNCTION: main()

# Runs the menu loop and responds to user choices

def main():
    while True:  # Infinite loop - keeps running until user chooses Exit

        clear_screen()  # Clean terminal before showing the menu

        # Show menu options

        print("\nSelect a shape to draw:")
        print("1. Square")
        print("2. Circle")
        print("3. Triangle")
        print("4. Exit")

        # Ask user for input

        choice = input("Enter the number of your choice: ").strip()

        # Respond to user input

        if choice == "1":
            t.clear()           # Clear previous drawing

            size = get_size()   # get user input on size of drawing

            draw_square(size)       # Draw the shape

            pause()             # Wait before returning to menu


        elif choice == "2":
            t.clear()           # Clear previous drawing

            size = get_size()   # get user input on size of drawing

            draw_circle(size)       # Draw the shape

            pause()             # Wait before returning to menu


        elif choice == "3":
            t.clear()           # Clear previous drawing

            size = get_size()   # get user input on size of drawing

            draw_triangle(size)     # Draw the shape

            pause()             # Wait before returning to menu


        elif choice == "4":
            # User chose to exit the program

            print("Goodbye!")   # Exit message

            pause()             # Wait for user to press Enter

            turtle.bye()        # Close the turtle graphics window

            return              # End the program completely

        else:
            print("Invalid choice. Please enter 1-4.")  # Error message

            pause()             # Pause so user can read the message


# This runs the main function when the script is executed

if __name__ == "__main__":
    main()           # Start the menu loop

    





