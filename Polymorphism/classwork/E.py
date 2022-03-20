class LineToTable:
    def __init__(self, llist, height, width):
        self.llist = llist
        self.height = height
        self.width = width

    def resize(self):
        return (
            [
                self.llist[i: i + self.width]
                for i in range(0, len(self.llist), self.width)
            ],
            self.height,
            self.width,
        )


class TableToLine:
    def __init__(self, llist):
        self.llist = llist
        self.height = len(self.llist)
        self.width = len(self.llist[0])

    def resize(self):
        new_list = []
        for i in self.llist:
            for j in i:
                new_list.append(j)
        return new_list, self.height, self.width
