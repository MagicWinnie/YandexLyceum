class ChemicalPowerSource:
    def __init__(self, metal_1, elektrolyte, metal_2):
        self.metal_1 = metal_1
        self.metal_2 = metal_2
        self.elektrolyte = elektrolyte

    def get_content(self):
        return [self.metal_1, self.elektrolyte, self.metal_2]

    def change_content(self, metal_1, elektrolyte, metal_2):
        self.metal_1 = metal_1
        self.metal_2 = metal_2
        self.elektrolyte = elektrolyte

    def voltage(self):
        return (len(self.metal_1) + len(self.metal_2) + len(self.elektrolyte)) / 10


class BotanicPowerSource:
    def __init__(self, plant, metal_1, metal_2):
        self.plant = plant
        self.metal_1 = metal_1
        self.metal_2 = metal_2

    def get_content(self):
        return [self.plant, self.metal_1, self.metal_2]

    def change_content(self, plant, metal_1, metal_2):
        self.plant = plant
        self.metal_1 = metal_1
        self.metal_2 = metal_2

    def voltage(self):
        return (len(self.plant) + len(self.metal_1) + len(self.metal_2)) / 10


class MechanicalPowerSource:
    def __init__(self, d_1, d_2):
        self.d_1 = d_1
        self.d_2 = d_2

    def get_content(self):
        return [self.d_1, self.d_2]

    def change_content(self, d_1, d_2):
        self.d_1 = d_1
        self.d_2 = d_2

    def voltage(self):
        return (self.d_1 + self.d_2) / 10
