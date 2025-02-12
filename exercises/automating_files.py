# This is a script to manage the files in a directory

import os

# Get the directory path
directory = input("Directory path: ")

# Change to the directory
os.chdir(directory)

for file in os.listdir():
    file_name, file_ext = os.path.splitext(file)


    print(file_name)