from PIL import Image

def clean_and_resize(input_file, output_file, size=(150, 150)):
    img = Image.open(input_file).convert("RGBA")

    datas = img.getdata()
    new_data = []
    for item in datas:
        if item[0] > 240 and item[1] > 240 and item[2] > 240:
            new_data.append((255, 255, 255, 0))
        else:
            new_data.append(item)

    img.putdata(new_data)

    bbox = img.getbbox()
    img = img.crop(bbox)

    img = img.resize(size, Image.LANCZOS)
    img.save(output_file, "PNG")
    print(f"Saved cleaned image: {output_file}")

# Match your actual filenames
clean_and_resize("images/Rock.png", "images/rock_clean.png")
clean_and_resize("images/Paper.png", "images/paper_clean.png")
clean_and_resize("images/Scissors.png", "images/scissors_clean.png")