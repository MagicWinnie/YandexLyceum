VOWELS = "aoeiuy"


class Knight:
    def __init__(self, name, *args):
        self.name = name
        self.weapons = list(args)

    def fight(self, weapon):
        if weapon not in self.weapons:
            return None
        string = ""
        for w in weapon:
            if w not in VOWELS:
                string += w.upper()
        return string

    def info(self):
        return "Knight(" + self.name + ")"

    def announce(self, lady):
        return f"Long live the noblest {lady}!"


class Squire:
    def __init__(self, name, knight_name, *args):
        self.name = name
        self.knight_name = knight_name
        self.weapons = list(args)

    def fight(self, weapon):
        if weapon not in self.weapons:
            return None
        string = ""
        for w in weapon:
            if w not in VOWELS:
                string += w.lower()
        return string

    def info(self):
        return "Squire(" + self.name + ")"

    def praise(self):
        return f"Glory to {self.knight_name}!"
