class SnowFlakes:
    def __init__(self, a):
        self.a = a
        self.border = 0
        self.thickness = 1
        self.snowflake = [["-" for _ in range(self.a)] for _ in range(self.a)]
        self.thicken(0)
        self.thaw(self.border)

    def thaw(self, n):
        for i in range(n):
            for j in range(self.a):
                self.snowflake[i][j] = "-"
        for i in range(self.a - n, self.a):
            for j in range(self.a):
                self.snowflake[i][j] = "-"
        for i in range(self.a):
            for j in range(n):
                self.snowflake[i][j] = "-"
        for i in range(self.a):
            for j in range(self.a - n, self.a):
                self.snowflake[i][j] = "-"

    def thicken(self, thick=None):
        if thick is None:
            thick = self.thickness
        for i in range(-thick, thick + 1):
            self.snowflake[self.a // 2 + i] = ["*" for _ in range(self.a)]
        for i in range(-thick, thick + 1):
            for j in range(self.a):
                self.snowflake[j][self.a // 2 + i] = "*"
        for j in range(-thick, thick + 1):
            for i in range(self.a):
                self.snowflake[min(self.a - 1, max(0, i + j))][i] = "*"
                self.snowflake[i][max(0, min(self.a - 1, self.a - i - 1 + j))] = "*"
        if thick is None:
            self.thickness += 1

    def freeze(self, n):
        self.a += 2 * n
        self.snowflake = [["-" for _ in range(self.a)] for _ in range(self.a)]
        self.thicken(0)
        self.thaw(self.border)
        self.thicken(self.thickness - 1)

    def show(self):
        for i in range(self.a):
            print("".join(self.snowflake[i]))
