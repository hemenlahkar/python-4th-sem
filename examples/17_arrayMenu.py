def inputArray(lst):
    n = int(input("\033[1;33mEnter size of the array:\033[0;0m "))

    for _ in range(n):
        temp = int(input("Enter element: "))
        lst.append(temp)

def printEven(lst):
    for x in lst:
        if x % 2 == 0:
            print(f"{x:2d}", end=" ")
    print()

def printOdd(lst):
    for x in lst:
        if x % 2:
            print(f"{x:2d}", end=" ")
    print()
    
def printSumAvg(lst):
    s = sum(lst)
    avg = s / len(lst)
    print(f"Sum = {s:2d}\tAverage = {avg:.3f}")

def printMaxMin(lst):
    mn = min(lst)
    mx = max(lst)

    print(f"Min element: {mn}\nMax element: {mx}")

def removeDuplicate(lst):
    lst = list(set(lst))
    return lst

def printReverse(lst):
    print(list(reversed(lst)))

def printMenu(lst = None):
    if lst == None:
        lst = []
        inputArray(lst)

    while True:
        print("\n0. Print the array")
        print("1. Print even-valued elements.")
        print("2. Print odd-valued elements.")
        print("3. Calculate and print sum and average of all elements.")
        print("4. Print maximum and minimum element.")
        print("5. Remove duplicate elements")
        print("6. Print the array in reverse order")
        print("7. Re-enter the array")
        print("8. quit")
        
        i = int(input("\033[1;33mEnter your choice number:\033[0;0m "))
        
        print("\033[1;32m")
        match i:
            case 0:
                print(lst)
            case 1:
                printEven(lst)
            case 2:
                printOdd(lst)
            case 3:
                printSumAvg(lst)
            case 4:
                printMaxMin(lst)
            case 5:
                lst = removeDuplicate(lst)
            case 6:
                printReverse(lst)
            case 7:
                inputArray(lst)
            case 8:
                print("\033[0;0m", end="")
                return 1
        print("\033[0;0m", end="")

printMenu()