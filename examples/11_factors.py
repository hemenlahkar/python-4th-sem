# Write a program to compute the factors of a given number

n = int(input("Enter the number: "))

print(f"Factors of {n} are: ", end=" ")
for i in range(1, n//2 + 1):
    if n % i == 0:
        print(f"{i}", end=" ")
print(n)