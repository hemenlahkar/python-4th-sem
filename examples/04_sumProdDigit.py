a = int(input("Enter a number: "))
sum, prod = 0, 1

while a > 0:
    sum += a % 10
    prod *= a % 10
    a //= 10
    
print(f"Sum of digits = {sum}\nProduct of digits = {prod}")