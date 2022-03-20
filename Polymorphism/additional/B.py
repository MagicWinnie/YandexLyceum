class TwoHandedSawUp:
    def __init__(self, lst):
        self.lst = lst.copy()

    def sawing(self):
        self.lst.sort()
        new_lst = []
        size = len(self.lst) // 2
        size_tmp = size + 1 if len(self.lst) % 2 != 0 else size
        for i in range(size):
            new_lst.append(self.lst[i])
            new_lst.append(self.lst[size_tmp + i])
        if len(self.lst) % 2 != 0:
            new_lst.append(size_tmp)
        self.lst = new_lst

    def get_list(self):
        return self.lst


class TwoHandedSawDown:
    def __init__(self, lst):
        self.lst = lst.copy()

    def get_list(self):
        return self.lst

    def sawing(self):
        self.lst.sort(reverse=True)
        new_lst = []
        size = len(self.lst) // 2
        size_tmp = size + 1 if len(self.lst) % 2 != 0 else size
        for i in range(size):
            new_lst.append(self.lst[i])
            new_lst.append(self.lst[size_tmp + i])
        if len(self.lst) % 2 != 0:
            new_lst.append(size_tmp)
        self.lst = new_lst


def print_hist(array):
    for el in array:
        print("*" * el)
