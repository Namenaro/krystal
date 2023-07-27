
class IdsGen:
    def __init__(self):
        self.i=-1

    def generate_id(self):
        self.i+=1
        return self.i