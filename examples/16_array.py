# Write a program to create an array with inputs from the user and print the same.

n = int(input("Enter size of the array: "))

array = []

for _ in range(n):
    temp = int(input("Enter array element: "))
    array.append(temp)
    
print(array)