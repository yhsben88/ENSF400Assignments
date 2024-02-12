import random
import string
import os

file_path = "/serverdata/random.txt"

if os.path.exists(file_path):
    # File exists, read and print existing content
    with open(file_path, "r") as file:
        existing_content = file.read()
        print("Existing Content:", existing_content)

# Generate new random text
new_content = ''.join(random.choices(string.ascii_letters + string.digits, k=100))

# Write new content to the file
with open(file_path, "w") as file:
    file.write(new_content)
    print("New Content:", new_content)
