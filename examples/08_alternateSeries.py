n = int(input("Enter number of terms: "))

s, sign = 0, 1
for i in range(1, n + 1):
    s += sign * i
    sign *= -1

print(f"1 - 2 + 3 - ...upto {n} terms = {s}")