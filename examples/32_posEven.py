'''
Write a program to implement array initialized
with the numbers divisible by three up to 30.
Write a function which accepts the array and
return the positions of the even numbers in the array.
'''

def getEvenIndices(arr):
    result = []

    for i in range(0, len(arr)):
        if arr[i] % 2 == 0:
            result.append(i)
    return result

array = [x for x in range(3, 31, 3)]

print("\033[33m{:>27}\033[0m".format("Initial array ="), array)
print("\033[33mPosition of even elements =\033[0m", getEvenIndices(array))