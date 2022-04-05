class Talking:
    def __init__(self, name, time, theme=[]):
        self.name = name
        self.time = time
        self.theme = theme

    def add_theme(self, value):
        self.theme.append(value)

    def change_theme(self):
        if self.theme:
            self.theme = self.theme[1:] + [self.theme[0]]

    def change_time(self, number):
        self.time += number

    def __eq__(self, other):
        return (self.time, len(self.theme), self.name) ==\
            (other.time, len(other.theme), other.name)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        return (self.time, len(self.theme), self.name) <\
            (other.time, len(other.theme), other.name)

    def __gt__(self, other):
        return not self.__lt__(other)

    def __le__(self, other):
        return (self.time, len(self.theme), self.name) <=\
            (other.time, len(other.theme), other.name)

    def __ge__(self, other):
        return not self.__le__(other)

    def __str__(self):
        first = ''
        if self.theme:
            first = self.theme[0]
        return f"{self.name}'s Conversation, main theme is {first} for {self.time} minutes"
