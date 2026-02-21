# Write a function to accept two arrays as argument and returns their sum as an array.

def addArray(l1, l2):
    result = []
    i = 0
    while i < len(l1) and i < len(l2):
        result.append(l1[i] + l2[i])
        i += 1
    while i < len(l1):
        result.append(l1[i])
    while i < len(l2):
        result.append(l2[i])
        
    return result

def sumArray(l1, l2):
    return [sum(l1), sum(l2)]

list1 = [int(x) for x in input("Enter elements of first array: ").split()]
list2 = [int(x) for x in input("Enter elements of second array: ").split()]

print("Sum of corresponding elements of the two array:", addArray(list1, list2))
print("Sum of each array:", sumArray(list1, list2))
    