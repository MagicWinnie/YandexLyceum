class AbstractCat:
    weight = 0
    food = 0

    def eat(self, food):
        self.food += food
        self.weight += self.food // 10
        self.food %= 10
        self.weight = min(self.weight, 100)
    
    def __repr__(self):
        return f"{self.__class__.__name__} ({self.weight})"


class Kitten(AbstractCat):
    def __init__(self, weight):
        self.weight = weight

    def meow(self):
        return "meow..."
    
    def sleep(self):
        return "Snore" * (self.weight // 5)


class Cat(Kitten):
    def __init__(self, weight, name):
        self.weight = weight
        self.name = name

    def meow(self):
        return "MEOW..."
    
    def get_name(self):
        return self.name

    def catch_mice(self):
        return "Got it!"
