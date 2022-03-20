class Student:
    def __init__(self, name, university):
        self.name = name
        self.university = university
        self.course = 1

    def get_name(self):
        return self.name

    def get_university(self):
        return self.university

    def get_year(self):
        return self.course

    def study(self):
        self.course = min(self.course + 1, 6)


class Employee:
    positions = ["junior", "middle", "senior", "lead"]

    def __init__(self, name, company):
        self.name = name
        self.company = company
        self.pos = 0

    def get_name(self):
        return self.name

    def get_company(self):
        return self.company

    def work(self):
        self.pos = min(self.pos + 1, 3)

    def get_position(self):
        return self.positions[self.pos]


class Human:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name
