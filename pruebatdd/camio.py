class Camio(object):
    def __init__(self,):
        self.vacas = {}
        self.pesMaxim = 150

    def add(self,vaca):
        if self.superaPes(vaca.getPes()):
            print ('Imposible carregar vaca. Sobrepasat límit pes')
        else:
            self.vacas[vaca.getNom()]=vaca

    def substract(self,vaca):
        try:
            del self.vacas[vaca.getNom()]
        except:
            print ("No existe esa vaca")

    def quantitatLlet(self):
        total=0
        for key, vaca in self.vacas.items():
             total+=vaca.getLlet()
        return total

    def superaPes(self,pes):
        total=0
        for key, vacaa in self.vacas.items():
             total+=vacaa.getPes()
        return True if total + pes > self.pesMaxim else False

