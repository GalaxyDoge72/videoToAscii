import cv2
from tkinter import filedialog

# Open a file dialog to select the video
video_path = str(filedialog.askopenfilename())
print(f"Selected video path: {video_path}")

# Open the video capture object using the path
cap = cv2.VideoCapture(video_path)

# Check if video opened successfully
if not cap.isOpened():
    print("Error opening video!")
    exit()

frame_count = 0
output_dir = "extracted_frames"
import os
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    filename = os.path.join(output_dir, f"frame{frame_count}.bmp")
    cv2.imwrite(filename, frame)
    print(f"Wrote file: {filename}")

    frame_count += 1

import subprocess
command = f"ffmpeg -i '{video_path}' -vn -c:a pcm_s16le output.wav"
subprocess.run(command)

cap.release()

print("Finished processing video!")
