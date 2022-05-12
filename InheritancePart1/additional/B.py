class RealGhost:
    def __init__(self, feat=""):
        self.feat = feat.split()
        self.feat_sorted = sorted(self.feat)

    def __repr__(self):
        return f"RealGhost('{' '.join(self.feat_sorted)}')"


class ModelGhost(RealGhost):
    def __init__(self, feat="", name=""):
        super().__init__(feat)
        self.name = name

    def __getitem__(self, key):
        return self.feat_sorted[key]

    def add(self, value):
        self.feat.append(value)
        self.feat_sorted = sorted(self.feat)

    def pop(self, key):
        it = self.feat[self.feat.index(self.feat_sorted[key])]
        del self.feat[self.feat.index(self.feat_sorted[key])]
        self.feat_sorted = sorted(self.feat)
        return it

    def __iter__(self):
        return iter(self.feat_sorted)

    def __len__(self):
        return len(self.feat)

    def __repr__(self):
        return f"ModelGhost('{' '.join(self.feat_sorted)}', name='{self.name}')"
