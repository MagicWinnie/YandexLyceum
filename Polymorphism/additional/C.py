from math import factorial


class EulerNumber:
    def __init__(self, n):
        self.n = n

    def get_number(self, x=1):
        self.e = 0
        for i in range(self.n):
            self.e += x ** i / factorial(i)
        return self.e
