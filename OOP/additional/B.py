class Quadratic:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.d = self.b * self.b - 4 * self.a * self.c 

    def branch(self):
        if self.a > 0:
            return "up"
        return "down"

    def x_sect(self):
        if self.d < 0:
            return 0
        elif self.d == 0:
            return 1
        else:
            return 2

    def calc(self, x):
        return self.a * x * x + self.b * x + self.c

    def sections(self):
        if self.d < 0:
            return None 
        elif self.d == 0:
            return (-self.b / (2 * self.a), self.calc(-self.b / (2 * self.a)))
        else:
            x1 = (-self.b + self.d**.5) / (2 * self.a)
            x2 = (-self.b - self.d**.5) / (2 * self.a)
            y1 = self.calc(x1)
            y2 = self.calc(x2)
            if x1 < x2 or (x1 == x2 and y1 < y2):
                return (x1, y1, x2, y2)
            return (x2, y2, x1, y1)

    def top(self):
        return (-self.b / (2 * self.a), self.calc(-self.b / (2 * self.a)))

    def y_sect(self):
        return (0, self.c)
