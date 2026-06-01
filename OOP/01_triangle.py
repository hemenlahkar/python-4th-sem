"""
Define a class named "triangle" to represent a triangle using the lenghts of the three sides.
Write a constructor to initialize objects of this class, given the lengths of the sides.
Also write member functions to check
    a) if a triangle is isosceles
    b) if a triangle is equilateral
Write main function to test your functions.
"""

class triangle:
    def __init__(self, x=0, y=0, z=0):
        self.a, self.b, self.c = x, y, z
    
    def isIsosceles(self):
        if self.a == self.b and self.a != self.c:
            return True
        if self.b == self.c and self.b != self.a:
            return True
        if self.c == self.a and self.c != self.b:
            return True
        return False
    
    def isEquilateral(self):
        if self.a == self.b and self.a == self.c:
            return True
        return False
    
def main():
    t = triangle(4, 4, 3)
    print("For triangle (4, 4, 3): ")
    print("\tIsosceles  : ", "Yes" if t.isIsosceles() else "No")
    print("\tEquilateral: ", "Yes" if t.isEquilateral() else "No")

if __name__ == "__main__":
    main()