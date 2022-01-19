class Figure:
    def __init__(self, name, area, perimeter):
        self.__name = name
        self.__area = area
        self.__perimeter = perimeter

    @property
    def name(self):
        return self.__name

    @property
    def area(self):
        return self.__area

    @property
    def perimeter(self):
        return self.__perimeter

    def add_area(self, second_figure):
        if not isinstance(second_figure, Figure):
            raise ValueError("Only Figure class!")
        return self.__area + second_figure.__area

    def add_perimeter(self, second_figure):
        if not isinstance(second_figure, Figure):
            raise ValueError("Only Figure class!")
        return self.__perimeter + second_figure.__perimeter
