import os
import re
import time
from just_playback import Playback
from tkinter import filedialog
import cv2
import threading
playback = Playback()
def sort_files_by_number(directory):

  files = []
  pattern = r'frame(\d+).bmp.txt'

  for root, _, filenames in os.walk(directory):
    for filename in filenames:
      if filename.endswith(".bmp_ascii.txt"):
        match = re.search(pattern, filename)
        number = int(match.group(1)) if match else 0
        files.append((number, os.path.join(root, filename)))

  return [f[1] for f in sorted(files)]  # Extract file paths from sorted list

def playAudio():
  playback.load_file('output.wav')
  playback.play()

def display_file_content(file_paths):
  framecount = 0
  video_path = str(filedialog.askopenfilename())
  cap = cv2.VideoCapture(video_path)
  fps = cap.get(cv2.CAP_PROP_FPS)
  totalFrames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
  playAudio()
  for file_path in file_paths:
    with open(file_path, 'r') as file:
      os.system("cls")
      content = file.read()
      print(content)
      time.sleep(1/fps)


directory = os.getcwd()
sorted_file_list = sort_files_by_number(directory)
display_file_content(sorted_file_list)
