class ConveySequence:
    def __init__(self, start=1):
        self.start = start
        self.lines = [self.start]

    def __str__(self):
        return f"Covey sequence (start={self.start})"

    def line(self, number_of_lines):
        if len(self.lines) >= number_of_lines:
            return self.lines[number_of_lines - 1]

        p = str(self.lines[-1])
        n = number_of_lines - len(self.lines) + 1
        while n > 1:
            q = ''
            idx = 0
            length = len(p)
            while idx < length:
                start = idx
                idx = idx + 1
                while idx < length and p[idx] == p[start]:
                    idx = idx + 1
                q = q + str(idx - start) + p[start]
            n -= 1
            p = q
            self.lines.append(int(p))
        return self.lines[-1]

    def line_dict(self, n):
        if len(self.lines) < n:
            self.line(n)
        s_l = str(self.lines[n - 1])
        numbers = set(s_l)
        d = {}
        for el in numbers:
            d[int(el)] = s_l.count(el)
        return d

    def number(self, n, m):
        if len(self.lines) < n:
            self.line(n)
        s_l = str(self.lines[n - 1])
        if m > len(s_l):
            return None
        return int(s_l[m - 1])
