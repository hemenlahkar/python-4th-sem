# Write a program to find the smallest or greatest of three numbers given as input.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

largest = smallest = 0

if a > b and a > c:
    largest = a
    if b < c:
        smallest = b
    else:
        smallest = c
elif b > c:
    largest = b
    if a < c :
        smallest = a
    else:
        smallest = c
else:
    largest = c
    if b < a:
        smallest = b
    else:
        smallest = a
        
print(f"Smallest: {smallest}\nLargest: {largest}")