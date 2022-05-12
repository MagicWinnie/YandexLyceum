class Sound:
    def __init__(self, sound="zing"):
        self.sound = sound

    def __repr__(self):
        return f"Sound('{self.sound}')"


class ChainRattle(Sound):
    def __init__(self, n, *args):
        self.n = n
        self.sounds = list(args) if args else ["zing" for _ in range(n)]

    def __getitem__(self, key):
        return self.sounds[key]

    def __setitem__(self, key, value):
        self.sounds[key] = value

    def __delitem__(self, key):
        del self.sounds[key]

    def append(self, value):
        self.sounds.append(value)

    def __repr__(self):
        s = ""
        for el in self.sounds:
            s += "'" + el + "', "
        return f"ChainRattle({self.n}, {s[:-2]})"

    def __iter__(self):
        return iter(self.sounds)
