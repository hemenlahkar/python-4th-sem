'''
Write a program to compute the sum of the first n terms of the following series
        S = 1+1/2+1/3+1/4+......
'''

n = int(input("Enter the number of terms: "))
s = 0

for i in range(1, n + 1):
    s += 1 / i
    
print(f"1 + 1/2 + 1/3 +...upto {n} terms = {s:.3f}")