class Darkness:
    def __init__(self, *args, name="Marley"):
        self.things = list(args)
        self.name = name

    def change_name(self, new_name):
        self.name = new_name

    def add_event(self, new_arg):
        self.things.append(new_arg)

    def ordinary(self):
        res = []
        for el in self.things:
            count = 0
            for ch in set(el.lower()):
                if ch in self.name.lower():
                    count += 1
            if count < 2:
                res.append(el)
        return res

    def suspicious(self):
        res = []
        for el in self.things:
            count = 0
            for ch in set(el.lower()):
                if ch in self.name.lower():
                    count += 1
            if count >= 2:
                res.append(el)
        return res
