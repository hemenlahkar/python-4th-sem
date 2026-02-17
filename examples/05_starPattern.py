n = int(input("Enter number of lines: "))

for i in range(n):
    print(" " * (n - 1 - i), "*" * (2 * i + 1))