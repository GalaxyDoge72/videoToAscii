import os
from PIL import Image
import numpy as np
from tkinter import filedialog

directory = os.getcwd()
files = []
import os

directory = os.getcwd()
files = []
for root, _, filenames in os.walk(directory):  
    for file in filenames:
        if file.endswith(".bmp"):
            files.append(os.path.join(root, file))

cols = int(input("How many columns to use: "))

for item in files:
    img = Image.open(item).convert('RGB')

    width, height = img.size
    aspect_ratio = height / width
    new_height = int(cols * aspect_ratio)
    img = img.resize((cols, new_height))

    img_array = np.array(img)
    ascii_chars = ["@", "#", "$", "%", "*", "+", "-", ".", " "]


    
    min_val, max_val = img_array.min(), img_array.max()
    char_range = max_val - min_val
    char_ratio = char_range / len(ascii_chars)
    ascii_str = ""
    for y, row in enumerate(img_array):
        for x, _ in enumerate(row):  # Use _ to discard unused value
            pixel_value = img.getpixel((x, y))
            red, green, blue = pixel_value

            # Convert RGB to a single value for character mapping
            gray_value = int(0.2126 * red + 0.7152 * green + 0.0722 * blue)

            # Calculate character index
            char_index = int((gray_value - min_val) / char_ratio)
            char_index = max(0, min(len(ascii_chars) - 1, char_index))

            # Create ANSI escape sequence for color
            color_code = f"\033[38;2;{red};{green};{blue}m"
            ascii_str += color_code + ascii_chars[char_index] + "\033[0m"
        ascii_str += "\n"
        ascii_filename = f"{item}_ascii.txt"
        with open(ascii_filename, "w") as f:
            f.write(ascii_str)