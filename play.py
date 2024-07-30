import os
import re
import time

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

def display_file_content(file_paths):
  """Clears the screen and displays the content of each file in sorted order.

  Args:
    file_paths: A list of file paths in sorted order.
  """

  for file_path in file_paths:
    with open(file_path, 'r') as file:
      os.system('clear')  # Clear screen before displaying content
      content = file.read()
      print(content)
      time.sleep(0.0333)  # Pause for 0.333 seconds between files

# Example usage:
directory = os.getcwd()
sorted_file_list = sort_files_by_number(directory)
display_file_content(sorted_file_list)
