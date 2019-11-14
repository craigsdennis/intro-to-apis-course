"""Lists files and directories in the current working directory."""

import os

current_dir = os.getcwd()
for entry in os.listdir(current_dir):
    print(entry)