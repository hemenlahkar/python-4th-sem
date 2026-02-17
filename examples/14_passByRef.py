# Write a program in which a function is passed address of two variables and then alter its contents.
def swap(lst):
    lst[0], lst[1] = lst[1], lst[0]

values = [5, 10]
print(f"Before: x = {values[0]}, y = {values[1]}")
swap(values)
print(f"After: x = {values[0]}, y = {values[1]}")