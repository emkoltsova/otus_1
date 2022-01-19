from Figure import Figure


class Rectangle(Figure):

    def __init__(self, a, b):
        perimeter = 2 * (a + b)
        area = a * b
        super().__init__("Rectangle", area, perimeter)
