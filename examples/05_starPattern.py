'''
Write a program to print a triangle of stars as follows (take number of lines from user):

    *
   ***
  *****
 *******
*********
'''

n = int(input("Enter number of lines: "))

for i in range(n):
    print(" " * (n - 1 - i), "*" * (2 * i + 1))