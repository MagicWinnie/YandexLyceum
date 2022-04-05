class Butterfly:
    def __init__(self, volume):
        self.volume = volume
        self.used = 0

    def __iadd__(self, number):
        self.used += number
        self.used = max(0, min(self.volume, self.used))
        return self

    def __add__(self, other):
        return Butterfly(self.volume + other.volume)

    def __floordiv__(self, other):
        res = [Butterfly(self.volume // other) for _ in range(other)]
        if self.volume % other != 0:
            res += [Butterfly(self.volume % other)]
        return res

    def __str__(self):
        return f"Volume: {self.volume}, content: {self.used}"

    def __repr__(self):
        return f"Butterfly({self.volume})"
