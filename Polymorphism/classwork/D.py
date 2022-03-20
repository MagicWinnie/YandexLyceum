class ShoppingList:
    def __init__(self, *args):
        self.llist = list(map(list, args))

    def values(self):
        return tuple(map(tuple, self.llist))

    def append(self, value):
        self.llist.append([value, False])

    def check(self, value):
        for i in range(len(self.llist)):
            if self.llist[i][0] == value:
                self.llist[i][1] = True
                break

    def checked_values(self):
        checked = []
        for i in range(len(self.llist)):
            if self.llist[i][1]:
                checked.append(self.llist[i])
        return tuple(map(tuple, checked))

    def rest_values(self):
        not_checked = []
        for i in range(len(self.llist)):
            if not self.llist[i][1]:
                not_checked.append(self.llist[i])
        return tuple(map(tuple, not_checked))


class TODOList:
    def __init__(self, *args):
        self.llist = list(map(list, args))
        self.llist = sorted(self.llist, key=lambda x: x[1], reverse=True)

    def values(self):
        return tuple(map(tuple, self.llist))

    def append(self, value, sr):
        self.llist.append([value, sr, False])
        self.llist = sorted(self.llist, key=lambda x: x[1], reverse=True)

    def check(self, value):
        for i in range(len(self.llist)):
            if self.llist[i][0] == value:
                self.llist[i][2] = True
                break

    def checked_values(self):
        checked = []
        for i in range(len(self.llist)):
            if self.llist[i][2]:
                checked.append(self.llist[i])
        return tuple(map(tuple, checked))

    def rest_values(self):
        not_checked = []
        for i in range(len(self.llist)):
            if not self.llist[i][2]:
                not_checked.append(self.llist[i])
        return tuple(map(tuple, not_checked))


class Route:
    def __init__(self, *args):
        self.llist = list(map(list, args))

    def values(self):
        return tuple(map(tuple, self.llist))

    def append(self, value, t):
        if len(self.llist) == 0:
            self.llist.append([value, t, False])
            return
        old_time = self.llist[-1][1]
        if int(t[:2]) > int(old_time[:2]) or (
            int(t[:2]) == int(old_time[:2]) and int(t[3:]) > int(old_time[3:])
        ):
            self.llist.append([value, t, False])

    def check(self, value):
        for i in range(len(self.llist)):
            if self.llist[i][0] == value:
                self.llist[i][2] = True
                break

    def checked_values(self):
        checked = []
        for i in range(len(self.llist)):
            if self.llist[i][2]:
                checked.append(self.llist[i])
        return tuple(map(tuple, checked))

    def rest_values(self):
        not_checked = []
        for i in range(len(self.llist)):
            if not self.llist[i][2]:
                not_checked.append(self.llist[i])
        return tuple(map(tuple, not_checked))
