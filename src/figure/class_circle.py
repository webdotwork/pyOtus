import math
from class_figure import Figure


class Circle(Figure):
    def __init__(self, radius, name="Circle"):
        super().__init__(name)
        if radius <= 0:
            raise ValueError("нельзя создать круг")
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius**2

    def get_perimeter(self):
        return 2 * math.pi * self.radius
