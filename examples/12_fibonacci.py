# Write a program to display Fibonacci series (i) using recursion, (ii) using iteration

n = int(input("Enter number of terms: "))

# Iteration
t1, t2 = 0, 1
print("By Iteration: ", end=" ")
for _ in range(n):
    print(t1, end=" ")
    t1, t2 = t2, t1 + t2
    
print("\nBy Recursion: ", end=" ")

def fibo_recursive(n):
    if n == 0 or n == 1:
        return n
    return fibo_recursive(n - 1) + fibo_recursive(n - 2)

for i in range(n):
    print(fibo_recursive(i), end=" ")