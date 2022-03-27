class ChairLeg:
    def __init__(self, value):
        self.length = value

    def __mul__(self, other):
        self.length *= other

    def __rmul__(self, other):
        self.length *= other

    def __floordiv__(self, other):
        self.length //= other

    def __mod__(self, other):
        return self.length % other
