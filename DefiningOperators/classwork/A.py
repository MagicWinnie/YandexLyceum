class ModifiedString:
    def __init__(self, string):
        self.string = string

    def __str__(self):
        return self.string

    def __add__(self, new_str):
        return ModifiedString(self.string + new_str)

    def __radd__(self, other):
        return ModifiedString(other + self.string)

    def __sub__(self, new_str):
        new_str = new_str.lower()
        out_str = ""
        for ch in self.string:
            if ch.lower() not in new_str:
                out_str += ch
        return ModifiedString(out_str)

    def __rsub__(self, other):
        new_str = self.string.lower()
        out_str = ""
        for ch in other:
            if ch.lower() not in new_str:
                out_str += ch
        return ModifiedString(out_str)
