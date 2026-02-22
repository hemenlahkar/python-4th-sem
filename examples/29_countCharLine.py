"""
Write a C program to open a file and
count the number of characters and lines in the file.
"""

with open("27_textfile.txt", "rt") as f:
    content = f.read()

print("Number of character:", len(content))
print("Number of lines:", content.count("\n") + 1)
