class Controller:
    def __init__(self):
        self.channel = 1

    def click(self):
        self.channel += 1
        if self.channel > 5:
            self.channel = 1
