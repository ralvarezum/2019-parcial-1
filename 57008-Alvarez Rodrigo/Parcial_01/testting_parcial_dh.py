#Rodrigo Alvarez, 57008 II
import unittest
from interfaz_parcial_dh import interfaz_parcial_dth

#TEST DE LA CONSIGNA

class Test_Decimal_to_Hexa(unittest.TestCase):
    def test_dem_to_hex_5(self):
        var = interfaz_parcial_dth(5)
        self.assertEqual(var,'5')
    def test_dem_to_hex_10(self):
        var = interfaz_parcial_dth(10)
        self.assertEqual(var,'A')
    def test_dem_to_hex_ABCDEFG(self):
        var = interfaz_parcial_dth('ABCDEFG')
        self.assertEqual(var,'Disculpe, solo acepto números!')
    def test_dem_to_hex_17(self):
        var = interfaz_parcial_dth(17)
        self.assertEqual(var,'11')
    def test_dem_to_hex_16(self):
        var = interfaz_parcial_dth(16)
        self.assertEqual(var,'10')
    def test_dem_to_hex_4095(self):
        var = interfaz_parcial_dth(4095)
        self.assertEqual(var,'FFF')
    def test_dem_to_hex_1234(self):
        var = interfaz_parcial_dth(1234)
        self.assertEqual(var,'4D2')
    def test_dem_to_hex_234(self):
        var = interfaz_parcial_dth(234)
        self.assertEqual(var,'EA')
    #TEST EXTRAS
    def test_dem_to_hex_379(self):
        var = interfaz_parcial_dth(379)
        self.assertEqual(var,'17B')
    def test_dem_to_hex_1027(self):
        var = interfaz_parcial_dth(1027)
        self.assertEqual(var,'403')
    def test_dem_to_hex_3472(self):
        var = interfaz_parcial_dth(3472)
        self.assertEqual(var,'D90')
    
if __name__ == '__main__':
    unittest.main()