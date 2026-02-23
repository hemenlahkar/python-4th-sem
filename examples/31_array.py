'''
Write a program to declare an array and 
initialize the values according to the user.
Now ask the user for a number n and
return the nth element from the array.
'''

array = [int(x) for x in input("Enter the elements of the array(separated by a space): ").split()]


index = -1
while index < 1 or index > len(array):
    index = int(input("Enter the index you want to visit(1 being first element): "))

print(f"\nThe {index}th element is: {array[index - 1]}")