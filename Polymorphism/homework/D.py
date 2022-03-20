class TypeStatistics:
    def __init__(self, lst):
        self.lst = lst

    def type_values(self):
        d = {}
        for el in self.lst:
            t = el.__class__.__name__
            if t not in d:
                d[t] = []
            d[t].append(el)
        return d

    def type_counts(self):
        d = {}
        for el in self.lst:
            t = el.__class__.__name__
            if t not in d:
                d[t] = 0
            d[t] += 1
        return d
