class Rewrite:
    def __init__(self, in_name, out_name):
        self.in_name = in_name
        self.out_name = out_name
    
    def done(self):
        with open(self.in_name) as in_file, open(self.out_name, 'w') as out_file:
            out_file.writelines(in_file.readlines())


class Calculus(Rewrite):
    def five_per_line(self):
        with open(self.in_name) as in_file, open(self.out_name, 'w') as out_file:
            lst = []
            for line in in_file:
                nums = list(map(int, line.split()))
                lst += nums
            lst.sort()
            for i in range(0, len(lst), 5):
                out_file.write(' '.join(list(map(str, lst[i: i + 5]))) + '\n')


class Align(Rewrite):
    def to_right(self):
        with open(self.in_name) as in_file, open(self.out_name, 'w') as out_file:
            lst = []
            for line in in_file:
                nums = line.split()
                lst += nums
            max_len = len(max(lst, key=lambda x: len(x)))
            for el in lst:
                out_file.write(' ' * (max_len - len(el)) + el + '\n')
