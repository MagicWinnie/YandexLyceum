class Talking:
    def __init__(self, name):
        self.name = name
        self.yes = 0
        self.no = 0

    def to_answer(self):
        if (self.yes + self.no) % 2 == 0:
            self.yes += 1
            return "moore-moore"
        else:
            self.no += 1
            return "meow-meow"

    def number_yes(self):
        return self.yes 
    
    def number_no(self):
        return self.no
