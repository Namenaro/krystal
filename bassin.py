import statistics

class Bassin:
    def __init__(self, vals, global_indexes):
        self.indexes_to_vals = {}
        for i in range(len(vals)):
            val = vals[i]
            global_index = global_indexes[i]
            self.indexes_to_vals[global_index] = val

    def remove_element(self, global_index):
        del self.indexes_to_vals[global_index]

    def get_auto_prediction(self):
        return statistics.mean(self.indexes_to_vals.values())
        