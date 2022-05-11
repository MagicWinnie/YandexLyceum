from ast import Or


class NestingDoll:
    def __init__(self, size):
        self.size = size

    def __str__(self):
        return f"Russian Folk doll, size {self.size}."

    def get_size(self):
        return self.size


class OrdinaryNestingDoll(NestingDoll):
    def __init__(self, size, delta):
        self.size = size
        self.delta = delta

    def previous_doll(self):
        return OrdinaryNestingDoll(self.size + self.delta, self.delta)

    def next_doll(self):
        if self.size - self.delta > 0:
            return OrdinaryNestingDoll(self.size - self.delta, self.delta)
        return SmallestNestingDoll(self.size, self.delta)
    

class SmallestNestingDoll(OrdinaryNestingDoll):
    def __init__(self, size, delta):
        super().__init__(size, delta)

    def next_doll(self):
        return None
