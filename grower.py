from bassin import Bassin
from cristall import Cristall

import statistics



class OneKristalGrower:
    def __init__(self, start_point, allowed_global_indexes, bassin):
        self.crystal_points = [start_point]

        self.allowed_indexes = allowed_global_indexes
        self.bassin = bassin

    def grow(self):
        while True:
            result = self.grow_step()
            if result is None:
                break

    def _get_left_allowed_index(self):
        left_index = self.crystal_points[-1]
        position_in_allowed = self.allowed_indexes.index(left_index)
        if position_in_allowed == len(self.allowed_indexes)-1:
            return None

        return self.allowed_indexes[position_in_allowed+1]


    def _get_right_allowed_index(self):
        left_index = self.crystal_points[0]
        position_in_allowed = self.allowed_indexes.index(left_index)
        if position_in_allowed == 0:
            return None

        return self.allowed_indexes[position_in_allowed - 1]

    def get_krystal_vals(self):
        vals = list([self.bassin.get_val(i) for i in self.crystal_points])
        return vals

    def get_cystal_points(self):
        return self.crystal_points

    def get_crystall_obj(self):
        indexes = self.crystal_points
        vals = self.get_krystal_vals()
        wins = self.get_wins()
        cristall = Cristall(indexes, vals, wins)
        return cristall

    def get_krystal_prediction(self):
        kristal_vals = self.get_krystal_vals()
        return statistics.mean(kristal_vals)

    def check_win_in_point(self, gloabal_index, old_prediction, new_prediction):
        if gloabal_index is None:
            return None
        real_val = self.bassin.get_val(gloabal_index)
        abs_err_old = abs(old_prediction - real_val)
        abs_err_new = abs(new_prediction - real_val)
        win = abs_err_old - abs_err_new
        return win

    def get_wins(self):
        auto_prediction = self.bassin.get_auto_prediction()
        krystal_prediction = self.get_krystal_prediction()
        wins = []
        for i in self.crystal_points:
            win = self.check_win_in_point(i, old_prediction=auto_prediction, new_prediction=krystal_prediction)
            wins.append(win)
        return wins



    def grow_step(self):
        left_candidate = self._get_left_allowed_index()
        right_candidate = self._get_right_allowed_index()

        auto_prediction = self.bassin.get_auto_prediction()
        krystal_prediction = self.get_krystal_prediction()

        physical_win_left = self.check_win_in_point(left_candidate, old_prediction=auto_prediction, new_prediction=krystal_prediction)
        physical_win_right = self.check_win_in_point(right_candidate, old_prediction=auto_prediction, new_prediction=krystal_prediction)

        if physical_win_right is None and physical_win_left is None:
            return None

        if physical_win_right is None:
            if physical_win_left < 0:
                return None

        if physical_win_left is None:
            if physical_win_right <0:
                return None

        if physical_win_right > physical_win_left:
            self.crystal_points.append(right_candidate)
            result = right_candidate
        else:
            self.crystal_points = [left_candidate] + self.crystal_points
            result = left_candidate

        return result
