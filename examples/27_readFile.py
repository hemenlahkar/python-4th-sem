"""
Write a C program that opens a file for reading and
displays the contents of the file in binary mode and text mode.
"""

print("\033[1;32m")
print("-" * 40)
print("{:^40}".format("Text content"))
print("-" * 40, end="\033[0m\n")

with open("27_textfile.txt", "rt") as f:
    print(f.read())
    
print("\033[1;32m")
print("-" * 40)
print("{:^40}".format("Binary content (as hex)"))
print("-" * 40, end="\033[0m\n")

with open("27_textfile.txt", "rb") as f:
    content = f.read().hex()
    for i in range(len(content)//2):
        print(content[i:i+2], end=" ")
        if (i + 1) % 10 == 0:
            print()
    print()

print("\n\033[1;31m", "-" * 40, sep="", end="\033[0m\n")
