class VoltaicPile:
    def __init__(self, mats):
        self.mats = mats
        self.current = -1

    def __getitem__(self, key):
        return self.mats[key]

    def __setitem__(self, key, value):
        self.mats[key] = value

    def __iter__(self):
        return iter(self.mats)

    def __len__(self):
        return len(self.mats)

    def __next__(self):
        self.current += 1
        if self.current < len(self.mats):
            return self.mats[self.current]
        raise StopIteration

    def append(self, other):
        if not self.mats:
            self.mats.append(other)
            return
        if self.mats[-1] == other:
            return
        if len(self.mats) == 1:
            if self.mats[-1] == "Cu" and other == "cloth":
                self.mats.append(other)
            elif self.mats[-1] == "cloth" and other == "Cu":
                self.mats.append(other)
            elif self.mats[-1] == "Zn" and other == "cloth":
                self.mats.append(other)
        else:
            if self.mats[-2] == "Cu" and self.mats[-1] == "cloth" and\
                    other == "Zn":
                self.mats.append(other)
            elif self.mats[-2] == "cloth" and self.mats[-1] == "Zn" and\
                    other == "cloth":
                self.mats.append(other)
            elif self.mats[-2] == "Zn" and self.mats[-1] == "cloth" and\
                    other == "Cu":
                self.mats.append(other)
            elif self.mats[-2] == "cloth" and self.mats[-1] == "Cu" and\
                    other == "cloth":
                self.mats.append(other)

    def __str__(self):
        tmp = ''.join(self.mats)
        count = min(tmp.count("Cu"), tmp.count("Zn"))
        return f"{count * 1.1} V"
