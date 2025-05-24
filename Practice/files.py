#to play with code as you like
import os
file_path = 'C:/Users/narsi/OneDrive/Desktop/Bus fees.pdf'
if os.path.exists(file_path):
    print(f"File '{file_path}' exists.")
    if os.path.isfile(file_path):
        print(f"File '{file_path}' is a file.")
    elif os.path.isdir(file_path):
        print(f"File '{file_path}' is a directory.")
else:
    print(f"File '{file_path}' does not exist.")