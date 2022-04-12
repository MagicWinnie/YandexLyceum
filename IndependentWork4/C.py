class LifeGivingFire:
    def __init__(self, color, kolvo, length):
        self.color = color
        self.kolvo = kolvo
        self.length = length

    def __eq__(self, other):
        return (self.length, self.kolvo, self.color) ==\
            (other.length, other.kolvo, other.color)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        return (self.length, self.kolvo, self.color) <\
            (other.length, other.kolvo, other.color)

    def __gt__(self, other):
        return not self.__le__(other)

    def __le__(self, other):
        return (self.length, self.kolvo, self.color) <=\
            (other.length, other.kolvo, other.color)

    def __ge__(self, other):
        return not self.__lt__(other)

    def __call__(self, arg):
        return self.kolvo * self.length * len(self.color) // arg

    def throw_wood(self, arg):
        self.kolvo += arg
        self.length += arg // 10

    def change_color(self, arg):
        if len(arg) >= len(self.color):
            self.color = arg

    def __str__(self):
        return f"Life-Giving Fire with color of {self.color} by {self.kolvo} of wood, burning for {self.length}."
