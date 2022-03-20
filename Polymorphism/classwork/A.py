from math import pi


class SquareIntoCircle:
    def __init__(self, radius):
        self.radius = 2 * radius / pi

    def size(self):
        return round(self.radius, 3)

    def area(self):
        return round(pi * self.radius ** 2, 3)


class CircleIntoSquare:
    def __init__(self, side):
        self.side = side * pi / 2

    def size(self):
        return round(self.side, 3)

    def area(self):
        return round(self.side ** 2, 3)
