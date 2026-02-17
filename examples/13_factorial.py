# Write a program to calculate Factorial of a number (i) using recursion, (ii) using iteration

def factorial_recursion(n):
    if n <= 1:
        return 1
    return n * factorial_recursion(n - 1)

n = int(input("Enter the number: "))

print(f"By recursion: {n}! = {factorial_recursion(n)}")

factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(f"By iteration: {n}! = {factorial}")