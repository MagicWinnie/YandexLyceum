class Hyperbole:
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    def __str__(self):
        if self.b > 0:
            return f"y = {self.a} + {self.b}/x"
        else:
            return f"y = {self.a} - {abs(self.b)}/x"

    def __repr__(self):
        return f"Hyp({self.a}, {self.b})"

    def __call__(self, x: float):
        if x == 0:
            return None
        else:
            return round(self.a + self.b / x, 6)
