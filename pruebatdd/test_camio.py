from twisted.trial import unittest
from pruebatdd.camio import Camio

class TestCamio(unittest.TestCase):
    def test_add(self,vaca,camio):
        camio.add(vaca)
        exist = True if vaca.nom in camio.vacas else False
        self.assertEqual(exist,True)

    def test_substract(self,vaca,camio):
        camio.substract(vaca)
        exist = True if vaca.nom in camio.vacas else False
        self.assertEqual(exist, False)

