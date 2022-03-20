from math import pi


class Square:
    def __init__(self, size):
        self.area = size * size

    def extrude(self, h):
        return self.area * h


class Rectangle:
    def __init__(self, a, b):
        self.area = a * b

    def extrude(self, h):
        return self.area * h


class Triangle:
    def __init__(self, size):
        self.area = 3 ** 0.5 / 4 * size * size

    def extrude(self, h):
        return self.area * h


class Circle:
    def __init__(self, size):
        self.area = pi * size * size

    def extrude(self, h):
        return self.area * h
