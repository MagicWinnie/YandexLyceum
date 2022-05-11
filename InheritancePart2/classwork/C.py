class Fish:
    def swim(self):
        return "swim"

    def dive(self):
        return "dive"

    def breathe_with_gills(self):
        return "breathe_with_gills"


class LandAnimal:
    def walk_on_land(self):
        return "walk_on_land"

    def breathe_air(self):
        return "breathe_air"

    def feed_cubs(self):
        return "feed_cubs"


class Whale(Fish, LandAnimal):
    def filter_food(self, lst, size):
        return list(filter(lambda x: x <= size, lst))

    def breathe_with_gills(self):
        return None

    def walk_on_land(self):
        return None

    def feed_cubs(self):
        return None
