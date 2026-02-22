'''
Write a program that opens a file for reading
and displays the contents of the file character by
character and line by line on the screen.
'''

print("\033[1;32m")
print("-" * 40)
print("{:^40}".format("Character by Character"))
print("-" * 40, end="\033[0m\n")

with open("27_textfile.txt", "rt") as f:
    content = f.read()

    for i in content:
        print(i, end=" ")
        
print("\033[1;32m")
print("-" * 40)
print("{:^40}".format("Character by Character"))
print("-" * 40, end="\033[0m\n")

with open("27_textfile.txt", "rt") as f:
    for lines in f.readlines():
        print(lines)
        
        
print("\033[1;31m")
print("="*40, end="\033[0m")