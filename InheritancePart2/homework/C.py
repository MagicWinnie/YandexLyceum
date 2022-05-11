class Board:
    def __init__(self, row, col, fill='0'):
        self.row = row
        self.col = col
        self.fill = fill

        self.mat = [[self.fill for _ in range(self.col)] for _ in range(self.row)]

    def __str__(self):
        s = ''
        for el in self.mat:
            s += ''.join(el) + '\n'
        return s[:-1]


class Checker(Board):
    def __init__(self, side, white, black='0'):
        self.side = side
        super().__init__(side, side, black)
        for i in range(side):
            for j in range(1 if i % 2 == 0 else 0, side, 2):
                self.mat[side - i - 1][j] = white

    def put_on(self, black, white):
        for i in range(3):
            for j in range(0 if i % 2 == 0 else 1, self.side, 2):
                self.mat[self.side - i - 1][j] = white
            for j in range(1 if i % 2 == 0 else 0, self.side, 2):
                self.mat[i][j] = black


class Chess(Checker):
    def __init__(self):
        super().__init__(8, '1')

    def put_on(self, one=str.lower, two=str.upper):
        pole = ['RNBKQBNR', 'PPPPPPPP']
        for i in range(2):
            for j in range(8):
                self.mat[i][j] = one(pole[i][j])
                self.mat[8 - i - 1][j] = two(pole[i][j])
