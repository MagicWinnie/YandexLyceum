class FastFibonacci:
    fibs = {
        1: 1,
        2: 1
    }

    def __call__(self, number):
        if number in self.fibs:
            return self.fibs[number]
        for i in range(max(self.fibs.keys()) + 1, number + 1):
            self.fibs[i] = self.fibs[i - 1] + self.fibs[i - 2]
        return self.fibs[number]
