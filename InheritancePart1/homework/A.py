class Wardrobe:
    def __init__(self, *args):
        self.args = list(args)
    
    def __str__(self):
        return ' '.join(self.args)

    def __eq__(self, b):
        return type(self) == type(b) and len(self.args) == len(b.args)

    def __ne__(self, b):
        return not self.__eq__(b)

    def __lt__(self, b):
        return isinstance(b, MagicWardrobe) and isinstance(self, JustWardrobe) or\
            type(self) == type(b) and len(self.args) < len(b.args)

    def __le__(self, b):
        return isinstance(b, MagicWardrobe) and isinstance(self, JustWardrobe) or\
            type(self) == type(b) and len(self.args) <= len(b.args)

    def __gt__(self, b):
        return not self.__le__(b)

    def __ge__(self, b):
        return not self.__lt__(b)


class JustWardrobe(Wardrobe):
    def __str__(self):
        self.args[0] = self.args[0][0].upper() + self.args[0][1:].lower()
        return ', '.join(self.args) + '.'


class MagicWardrobe(Wardrobe):
    def __str__(self):
        self.args = list(map(lambda x: x[0].upper() + x[1:].lower(), self.args))
        self.args.sort()
        return ', '.join(self.args) + '.'
