class EpicHero:
    def __init__(self, name, num, weapon):
        self.name = name
        self.num = num
        self.weapon = weapon.copy()

    def __str__(self):
        return f"Epic Hero {self.name}, {self.num}"

    def __repr__(self):
        return f"EpicHero('{self.name}', {self.num}, {sorted(self.weapon)})"

    def add_win(self):
        self.num += 1

    def add_weapon(self, item):
        self.weapon.append(item)

    def del_weapon(self, item):
        if item not in self.weapon:
            return
        ind = self.weapon.index(item)
        del self.weapon[ind]

    def __lt__(self, other):
        return (self.num, len(self.weapon), -len(self.name), self.name) <\
            (other.num, len(other.weapon), -len(other.name), other.name)

    def __gt__(self, other):
        return (self.num, len(self.weapon), -len(self.name), self.name) >\
            (other.num, len(other.weapon), -len(other.name), other.name)

    def __le__(self, other):
        return (self.num, len(self.weapon), -len(self.name), self.name) <=\
            (other.num, len(other.weapon), -len(other.name), other.name)

    def __ge__(self, other):
        return (self.num, len(self.weapon), -len(self.name), self.name) >=\
            (other.num, len(other.weapon), -len(other.name), other.name)

    def __eq__(self, other):
        return (self.num, len(self.weapon), -len(self.name), self.name) ==\
            (other.num, len(other.weapon), -len(other.name), other.name)

    def __ne__(self, other):
        return (self.num, len(self.weapon), -len(self.name), self.name) !=\
            (other.num, len(other.weapon), -len(other.name), other.name)
