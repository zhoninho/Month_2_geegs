class Figure:
    unit = 'cm'
    def __init__(self):
        pass
    def calculate_area(self):
        pass
    def info(self):
        pass
class Square(Figure):
    def __init__(self, side_length):
        super().__init__()
        self.__side_length = side_length
    def calculate_area(self):
        return self.__side_length ** 2
    def info(self):
        print(f'Square side length: {self.__side_length}{Figure.unit}, area: {self.calculate_area()}{Figure.unit}.')

class Rectangle(Figure):
    def __init__(self, width, lenght):
        super().__init__()
        self.__width = width
        self.__lenght = lenght
    def calculate_area(self):
        return self.__width * self.__lenght
    def info(self):
        print(f'Rectangle length: {self.__lenght}{Figure.unit}, width: {self.__width}{Figure.unit}, area: {self.calculate_area()}{Figure.unit}.')

squares = [
    Square(5),
    Square(10)
]
rectangles = [
    Rectangle(5, 10),
    Rectangle(6, 20),
    Rectangle(7, 30),
]

for square in squares:
    square.info()
for rectangle in rectangles:
    rectangle.info()