'''
Define a class "circle" to represent circles. Add a member
radius to store the radius of a circle. Write member functions
area() and perimeter() to compute the area and perimeter of a circle.
'''

class Circle:
    def __init__(self, r=0):
        self.radius = r
    
    def area(self):
        return 3.14159 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14159 * self.radius

def main():
    c = Circle(5)

    print("\n\033[32mFor circle with radius 5:\033[0m")
    print("\tArea     :", c.area())
    print("\tPerimeter:", c.perimeter())
    
if __name__ == '__main__':
    main()