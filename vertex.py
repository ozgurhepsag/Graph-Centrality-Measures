class vertex:

    def __init__(self, key):
        self.key = key
        self.points_to = {}

    def get_key(self):
        return self.key

    def add_neighbour(self, dest, weight):
        self.points_to[dest] = weight

    def get_neighbours(self):
        return self.points_to

    def get_neighbours_counts(self):
        return self.points_to.keys().__len__()

    def does_it_point_to(self, dest):
        return dest in self.points_to
