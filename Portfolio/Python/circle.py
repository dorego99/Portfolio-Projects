"""
Charles Valenca
SEC 290
Exercise Set 7
Febuary 27 2021
"""
#imports math
import math

#creates class for circle
class Circle:
#creates function and constructor for radius
    def __init__(self, radius):
        self.radius = radius
#creates math problem for the area of a circle
    def area(self):
        return math.pi * self.radius ** 2
#creates math problem for the circumference of a circle
    def circumference(self):
        return 2 * math.pi * self.radius
#changes the self.radius tag to new_radius
    def change_radius(self, new_radius):
        self.radius = new_radius

#creates f\variable circle from the class Circle
circle = Circle(7)
# creates while true statement for the math solutions
while True:
    radius = float(input("Circle radius: "))
    circle.change_radius(radius)
#prints area and circumference of a circle based off of whatever the user inputs
    print("Area:", circle.area())
    print("Circumference:", circle.circumference())