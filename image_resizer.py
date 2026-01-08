# Codemy.com - Instructor John Elder

# Course: Python Projects

# image_resizer.py

# project build date: Jan 7, 2026

# Modified instructors code to be more Pythonic and readable

"""Image Resizer App using Pillow."""

# Import modules

from PIL import Image
import os


"""
TODO (Future Upgrades):
- Add auto-numbering for output files to avoid overwriting.
- Auto-create missing folders when saving images.
- Add aspect-ratio lock option.
- Add preset sizes (e.g., 1080p, 720p, thumbnails).
"""


def clean_path(path):
    """Normalize and clean Windows paths (handles drag-and-drop)."""
    # Remove surrounding quotes (Windows adds these when dragging files)

    path = path.strip('"')
    # Normalize slashes so Pillow can read the path

    return os.path.normpath(path)


def clear_screen():
    """Clear the terminal screen."""

    os.system('cls' if os.name == 'nt' else 'clear')


def pause():
    """Pause the program until the user presses Enter."""

    input("\nPress Enter to continue...")


def get_user_int(prompt):
    """Ask the user for an integer until they enter a valid one."""

    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid number. Please try again.")


def get_image(path):
    """Load an image from disk and return the Image object."""

    try:
        img = Image.open(path)
        return img
    except FileNotFoundError:
        print("Image not found. Check the path and try again.")
        return None
    except Exception as e:
        print(f"Error loading image: {e}")
        return None
    

def resize_image(image, width, height):
    """Resize the image to the given width and height."""

    return image.resize((width, height))


def save_image(image, output_path):
    """Save the image to the given output path."""

    try:
        image.save(output_path)
        print(f"Image saved to: {output_path}")
    except FileNotFoundError:
        print("Output path not found. Please check the folder and try again.")
    except Exception as e:
        print(f"Error saving image: {e}")


# ------------------------------------------------------------
# FUTURE UPGRADE IDEA:
# Add auto-numbering to prevent overwriting existing files.
# Example:
#   jungle.jpg      -> jungle_2.jpg
#   jungle_2.jpg    -> jungle_3.jpg
# This would make the app safer and more user-friendly.
# ------------------------------------------------------------


def main():
    """Main program flow for the Image Resizer App."""

    clear_screen()
    print("\n--- Image Resizer App ---\n")

    # 1. Ask for input image path

    input_path = clean_path(input("Enter the path of the image to resize: "))

    # 2. Load the image

    img = get_image(input_path)
    if img is None:
        return  # Stops program if image failed to load
    
    # 3. Show original size

    original_width, original_height = img.size
    print(f"Original size: {original_width} x {original_height}")

    # 4. Ask for new size

    new_width = get_user_int("Enter new width: ")
    new_height = get_user_int("Enter new height: ")

    # 5. Resize the image

    resized_img = resize_image(img, new_width, new_height)

    # 6. Ask for output path

    output_path = clean_path(input("Enter the output path for the resized image: "))

    if not output_path.lower().endswith(('.jpg', '.png', '.png', '.gif')):
        output_path += '.jpg'  # Default to JPEG
        print(f"No extension detected. Saving as: {output_path}")

    # 7. Save the resized image

    save_image(resized_img, output_path)

    # 8. Confirm to the user

    print(f"Image resized to: {new_width} x {new_height}")
    pause()


if __name__ == "__main__":
    main()






