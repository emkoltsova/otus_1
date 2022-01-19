import pytest

from src.Circle import Circle
from src.Rectangle import Rectangle
from src.Square import Square
from src.Triangle import Triangle


def test_circle_object(circle_one):
    assert isinstance(circle_one, Circle)
    assert circle_one.name == "Circle"


def test_triangle_object(triangle_one):
    assert isinstance(triangle_one, Triangle)
    assert triangle_one.name == "Triangle"


def test_square_object(square_one):
    assert isinstance(square_one, Square)
    assert square_one.name == "Square"


def test_rectangle_object(rectangle_one):
    assert isinstance(rectangle_one, Rectangle)
    assert rectangle_one.name == "Rectangle"


def test_circle_triangle_sum_area(circle_one, triangle_one):
    assert circle_one.add_area(triangle_one) == circle_one.area + triangle_one.area
    assert triangle_one.add_area(circle_one) == circle_one.area + triangle_one.area


def test_square_rectangle_sum_area(square_one, rectangle_one):
    assert square_one.add_area(rectangle_one) == square_one.area + rectangle_one.area
    assert rectangle_one.add_area(square_one) == square_one.area + rectangle_one.area


def test_circle_triangle_sum_area(circle_one, triangle_one):
    assert circle_one.add_area(triangle_one) == circle_one.area + triangle_one.area
    assert triangle_one.add_area(circle_one) == circle_one.area + triangle_one.area


def test_square_rectangle_sum_area(square_one, rectangle_one):
    assert square_one.add_area(rectangle_one) == square_one.area + rectangle_one.area
    assert rectangle_one.add_area(square_one) == square_one.area + rectangle_one.area


def test_circle_triangle_sum_perimeter(circle_one, triangle_one):
    assert circle_one.add_perimeter(triangle_one) == circle_one.perimeter + triangle_one.perimeter
    assert triangle_one.add_perimeter(circle_one) == circle_one.perimeter + triangle_one.perimeter


def test_square_rectangle_sum_perimeter(square_one, rectangle_one):
    assert square_one.add_perimeter(rectangle_one) == square_one.perimeter + rectangle_one.perimeter
    assert rectangle_one.add_perimeter(square_one) == square_one.perimeter + rectangle_one.perimeter


def test_sum_fail(circle_one):
    with pytest.raises(Exception) as e_info:
        circle_one.add_area(100)
    assert e_info.value.args[0] == "Only Figure class!"


def test_triangle_fail(triangle_err):
    assert triangle_err is None
