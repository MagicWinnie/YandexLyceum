from itertools import combinations


class Device:
    def __init__(self, n):
        self.n = n
        self.sensors = ["O"] * n

    def append(self, value):
        self.sensors.append(value)
        self.n += 1

    def remove(self, key):
        if key >= len(self.sensors):
            return
        del self.sensors[key]

    def change(self, key):
        if key >= len(self.sensors):
            return
        if self.sensors[key] == "O":
            self.sensors[key] = "X"
        elif self.sensors[key] == "X":
            self.sensors[key] = "O"

    def __call__(self, num, mode=1):
        inds = []
        nonworking = 0
        for i in range(len(self.sensors)):
            if self.sensors[i] == "O":
                inds.append(i)
            else:
                nonworking += 1
        if nonworking >= num:
            if mode == 1:
                return (1,)
            return ["".join(self.sensors)]
        lst = list(combinations(inds, num - nonworking))
        if mode == 1:
            return (len(lst),)
        out = []
        for el in lst:
            tmp = self.sensors.copy()
            for ind in el:
                tmp[ind] = "X"
            out.append("".join(tmp))
        return out

    def __str__(self):
        return "".join(self.sensors)
