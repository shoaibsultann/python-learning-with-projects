# Q3. Write a python program to print the contents of a directory using the os module.
# Search online for the function which does that. 

import os

# Specify the directory path

directory_path = "/Users/PKC"

# List all files and directories in the specified path
contents = os.listdir(directory_path)

# Print each item in the directory
for item in contents:
    print(item)