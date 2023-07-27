from grower import OneKristalGrower
from bassin import Bassin
from utils import IdsGen
from cristall import Cristall




class Situation:
    def __init__(self, full_signal):
        self.full_signal = full_signal

        self.names_to_crystalls = {} # int :cristall

        self.points_to_cristalls_names = {} # point : [name1, name2,...] последний самый "молодой"
        for i in range(len(full_signal)):
            self.points_to_cristalls_names[i] = []

        self.names_gen = IdsGen()

    def init_grower_from_point(self, point):
        return parent_name, grower

    def add_crystall(self, parent_name, crystall):
        pass

    def init_grower_from_val_and_point(self, point, val):
        return parent_name, grower

    def get_worst_point(self):
        point_err_worst = None
        point_index_worst = None
        for point in range(len(self.full_signal)):
            latest_cristall = self.get_best_cristall_for_point(point)
            err_in_point = latest_cristall.get_err_in_point(point)

            if point_err_worst is None:
                point_err_worst = err_in_point
                point_index_worst = point
            else:
                if point_err_worst< err_in_point:
                    point_err_worst = err_in_point
                    point_index_worst = point

        return point_index_worst

    #-----------------------------------------------------------
    #----------------------------------------------------------
    def get_best_cristall_for_point(self, point):
        names = self.points_to_cristalls_names[point]
        if len(names) == 0:
            return None
        best_cristall_name = names[-1]
        return self.names_to_crystalls[best_cristall_name]

    def register_crystall_no_modification(self, cristall):
        cristal_id = self.names_gen.generate_id()
        self.names_to_crystalls[cristal_id] = cristall

        for cristal_point in cristall.get_points():
            self.points_to_cristalls_names[cristal_point].append(cristal_id)





