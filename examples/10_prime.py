def isPrime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    
    for i in range(3, n//2 + 1, 2):
        if n % i == 0:
            return False
    return True

n = int(input("Enter a number: "))

if isPrime(n):
    print(f"{n} is a Prime Number.")
else:
    print(f"{n} is NOT a prime number!")