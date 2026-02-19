# Write a program to take two matrices from the user and find the sum and product of both.

def printMatrix(m):
    if m == None:
        return
    for i in m:
        for j in i:
            print(j, end=" ")
        print()

def getSum(m, n):
    if len(m) != len(n) or len(m[0]) != len(n[0]):
        print("Unable to add matrix: Unsupported dimensions!")
        return None
    temp_matrix = []
    
    for i in range(len(m)):
        curr_row = []
        for j in range(len(m[0])):
            curr_row.append(m[i][j] + n[i][j])
        temp_matrix.append(curr_row)
    return temp_matrix


def getProd(m, n):
    if len(m[0]) != len(n):
        return None
    
    temp_matrix = []
    for i in range(len(m)):
        curr_row = []
        for j in range(len(n[0])):
            curr_sum = 0
            for k in range(len(n[0])):
                curr_sum += m[i][k] * n[k][j]
            curr_row.append(curr_sum)
        temp_matrix.append(curr_row)
    return temp_matrix


matrix1, matrix2 = [], []
n = int(input("Enter no. of rows of first matrix: "))

print("Enter elements of the first matrix:")
for i in range(n):
    temp_list = [int(x) for x in input().split()]
    matrix1.append(temp_list)

n = int(input("Enter no. of rows of second matrix: "))

print("\nEnter elements of the second matrix:")
for i in range(n):
    temp_list = [int(x) for x in input().split()]
    matrix2.append(temp_list)

print("\nSum of the given matrices: ")
printMatrix(getSum(matrix1, matrix2))
print("\nProduct of the given matrices: ")
printMatrix(getProd(matrix1, matrix2))