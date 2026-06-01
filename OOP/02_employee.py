'''
Define a class "employee" with the following specifications
    empno: integer
    ename: 20 characters
    basic, hra, da: float
    calculate(): a function to compute net pay as basic+hra+da with float return type
    getdata(): a function to read values for empno, ename, basic, hra, da.
    dispdata(): a function to display all the data on the screen
Write a main program to test the program
'''

class employee:
    def __init__(self):
        self.empno:int = -1
        self.ename:str = ''
        self.basic:float = 0.0
        self.hra:float = 0.0
        self.da:float = 0.0
    
    def getdata(self) -> None:
        self.empno = int(input("Enter the employee no.: "))
        self.ename = input("Enter the employee name: ")
        self.basic = float(input("Enter the basic pay: "))
        self.hra = float(input("Enter the HRA: "))
        self.da = float(input("Enter the DA: "))

    def calculate(self) -> float:
        return self.basic + self.hra + self.da

    def dispdata(self) -> None:
        print("\n\033[1;32m==== Employee Details ====\033[0m")
        print("Employee No. :", self.empno)
        print("Employee Name:", self.ename)
        print("Salary       :", self.calculate())
        print()
    
def main():
    e1 = employee()
    e1.getdata()
    e1.dispdata()
    
if __name__ == '__main__':
    main()