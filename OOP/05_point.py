"""
Define a class "point" with two data members "xordinate" and "yordinate"
to represent all points in the two-dimensional plane by storing their
x co-ordinate and y co-ordinate values. Write member funcions:
    dist(): to return the distance of the point from the origin
    slope(): to return the slope of the line obtained by joining
            this point with the origin.
  Write constructor with zero, one and two arguments to initialize objects.
  Also write a friend function to compute the distance between two points
"""

import math

class Point:
    def __init__(self, x=0, y=0):
        self.xordinate, self.yordinate = x, y

    def dist(self):
        return round(math.sqrt(self.xordinate**2 + self.yordinate**2), 2)

    def slope(self):
        return round(self.yordinate / self.xordinate, 2)
    
    
def distance(a: Point, b: Point):
    return round(math.sqrt((a.xordinate - b.xordinate)**2 + (a.yordinate - b.yordinate)**2), 2)

def main():
    a = Point(3, 4)
    b = Point(8)
    
    print("\nDistance of (3, 4) from origin =", a.dist())
    print("Slope of line connecting origin and (3, 4) =", a.slope())
    print("Distance between (3, 4) and (8, 0) is", distance(a, b))

if __name__ == '__main__':
    main()