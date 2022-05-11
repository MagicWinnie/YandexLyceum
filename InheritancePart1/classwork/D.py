class ClassicalMechanics:
    def __init__(self, v):
        self.v = v

    def __call__(self, v_r):
        return self.v + v_r

    def __str__(self):
        return f"Object {self.__class__.__name__}, velocity {self.v} c"


class SpecialTheoryRelativity(ClassicalMechanics):
    def __call__(self, v_r):
        if self.v < 0.1 and v_r < 0.1:
            return ClassicalMechanics(self.v)(v_r)
        return (self.v + v_r) / (1 + self.v * v_r)
