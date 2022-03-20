class BlackCat:
    def __init__(self, name):
        self.name = name
        self.wool = 0
        self.tail = 0

    def play(self, kind, n):
        if kind == 'wool':
            self.wool += n 
        elif kind == 'tail':
            self.tail += n 
        else:
            self.wool = 0
            self.tail = 0
    
    def get_play(self):
        return (self.wool, self.tail)
