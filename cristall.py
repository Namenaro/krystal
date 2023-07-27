import statistics


class Cristall:
    def __init__(self, indexes, vals, wins):
        self.indexes = indexes
        self.vals = vals
        self.wins = wins

        self.prediction = statistics.mean(vals)

    def get_b1(self):
        return self.indexes[0]

    def get_b2(self):
        return self.indexes[-1]

    def get_err_in_point(self, point):
        return abs(self.vals[point] - self.prediction)

    def get_points(self):
        return self.indexes

    def get_vals(self):
        return self.vals