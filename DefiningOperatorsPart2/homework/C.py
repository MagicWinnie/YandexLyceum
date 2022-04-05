class ModularArithmetic:
    def __init__(self, val, mod):
        self.val = val
        self.mod = mod

    def __call__(self, other):
        return other // self.mod

    def __add__(self, other):
        return ModularArithmetic((self.val + other.val) % self.mod, self.mod)

    def __sub__(self, other):
        return ModularArithmetic((self.val - other.val) % self.mod, self.mod)

    def __rshift__(self, other):
        return ModularArithmetic((self.val + other) % self.mod, self.mod)

    def __lshift__(self, other):
        return ModularArithmetic((self.val - other) % self.mod, self.mod)

    def __str__(self):
        return f"{self.val}({self.mod})"

    def __repr__(self):
        return f"{self.val}({self.mod})"
