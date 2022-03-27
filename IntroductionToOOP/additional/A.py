class Robot:
    def __init__(self, start):
        self.coord = list(start)
        self.p = [start]

    def move(self, s):
        self.p = []
        for i in s:
            self.p.append(tuple(self.coord))
            if i == "N":
                if self.coord[1] + 1 <= 100:
                    self.coord[1] += 1
            elif i == "S":
                if self.coord[1] - 1 >= 0:
                    self.coord[1] -= 1
            elif i == "E":
                if self.coord[0] + 1 <= 100:
                    self.coord[0] += 1
            else:
                if self.coord[0] - 1 >= 0:
                    self.coord[0] -= 1
        
        self.p.append(tuple(self.coord))

        return tuple(self.coord)

    def path(self):
        return self.p
