from src.class_rectangle import Rectangle
from src.class_circle import Circle
from src.class_square import Square
from src.class_triangle import Triangle
import pytest


@pytest.mark.smoke
def test_rectangle(rectangle_data_d):
    side_a, side_b, name = rectangle_data_d
    r = Rectangle(side_a, side_b)
    assert name
    assert r.get_area() == 15
    assert r.get_perimeter() == 16


# @pytest.mark.parametrize(("side_a", "side_b", "area", "perimeter"),
#                          [(4, 6, 24, 20),
#                           (5, 10, 50, 30)])
@pytest.mark.parametrize(("side_a", "side_b", "area", "perimeter"), [(0, 0, 0, 0)])
def test_rectangle_negative(side_a, side_b, area, perimeter):
    with pytest.raises(ValueError):
        r = Rectangle(side_a, side_b)
        assert r.name == f"Rectangle"
        assert r.get_area() == area
        assert r.get_perimeter() == perimeter


def test_add_area_negative(circle_data_n):
    r = Rectangle(2, 5)
    c = Circle(10)
    assert c.add_area(r) == 324.1592653589793


@pytest.mark.parametrize(("side_a", "area", "perimeter"), [(4, 16, 16), (5, 25, 20)])
def test_sq(side_a, area, perimeter):
    r = Square(side_a)
    assert r.name == "Square"
    assert r.get_area() == area
    assert r.get_perimeter() == perimeter


@pytest.mark.parametrize("rectangle_data", ["integer", "float"])
def test_r(rectangle_data_w, rectangle_data):
    side_a, side_b, name = rectangle_data_w(data=rectangle_data)
    r = Rectangle(side_a, side_b)
    assert r.name != name
    assert r.get_area() != 3
    assert r.get_perimeter() != 67


def test_add_area(square_data_sf):
    r = Rectangle(2, 5)
    s = Square(5)
    assert r.add_area(s) == 35


def test_triangle_area(triangle_data_d):
    side_a, side_b, side_c = triangle_data_d
    r = Triangle(side_a, side_b, side_c, name=Triangle)
    # s = Square(5)
    assert r.add_area(r) == 12.0
