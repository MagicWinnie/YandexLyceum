class Chubby:
    def __init__(self, name: str, money: int):
        self.name = name
        self.money = money

    def __iadd__(self, number: int):
        self.money += number
        self.money = max(0, self.money)
        return self

    def __add__(self, other):
        return Chubby(self.name + "-" + other.name, self.money + other.money)

    def __mul__(self, number: int):
        return [Chubby(self.name, self.money // number) for _ in range(number)]

    def __str__(self):
        return f"Chubby {self.name} has {self.money} coins"

    def __repr__(self):
        return f'Chubby("{self.name}", {self.money})'
