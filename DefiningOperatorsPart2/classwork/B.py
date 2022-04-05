class Knight:
    def __init__(self, name, weight, weapon=[]):
        self.name = name
        self.weight = weight
        self.weapon = weapon

    def overturn(self):
        self.name = self.name[::-1].capitalize()
        if len(self.weapon) > 0:
            first = self.weapon[0]
            self.weapon = self.weapon[1:] + [first]

    def add_weapon(self, unit):
        self.weapon.append(unit)

    def add_weight(self, value):
        self.weight += value
        self.weight = max(0, self.weight)

    def __eq__(self, other):
        return (self.weight, len(self.weapon), self.name) ==\
            (other.weight, len(other.weapon), other.name)

    def __ne__(self, other):
        return (self.weight, len(self.weapon), self.name) !=\
            (other.weight, len(other.weapon), other.name)

    def __lt__(self, other):
        return (self.weight, len(self.weapon), self.name) <\
            (other.weight, len(other.weapon), other.name)

    def __gt__(self, other):
        return (self.weight, len(self.weapon), self.name) >\
            (other.weight, len(other.weapon), other.name)

    def __le__(self, other):
        return (self.weight, len(self.weapon), self.name) <=\
            (other.weight, len(other.weapon), other.name)

    def __ge__(self, other):
        return (self.weight, len(self.weapon), self.name) >=\
            (other.weight, len(other.weapon), other.name)

    def __str__(self):
        weapon = ''
        if len(self.weapon) > 0:
            weapon = self.weapon[0]
        return f"Knight {self.name}, weapon {weapon}, {self.weight}"
