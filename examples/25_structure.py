"""
Write a program to implement struct in C.
Create a structure of Student with RNo, Name and
other credentials with proper datatype and print the same.
"""

class Student:
    def __init__(self):
        self.RNo = 0
        self.Name = ""
        self.mark = 0.0
        
    def inputDetails(self):
        self.RNo = int(input("Enter the roll no. of the student: "))
        self.Name = input("Enter the name of the student: ")
        self.mark = float(input("Enter the mark of the student: "))

    def printDetails(self):
        print("\n","-" * 30, sep="")
        print(f"{"Name":10}: {self.Name}")
        print(f"{"Roll no.":10}: {self.RNo}")
        print(f"{"Marks":10}: {self.mark}")
        print("-" * 30)

s1 = Student()
s1.inputDetails()
s1.printDetails()
    