from grower import OneKristalGrower
from bassin import Bassin
from utils import IdsGen
from cristall import Cristall, init_cristall_from_points


class Typo:
    def __init__(self, parent_name, point, val):
        self.parent_name = parent_name
        self.point = point
        self.val = val


class Situation:
    def __init__(self, full_signal):
        self.full_signal = full_signal

        self.names_to_crystalls = {} # int :cristall

        self.points_to_cristalls_names = {} # point : [name1, name2,...] последний самый "молодой"
        for i in range(len(full_signal)):
            self.points_to_cristalls_names[i] = []

        self.names_gen = IdsGen()


    #  -- для  обучения --------------------------------------------
    def init_grower_from_point(self, point): # автоопределение родителя, автоопеределение бассейна, вал
        parent_cristall_name = self.get_best_cristall_name_for_point(point)
        if parent_cristall_name is None:
            bassin = self.get_bassin_no_cristalls()
            allowed_points = self.get_allowed_points_no_cristalls(point)
        else:
            parent_cristall = self.names_to_crystalls[parent_cristall_name]
            bassin = self.get_bassin_by_cristall(parent_cristall)
            allowed_points = parent_cristall.get_points()
        grower = OneKristalGrower(point, allowed_points, bassin)

        return parent_cristall_name, grower

    def get_worst_point(self):
        point_err_worst = None
        point_index_worst = None
        for point in range(len(self.full_signal)):
            latest_cristall_name = self.get_best_cristall_name_for_point(point)
            latest_cristall =self.names_to_crystalls[latest_cristall_name]
            err_in_point = latest_cristall.get_err_in_point(point)

            if point_err_worst is None:
                point_err_worst = err_in_point
                point_index_worst = point
            else:
                if point_err_worst< err_in_point:
                    point_err_worst = err_in_point
                    point_index_worst = point

        return point_index_worst


    #  -- для распознавания по предсказанию ------------------------
    def init_grower_from_typo(self, typo):

        return parent_name, grower

    # -- для добавления результатов распознавания в ситуацию

    def add_crystall(self, parent_name, cristall):
        if parent_name is None:
            self.register_crystall_no_modification(cristall)
        else:
            cristalls = self.induse_cristalls_childen(parent_name, cristall)
            for crist in cristalls:
                self.register_crystall_no_modification(crist)


    #-----------------------------------------------------------
    #----------------------------------------------------------
    def induse_cristalls_childen(self, parent_name, cristall):
        central_crisstall = init_cristall_from_points(full_signal=self.full_signal, points= cristall.get_points())
        children = [central_crisstall]
        b1 = cristall.get_b1()
        if b1 >0:
            left_child_points = list(range(0, b1))
            left_child = init_cristall_from_points(self.full_signal, points=left_child_points)
            children.append(left_child)

        b2 = cristall.get_b2()
        if b2 < len(cristall.get_points())-1:
            right_child_points = list(range(b2, len(cristall.get_points())))
            right_child = init_cristall_from_points(self.full_signal, points=right_child_points)
            children.append(right_child)

        return children

    def get_bassin_by_cristall(self, parent_cristall):
        global_indexes = parent_cristall.get_points()
        vals = parent_cristall.get_vals()
        bassin = Bassin(vals, global_indexes)
        return bassin

    def get_best_cristall_name_for_point(self, point):
        names = self.points_to_cristalls_names[point]
        if len(names) == 0:
            return None
        best_cristall_name = names[-1]
        return best_cristall_name

    def register_crystall_no_modification(self, cristall):
        cristal_id = self.names_gen.generate_id()
        self.names_to_crystalls[cristal_id] = cristall

        for cristal_point in cristall.get_points():
            self.points_to_cristalls_names[cristal_point].append(cristal_id)





