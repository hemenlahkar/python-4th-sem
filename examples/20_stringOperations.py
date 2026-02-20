text = input("\033[1;33mEnter the string: \033[0;37m")

i = True
while i:
    print("\n\033[0;32m0. Print the string")
    print("1. Convert all lowercase characters to uppercase")
    print("2. Convert all uppercase characters to lowercase")
    print("3. Calculate number of vowels in the string")
    print("4. Reverse the string")
    print("5. Concatinate two string")
    print("6. Compare two string")
    print("7. Copy one string to another")
    print("8. quit")

    choice = int(input("\033[1;33mEnter choice number: \033[0m"))
    
    print("\n" + "-" * 50)
    
    match choice:
        case 0:
            print(text)
        case 1:
            text = text.lower()
        case 2:
            text = text.upper()
        case 3:
            vowel = "aeiou"
            temp = [x.lower() in vowel for x in text]
            print("No. of vowels: ", temp.count(True))
        case 4:
            text = text[::-1]
            print(text)
        case 5:
            text2 = input("Enter second string: ")
            text = text + text2
            print("After concatination:", text)
        case 6:
            text2 = input("Enter second string: ")
            if text == text2:
                print(f"Both strings \"{text}\" and \"{text2} are equal.")
            elif text > text2:
                print(f"The string \"{text}\" is lexicographically greater than \"{text2}\"")
            else:
                print(f"The string \"{text}\" is lexicographically smaller than \"{text2}\"")
        case 7:
            text = input("Enter the string to be copied: ")
            print("After copying, string =", text)
        case 8:
            i = False