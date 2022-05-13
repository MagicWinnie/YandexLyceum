class Ghost:
    def __init__(self, name="Ghost"):
        self.name = name

    def __repr__(self):
        return f"Ghost('{self.name}')"


class CantervilleGhost(Ghost):
    def __init__(self, **kwargs):
        self.args = kwargs
        if "name" in kwargs:
            super().__init__(kwargs["name"])
            self.pop("name")
        else:
            super().__init__()

    def __getitem__(self, key):
        return self.args[key]

    def __setitem__(self, key, value):
        self.args[key] = value

    def __iter__(self):
        return iter(self.args.keys())

    def pop(self, key):
        return self.args.pop(key)

    def items(self):
        return sorted(self.args.items())

    def __repr__(self):
        return f"CantervilleGhost(name='{self.name}')"
