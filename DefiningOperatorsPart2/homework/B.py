class Wagon:
    def __init__(self, num):
        self.num = num

    def get_number(self):
        return self.num

    def __str__(self):
        return f"№{self.num}"


class Train:
    def __init__(self, num, wagons=[]):
        self.num = num
        self.wagons = wagons.copy()

    def get_number(self):
        return self.num

    def get_wagons(self):
        return self.wagons[:]

    def append(self, item):
        self.wagons.append(item)

    def __len__(self):
        return len(self.wagons)

    def __str__(self):
        return f"Train {self.num} has {len(self.wagons)} wagons"

    def __getitem__(self, key):
        return self.wagons[key]

    def __setitem__(self, key, value):
        self.wagons[key] = value

    def __delitem__(self, key):
        if key == len(self.wagons) - 1:
            del self.wagons[-1]

    def __iter__(self):
        return iter(self.wagons)
