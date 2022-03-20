class TigerLily:
    def __init__(self, t):
        self.t = t

    def add_theme(self, value):
        self.t += (value,)

    def shift_one(self):
        val = []
        val.append(self.t[-1])
        for i in range(len(self.t) - 1):
            val.append(self.t[i])
        self.t = tuple(val)

    def reverse_order(self):
        self.t = tuple(reversed(list(self.t)))

    def get_themes(self):
        return self.t

    def get_first(self):
        return self.t[0]
