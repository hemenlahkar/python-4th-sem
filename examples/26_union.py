"""
Write a program to implement union in C.
Create a structure of Person with Pid, Name and other
credentials with proper datatype and print the same.
"""


class Person:
    def __init__(self):
        self.data = None

    def inputData(self):
        print("\n1. Name\n2. PId\n3. Annual Income\n4. quit the program")
        choice = int(input("\nEnter which field you want to fill: "))
        print()

        match choice:
            case 1:
                self.data = input("Enter name: ")
                print("Name have been stored successfully.")
            case 2:
                self.data = int(input("Enter person id: "))
                print("PId have been stored successfully.")
            case 3:
                self.data = float(input("Enter Annual Income: "))
                print("Annual Income have been stored successfully.")
            case 4:
                return 0
        print("Other fields were discarded!")
        return 1

    def printData(self):
        print("\n", "-" * 40, sep="")

        match str(type(self.data))[8:-2]:
            case "str":
                print("Name:", end="\t")
            case "int":
                print("PId:", end="\t")
            case "float":
                print("Annual Income:", end="\t")
        print(self.data)


p1 = Person()

while p1.inputData():
    p1.printData()
