import pytest

from src.Circle import Circle
from src.Rectangle import Rectangle
from src.Square import Square
from src.Triangle import Triangle


@pytest.fixture
def circle_one():
    circle = Circle(3)
    yield circle


@pytest.fixture
def triangle_one():
    triangle = Triangle(3, 4, 5)
    yield triangle


@pytest.fixture
def square_one():
    square = Square(7)
    yield square


@pytest.fixture
def rectangle_one():
    rectangle = Rectangle(7, 8)
    yield rectangle


@pytest.fixture
def triangle_err():
    triangle = Triangle(1, 2, 3)
    yield triangle
