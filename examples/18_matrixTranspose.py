def printTranspose(m):
    print("Transpose of the given matrix:")
    for i in range(len(m[0])):
        for j in range(len(m)):
            print(m[j][i], end=" ")
        print()


n = int(input("Enter number of rows of the matrix: "))
matrix = []

for i in range(n):
    temp_list = [int(x) for x in input().split()]
    matrix.append(temp_list)

printTranspose(matrix)
