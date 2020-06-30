from mockito import mock, when
from twisted.trial import unittest
from pruebatdd.camio import Camio
from pruebatdd.vaca import Vaca

class TestCamio(unittest.TestCase):

    def test_add(self):
        vaca = mock(Vaca)
        when(vaca).getNom().thenReturn('pinta')
        when(vaca).getPes().thenReturn(100)
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

    def test_quantitatLlet(self):
        vaca = mock(Vaca)
        when(vaca).getLlet().thenReturn(200)
        when(vaca).getNom().thenReturn('pinta')
        camio=Camio()
        camio.vacas[vaca.getNom()]=vaca
        litres = camio.quantitatLlet()
        self.assertEqual(litres,vaca.getLlet())

    def test_superaPes(self):
        camio = Camio()
        camio.pesMaxim =150
        vaca = mock(Vaca)
        when(vaca).getPes().thenReturn(200)
        when(vaca).getNom().thenReturn('pinta')
        camio.vacas[vaca.getNom()] = vaca
        superapes = camio.superaPes(vaca.getPes())
        self.assertEqual(superapes, True)
