import math

from Figure import Figure


class Triangle(Figure):

    def __init__(self, a, b, c):
        perimeter = a + b + c
        area = math.sqrt(
            perimeter * (perimeter / 2 - a) * (perimeter / 2 - b) * (perimeter / 2 - c) / 2)
        super().__init__("Triangle", area, perimeter)

    def __new__(cls, a, b, c):
        if a + b > c and a + c > b and b + c > a:
            return super().__new__(cls)
        else:
            return None
