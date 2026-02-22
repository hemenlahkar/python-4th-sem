'''
Write a program that opens a file in append mode
and allows the user to add text to the end of the file.
'''

text = input("Enter what you want to append to the file: ")
with open("30_append.txt", "a") as f:
    f.write("\n" + text)

print("Append successful!")