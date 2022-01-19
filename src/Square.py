from Figure import Figure


class Square(Figure):

    def __init__(self, a):
        perimeter = 4 * a
        area = a * a
        super().__init__("Square", area, perimeter)
