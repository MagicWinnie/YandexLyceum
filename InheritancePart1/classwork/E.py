class Storm:
    def __init__(self, tal):
        self.tal = tal

    def __repr__(self):
        return f"Storm('{self.tal}')"


class ThunderAndLightning(Storm):
    def __init__(self, dic, tal="Irma"):
        self.dic = dic
        self.tal = tal

    def __getitem__(self, key):
        return self.dic[key]

    def __setitem__(self, key, val):
        self.dic[key] = val

    def __repr__(self):
        return f"ThunderAndLightning({self.dic})"

    def items(self):
        return self.dic.items()

    def __iter__(self):
        return iter(self.dic)
