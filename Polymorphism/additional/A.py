class LettersRhombus:
    def __init__(self, fore, back=" "):
        self.fore = fore
        self.back = back
        self.size = (ord(fore) - ord("A")) * 2 + 1
        self.matrix = [
            [back for _ in range(self.size)] for _ in range(self.size)
        ]
        for i in range(self.size // 2 + 1):
            self.matrix[i][self.size // 2 - i] = chr(ord("A") + i)
            self.matrix[i][self.size // 2 + i] = chr(ord("A") + i)
            self.matrix[self.size - i - 1][self.size // 2 - i] = chr(
                ord("A") + i
            )
            self.matrix[self.size - i - 1][self.size // 2 + i] = chr(
                ord("A") + i
            )

    def rows(self):
        return ["".join(x) for x in self.matrix]

    def cols(self):
        new_mat = []
        for j in range(len(self.matrix[0])):
            tmp = []
            for i in range(len(self.matrix)):
                tmp.append(self.matrix[i][j])
            new_mat.append("".join(tmp))
        return new_mat
