import statistics


class Cristall:
    def __init__(self, indexes, vals):
        self.indexes = indexes
        self.vals = vals
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


def init_cristall_from_points(full_signal, points):
    vals = list([full_signal[point] for point in points])
    cristall = Cristall(indexes=points, vals=vals)
    return cristall



