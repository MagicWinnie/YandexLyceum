class Dragonfly:
    def __init__(self, height):
        self.height = height

    def __iadd__(self, other):
        self.height += other
        self.height = max(1, min(30, self.height))
        return self

    def __add__(self, other):
        if isinstance(other, Dragonfly):
            return Dragonfly(max(1, min(30, self.height + other.height)))

    def __truediv__(self, number):
        if number == 0:
            return []
        if self.height // number <= 0:
            return []
        res = [None for _ in range(number)]
        for i in range(number):
            res[i] = Dragonfly(self.height // number)
        return res

    def __str__(self):
        return f"Dragonfly with a height of {self.height}"

    def __repr__(self):
        return f"Dragonfly({self.height})"
