def isPalindrome(str):
    return str == str[::-1]

x = input("Enter the string: ")

if isPalindrome(x):
    print(f"{x} is a Palindrome.")
else:
    print(f"{x} is NOT a Palindrome!")