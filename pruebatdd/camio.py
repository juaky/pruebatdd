class Camio(object):
    def __init__(self,):
        self.vacas = {}

    def add(self,vaca):
        self.vacas[vaca.getNom()]=vaca

    def substract(self,vaca):
        del self.vacas[vaca.getNom()]

    # def quantitatLlet(self):
    #     pass
    #
    # def controlaPes(self):
    #     pass

