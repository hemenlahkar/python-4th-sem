def swap(a, b):
    return b, a

[a, b] = [int(x) for x in input("Enter two numbers: ").split()]

print("\nBefore swap:\ta =", a, "b =", b)
a, b = swap(a, b)
print("After swap:\ta =", a, "b =", b)