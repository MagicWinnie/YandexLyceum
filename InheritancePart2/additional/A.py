class Cycling:
    def __init__(self, n) -> None:
        self.n = n
        self.mat = [[[0, False] for _ in range(n)] for _ in range(n)]
        c = 1
        for i in range(n):
            for j in range(n):
                self.mat[i][j][0] = c
                c += 1

    def __str__(self):
        s = ''
        for i in range(self.n):
            s += '\t'.join(list(map(lambda x: str(x[0]), self.mat[i]))) + '\n'
        return s[:-1]

    def get(self):
        c = 1
        for i in range(self.n // 2 + 1):
            for j in range(2 * i + 1):
                if self.mat[self.n // 2 - i][self.n // 2 - i + j][1]:
                    continue 
                self.mat[self.n // 2 - i][self.n // 2 - i + j][0] = c
                self.mat[self.n // 2 - i][self.n // 2 - i + j][1] = True
                c += 1
            for j in range(2 * i - 1):
                if self.mat[self.n // 2 - i + 1 + j][self.n // 2 + i][1]:
                    continue
                self.mat[self.n // 2 - i + 1 + j][self.n // 2 + i][0] = c
                self.mat[self.n // 2 - i + 1 + j][self.n // 2 + i][1] = True
                c += 1
            for j in range(2 * i + 1):
                if self.mat[self.n // 2 + i][self.n // 2 + i - j][1]:
                    continue 
                self.mat[self.n // 2 + i][self.n // 2 + i - j][0] = c
                self.mat[self.n // 2 + i][self.n // 2 + i - j][1] = True
                c += 1
            for j in range(2 * i - 1):
                if self.mat[self.n // 2 + i - j - 1][self.n // 2 - i][1]:
                    continue
                self.mat[self.n // 2 + i - j - 1][self.n // 2 - i][0] = c
                self.mat[self.n // 2 + i - j - 1][self.n // 2 - i][1] = True
                c += 1
        for i in range(self.n):
            for j in range(self.n):
                self.mat[i][j][1] = False


class SouthernTornado(Cycling):
    def __init__(self, n):
        super().__init__(n)
    
    def get(self):
        c = 1
        for i in range(self.n // 2 + 1):
            for j in range(1, 2 * i + 1):
                if self.mat[self.n // 2 - i][self.n // 2 - i + j][1]:
                    continue 
                self.mat[self.n // 2 - i][self.n // 2 - i + j][0] = c
                self.mat[self.n // 2 - i][self.n // 2 - i + j][1] = True
                c += 1
            for j in range(2 * i - 1):
                if self.mat[self.n // 2 - i + 1 + j][self.n // 2 + i][1]:
                    continue
                self.mat[self.n // 2 - i + 1 + j][self.n // 2 + i][0] = c
                self.mat[self.n // 2 - i + 1 + j][self.n // 2 + i][1] = True
                c += 1
            for j in range(2 * i + 1):
                if self.mat[self.n // 2 + i][self.n // 2 + i - j][1]:
                    continue 
                self.mat[self.n // 2 + i][self.n // 2 + i - j][0] = c
                self.mat[self.n // 2 + i][self.n // 2 + i - j][1] = True
                c += 1
            for j in range(2 * i):
                if self.mat[self.n // 2 + i - j - 1][self.n // 2 - i][1]:
                    continue
                self.mat[self.n // 2 + i - j - 1][self.n // 2 - i][0] = c
                self.mat[self.n // 2 + i - j - 1][self.n // 2 - i][1] = True
                c += 1
        for i in range(self.n):
            for j in range(self.n):
                self.mat[i][j][1] = False


class NorthernTornado(Cycling):
    def __init__(self, n):
        super().__init__(n)
    
    def get(self):
        c = 1
        for i in range(self.n // 2 + 1):
            for j in range(1, 2 * i + 1):
                if self.mat[self.n // 2 - i][self.n // 2 - i + j][1]:
                    continue 
                self.mat[self.n // 2 - i][self.n // 2 - i + j][0] = c
                self.mat[self.n // 2 - i][self.n // 2 - i + j][1] = True
                c += 1
            for j in range(2 * i - 1):
                if self.mat[self.n // 2 - i + 1 + j][self.n // 2 + i][1]:
                    continue
                self.mat[self.n // 2 - i + 1 + j][self.n // 2 + i][0] = c
                self.mat[self.n // 2 - i + 1 + j][self.n // 2 + i][1] = True
                c += 1
            for j in range(2 * i + 1):
                if self.mat[self.n // 2 + i][self.n // 2 + i - j][1]:
                    continue 
                self.mat[self.n // 2 + i][self.n // 2 + i - j][0] = c
                self.mat[self.n // 2 + i][self.n // 2 + i - j][1] = True
                c += 1
            for j in range(2 * i):
                if self.mat[self.n // 2 + i - j - 1][self.n // 2 - i][1]:
                    continue
                self.mat[self.n // 2 + i - j - 1][self.n // 2 - i][0] = c
                self.mat[self.n // 2 + i - j - 1][self.n // 2 - i][1] = True
                c += 1
        for i in range(self.n):
            self.mat[i] = self.mat[i][::-1]
            for j in range(self.n):
                self.mat[i][j][1] = False
