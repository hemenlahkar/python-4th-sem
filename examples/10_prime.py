def isPrime(n):
    if n == 2:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    
    for i in range(3, n//2 + 1, 2):
        if n % i == 0:
            return False
    return True


for i in range(2, 100):
    if isPrime(i):
        print(f"{i:2d}", end=" ")