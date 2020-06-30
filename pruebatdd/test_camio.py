from mockito import mock, when
from twisted.trial import unittest
from pruebatdd.camio import Camio
from pruebatdd.vaca import Vaca

class TestCamio(unittest.TestCase):
    def test_add(self):
        vaca = mock(Vaca)
        when(vaca).getNom().thenReturn('pinta')
        camio = Camio()
        camio.add(vaca)
        exist = True if vaca.getNom() in camio.vacas else False
        self.assertEqual(exist,True)

    def test_substract(self):
        vaca = mock(Vaca)
        when(vaca).getNom().thenReturn('pinta')
        camio = Camio()
        camio.substract(vaca)
        exist = True if vaca.getNom() in camio.vacas else False
        self.assertEqual(exist, False)

