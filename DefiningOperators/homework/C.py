class FlowingRectangle:
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b
        self.koeff = a / b

    def get_width(self) -> float:
        return round(self.a, 2)

    def get_height(self) -> float:
        return round(self.b, 2)

    def __add__(self, other):
        if self.a == 0:
            s2 = other.a * other.b
            self.b = (s2 / self.koeff)**.5
            self.a = self.koeff * self.b
            return

        s1 = self.a * self.b
        s2 = other.a * other.b

        k = ((s1 + s2) / (s1))**.5

        self.a *= k
        self.b *= k

    def __sub__(self, other):
        s1 = self.a * self.b
        s2 = other.a * other.b

        if s1 < s2:
            self.a = 0
            self.b = 0
            return

        k = ((s1 - s2) / (s1))**.5

        self.a *= k
        self.b *= k
