import math

from Figure import Figure


class Circle(Figure):

    def __init__(self, r):
        perimeter = 2 * math.pi * r
        area = math.pi * r * r
        super().__init__("Circle", area, perimeter)
