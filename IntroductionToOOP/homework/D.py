class QuickFactorial:
    def __init__(self):
        self.d = {0: 1, 1: 1}

    def result(self, n):
        if n in self.d:
            return self.d[n]

        for i in range(max(self.d) + 1, n + 1):
            self.d[i] = self.d[i - 1] * i

        return self.d[n]
