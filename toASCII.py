import os
import numpy as np
from PIL import Image

## Locate all image files ##
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
    for row in img_array:
        for pixel in row:
            char_index = int((pixel - min_val) / char_ratio)
            char_index = max(0, min(len(ascii_chars) - 1, char_index))
            ascii_str += ascii_chars[char_index]
        ascii_str += "\n"
          # Clamp to valid range
        ascii_str += ascii_chars[char_index]
        ascii_filename = f"{item}_ascii.txt"
        with open(ascii_filename, "w") as f:
            print(f"Wrote Pixel: {pixel}")
            f.write(ascii_str)

txtfiles = []
for root, _, filenames in os.walk(directory):  
    for file in filenames:
        if file.endswith(".txt"):
            txtfiles.append(os.path.join(root, file))
