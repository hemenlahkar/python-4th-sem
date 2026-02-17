'''
Write a program which takes the radius of a circle as input from the user, passes it to another
function that computes the area and the circumference of the circle and displays the value of area
and circumference from the main() function.
'''

def getAreaCircumference(r):
    result = {}
    result["area"] = 3.14 * r * r
    result["circumference"] = 2 * 3.14 * r
    return result

radius = float(input("Enter the radius of the circle: "))

result = getAreaCircumference(radius)

print(f"Area = {result["area"]:.3f}\nCircumference = {result["circumference"]:.3f}")