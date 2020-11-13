import unittest
def suma(n1, n2):
    return n1+n2
class CajaNegraTest(unittest.TestCase):

    def test_duma_dos_positivos(self):
        numer_1 = 10
        numer_2 = 5
        resultado = suma(numer_1,numer_2)
        self.assertEqual(resultado,15)
if __name__ =='__main__':
    unittest.main()