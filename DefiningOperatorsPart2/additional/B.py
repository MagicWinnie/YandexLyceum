class OpticSystem:
    def __init__(self, lenses):
        self.lenses = lenses[:]

    def __iter__(self):
        return iter(self.lenses)

    def __getitem__(self, key):
        return self.lenses[key]

    def __delitem__(self, key):
        del self.lenses[key]

    def __setitem__(self, key, value):
        self.lenses[key] = value

    def append(self, value):
        self.lenses.append(value)

    def __len__(self):
        return len(self.lenses)

    def __eq__(self, other):
        return (sum(self.lenses), len(self.lenses)) ==\
            (sum(other.lenses), len(other.lenses))

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        return (sum(self.lenses), len(self.lenses)) <\
            (sum(other.lenses), len(other.lenses))

    def __gt__(self, other):
        return not self.__lt__(other)

    def __le__(self, other):
        return (sum(self.lenses), len(self.lenses)) <=\
            (sum(other.lenses), len(other.lenses))

    def __ge__(self, other):
        return not self.__le__(other)

    def __add__(self, other):
        return OpticSystem(self.lenses + other.lenses)

    def __iadd__(self, other):
        self.lenses += other.lenses
        return self

    def __call__(self, d):
        if d == 0:
            return None
        D = sum(self.lenses)
        if D * d - 1 == 0:
            return None
        f = d / (D * d - 1)
        return round(f, 4)

    def __rshift__(self, n):
        for _ in range(n):
            self.lenses = [self.lenses[-1]] + self.lenses[:-1]

    def __lshift__(self, n):
        for _ in range(n):
            self.lenses = self.lenses[1:] + [self.lenses[0]]
