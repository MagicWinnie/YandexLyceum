class BeeElephant:
    def __init__(self, bee, eleph):
        self.bee = bee
        self.eleph = eleph

    def fly(self):
        return self.bee >= self.eleph

    def trumpet(self):
        if self.eleph >= self.bee:
            return "tu-tu-doo-doo!"
        return "wzzzzz"

    def eat(self, meal, eat):
        if meal == "nectar":
            self.bee = min(100, max(self.bee + eat, 0))
            self.eleph = min(100, max(self.eleph - eat, 0))
        else:
            self.bee = min(100, max(self.bee - eat, 0))
            self.eleph = min(100, max(self.eleph + eat, 0))

    def get_parts(self):
        return (self.bee, self.eleph)
