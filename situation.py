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
        return index

    #-----------------------------------------------------------
    #----------------------------------------------------------

    def register_crystall_no_modification(self, cristall):
        cristal_id = self.names_gen.generate_id()
        self.names_to_crystalls[cristal_id] = cristall

        for cristal_point in cristall.get_points():
            self.points_to_cristalls_names[cristal_point].append(cristal_id)





