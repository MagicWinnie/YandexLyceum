class Cucumber:
    def crunch(self):
        return "crunch"

    def refresh(self):
        return "Cucumber refresh."


class Tomato:
    def melt(self):
        return "crunch"
    
    def refresh(self):
        return "Tomato refresh."


class Salad(Tomato):
    pass


class Smoothie(Cucumber):
    pass
