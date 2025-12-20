# Codemy.com - Instructor John Elder

# arrows_tkinter.py

# Modified instructors code to be more Pythonic and readable

# Import modules

import tkinter as tk

# Event Handlers
def on_key(event):

    key = event.keysym

    # Exit on 'q'
    if key == "q":
        print("Exiting... ")
        root.destroy()
        return
    
    # Arrow keys
    if key == "Up":
        print("up")
    elif key == "Down":
        print("down")
    elif key == "Left":
        print("left")
    elif key == "Right":
        print("right")
    else:
        # Any other key
        print(f"Pressed: {key}")

# UI Setup: (User Interface)

def build_ui(root):

    label = tk.Label(root, text = "Press arrow keys or any key. Press 'q' to exit.")
    label.pack(pady=40)

    # Bind ALL key presses
    root.bind("<Key>", on_key)

def main():

    global root
    root = tk.Tk()
    root.title("Arrows!")
    root.geometry("300x100")

    build_ui(root)
    root.mainloop()

if __name__ == "__main__":
    main()

