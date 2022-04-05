class Unicorn:
    def __init__(self, length, level):
        self.length = length
        self.level = level

    def __iadd__(self, other):
        if type(other) == tuple:
            self.length += other[0]
            self.level += other[1]

            self.length = max(0, min(10, self.length))
            self.level = max(1, min(100, self.level))

        return self

    def __add__(self, other):
        if isinstance(other, Unicorn):
            return Unicorn(
                max(0, min(10, self.length + other.length)),
                max(1, min(100, self.level + other.level)),
            )

    def __floordiv__(self, other):
        return [
            Unicorn(
                self.length // other,
                self.level // other,
            ) for _ in range(other)
        ]

    def __str__(self):
        return f"Unicorn has corn of {self.length} and degree of {self.level}"

    def __repr__(self):
        return f"Unicorn({self.length}, {self.level})"
