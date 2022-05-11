class RegularPolygon:
    def __init__(self, sides=3) -> None:
        self.sides = sides
        self.deg = round(180 * (self.sides - 2) / self.sides, 2)

    def inner_corner(self) -> float:
        return self.deg
    
    def __repr__(self) -> str:
        if self.__class__.__name__ in ["Square", "Triangle", "Hexagon"]:
            return f"{self.__class__.__name__}, {self.deg} degree, {self.sides} sides"    
        return f"{self.__class__.__name__}, {self.deg} degree"


class Square(RegularPolygon):
    def __init__(self, size):
        super().__init__(4)
        self.size = size

    def area(self):
        return self.size ** 2

    def perimeter(self):
        return 4 * self.size


class Triangle(RegularPolygon):
    def __init__(self, size):
        super().__init__()
        self.size = size

    def area(self):
        return round(3 ** .5 / 4 * self.size ** 2, 2)

    def perimeter(self):
        return 3 * self.size

    
class Hexagon(Triangle):
    def __init__(self, size):
        super(Triangle, self).__init__(6)
        self.size = size

    def area(self):
        return round(6 * super().area(), 2)

    def perimeter(self):
        return 2 * super().perimeter()

    def circumcircle(self):
        return round(3 ** .5 / 2 * self.size, 2)
