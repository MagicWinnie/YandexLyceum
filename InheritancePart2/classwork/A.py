class Seat:
    def __init__(self, *args):
        self.args = args

    def __str__(self):
        return (
            self.__class__.__name__ + "(" + ", ".join(list(map(str, self.args))) + ")"
        )


class Chair(Seat):
    def __init__(self, *args):
        super().__init__(*args)


class ArmChair(Seat):
    def __init__(self, *args):
        super().__init__(*args)


class Stool(Seat):
    def __init__(self, *args):
        super().__init__(*args)


class BagChair(Seat):
    def __init__(self, *args):
        super().__init__(*args)
