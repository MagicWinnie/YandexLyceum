emojis = [':)', ';)', ':(', ';(', ')', '(']


class Liked:
    def __init__(self, *args):
        self.s = ' '.join(args)

    def likes(self):
        d = {}
        s = self.s
        for emoji in emojis:
            if emoji not in s:
                continue
            d[emoji] = s.count(emoji)
            s = s.replace(emoji, '')
        return d


class MiMiMi(Liked):
    def __init__(self, *args):
        self.s = ' '.join(list(filter(lambda x: 'cat' in x or 'kitten' in x, args)))
