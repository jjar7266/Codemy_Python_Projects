# Codemy.com - Instructor John Elder

# arrows.py

# Modified instructors code to be more Pythonic and readable

# Import modules
from pynput import keyboard
import os 

# Clear the screen
os.system("cls")

def on_press(key):
    print("DEBUG RAW:", key)
    # 1. Handle normal keys (letters, numbers, symbols)

    try:
        char = key.char

        # Exit on 'q'
        if char == 'q':
            print("Exiting... ")
            return False
        
        # Print any normal key
        print(f"Pressed: {char}")
        return
    
    except AttributeError:
        # 2. Handle special keys (arrows, shift, ctrl, etc.)

        if key == keyboard.Key.up:
            print("up")
        elif key == keyboard.Key.down:
            print("down")
        elif key == keyboard.Key.left:
            print("left")
        elif key == keyboard.Key.right:
            print("right")
        else:
            # 3. Any other special key
            print(f"Pressed: {key}")

def on_release(key):
    # Print release events for everything

    try:
        print(f"Released: {key.char}")
    except AttributeError:
        if key == keyboard.Key.up:
            print("Released: up")
        elif key == keyboard.Key.down:
            print("Released: down")
        elif key == keyboard.Key.left:
            print("Released: left")
        elif key == keyboard.Key.right:
            print("Released: right")
        else:
            print(f"Released: {key}")

with keyboard.Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()


