'''
Write a function that checks whether a given string is Palindrome or not.
Use this function to find whether the string entered by user is Palindrome or not.
'''

def isPalindrome(str):
    return str == str[::-1]

x = input("Enter the string: ")

if isPalindrome(x):
    print(f"{x} is a Palindrome.")
else:
    print(f"{x} is NOT a Palindrome!")