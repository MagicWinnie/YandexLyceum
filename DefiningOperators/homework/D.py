from typing import List


class PearsBasket:
    def __init__(self, n: int):
        self.n = n

    def __floordiv__(self, number: int) -> List:
        arr = [PearsBasket(self.n // number) for _ in range(number)]
        if self.n % number != 0:
            arr += [PearsBasket(self.n % number)]
        return arr

    def __mod__(self, number: int) -> int:
        return self.n % number

    def __add__(self, other):
        return PearsBasket(self.n + other.n)

    def __sub__(self, number: int):
        self.n -= number
        self.n = max(0, self.n)

    def __str__(self):
        return str(self.n)

    def __repr__(self):
        return f"PearsBasket({self.n})"
