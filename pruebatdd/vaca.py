class Vaca(object):
    def __init__(self,nom,pes,raca):
        self.nom=nom
        self.pes=pes
        self.raca=raca

    def getLlet(self):
        return self.pes * self.raca.litresPerKg

    def getNom(self):
        return self.nom
