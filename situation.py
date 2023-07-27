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

    def add_crystall(self, cristall):
        cristal_id = self.names_gen.generate_id()
        self.names_to_crystalls[cristal_id] = cristall
        self.register_ctystall_to_points(cristall.get_points(), cristal_id)


    def register_ctystall_to_points(self, cristall_points, name):
        for cristal_point in cristall_points:
            self.points_to_cristalls_names[cristal_point].append(name)

