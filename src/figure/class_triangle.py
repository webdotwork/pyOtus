import math
from class_figure import Figure


class Triangle(Figure):
    """
    class Triangle
    side: int - takes Side integer
    """

    def __init__(self, side_a, side_b, side_c, name):
        super().__init__(name="Triangle")
        if (
            side_a <= 0
            or side_b <= 0
            or side_c <= 0
            or side_a + side_b <= side_c
            or side_a + side_c <= side_b
            or side_b + side_c <= side_a
        ):
            raise ValueError("нельзя создать треугольник")
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def get_area(self):
        s = self.get_perimeter() / 2
        return math.sqrt(s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c))

    def get_perimeter(self):
        return self.side_a + self.side_b + self.side_c
