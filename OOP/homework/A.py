class Avalanche:
    def __init__(self):
        self.first = True
        self.str = "O"

    def go(self):
        if self.first:
            print(self.str)
            self.first = False
            return
        out = ''
        for i in range(len(self.str)):
            if self.str[i] == 'O':
                out += "ooOoo"
            else:
                out += "oOo"
        self.str = out
        print(self.str)
