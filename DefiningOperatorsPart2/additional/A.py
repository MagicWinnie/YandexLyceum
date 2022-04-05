class Thought:
    def __init__(self, name, weight, theme=[]):
        self.name = name
        self.weight = weight
        self.theme = theme[:]
        self.flag = True

    def overturn(self, value):
        if self.flag:
            self.weight *= value
        else:
            self.weight //= value
        self.flag = not self.flag
        if self.theme:
            self.theme = self.theme[1:] + [self.theme[0]]

    def add_topic(self, value):
        self.theme.append(value)

    def __eq__(self, other):
        return (self.weight, len(self.theme), self.name) ==\
            (other.weight, len(other.theme), other.name)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        return (self.weight, len(self.theme), self.name) <\
            (other.weight, len(other.theme), other.name)

    def __gt__(self, other):
        return not self.__lt__(other)

    def __le__(self, other):
        return (self.weight, len(self.theme), self.name) <=\
            (other.weight, len(other.theme), other.name)

    def __ge__(self, other):
        return not self.__le__(other)

    def __str__(self):
        topic = ""
        if self.theme:
            topic = self.theme[0]
        return f"Thought of {self.name}, weight of {self.weight}, topic {topic}"
