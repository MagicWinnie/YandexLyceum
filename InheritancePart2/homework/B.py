class Mosquito:
    def __init__(self, age):
        self.age = age

    def __str__(self):
        return f"{self.__class__.__name__}, {self.age} days"

    def hearing(self):
        return "I hear and see everything " + self.lives

    def squeak(self):
        return "The thin squeak of a mosquito after eating " + self.feed


class MaleMosquito(Mosquito):
    feed = "nectar"
    lives = "on land"

    def __init__(self, age):
        self.age = age


class FemaleMosquito(Mosquito):
    feed = "blood"
    lives = "on land"

    def __init__(self, age):
        self.age = age

    
class MosquitoLarva(FemaleMosquito, MaleMosquito):
    feed = "algae"
    lives = "in water"

    def __init__(self, age):
        self.age = age
