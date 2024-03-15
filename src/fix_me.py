"""
modul docstring.
"""

from class_circle import Circle
from class_square import Square
from class_triangle import Triangle


def calculate_average(numbers):
    """
    function docstring
    """
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    return average


nums = [10, 15, 20]
result = calculate_average(nums)
print("The average is:", result)

s = Square(3)
print("Square Area:", s.get_area())
print("Square Perimeter:", s.get_perimeter())

t = Triangle(3, 4, 5, "Triangle")
print("Triangle Area:", t.get_area())
print("Triangle Perimeter:", t.get_perimeter())

c = Circle(5, "Circle")
print("Circle Area:", c.get_area())
print("Circle Perimeter:", c.get_perimeter())
