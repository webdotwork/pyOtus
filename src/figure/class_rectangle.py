from class_figure import Figure


class Rectangle(Figure):
    """ """

    def __init__(self, side_a, side_b, name="Rectangle"):
        super().__init__(name)
        if side_a <= 0 or side_b <= 0:
            raise ValueError("нельзя создать прямоугольник")
        self.side_a = side_a
        self.side_b = side_b
        self.name = name if name else "Rectangle"

    def get_area(self):
        return self.side_a * self.side_b

    def get_perimeter(self):
        return 2 * (self.side_a + self.side_b)
