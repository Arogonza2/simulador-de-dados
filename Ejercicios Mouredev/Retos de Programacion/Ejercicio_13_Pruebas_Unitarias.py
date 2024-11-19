

"""
 EJERCICIO:
 * Crea una función que se encargue de sumar dos números y retornar
 su resultado.
 Crea un test, utilizando las herramientas de tu lenguaje, que sea
 capaz de determinar si esa función se ejecuta correctamente.
 
 
"""
import unittest


def sum(a, b):
    return a + b



class TestSum(unittest.TestCase):
    
    def test_sum(self):
        self.assertEqual(sum(5, 7), 12)
        self.assertEqual(sum(5, -7), -2)
        self.assertEqual(sum(0, 0), 0)
        self.assertEqual(sum(2.5, 2.1), 4.6)
        self.assertEqual(sum(2, 2.1), 4.1)
        self.assertEqual(sum(2.5, 2.5), 5)

    def test_sum_type(self):
        with self.assertRaises(ValueError):
            sum("5", 7)
        with self.assertRaises(ValueError):
            sum(5, "7")
        with self.assertRaises(ValueError):
            sum("5", "7")
        with self.assertRaises(ValueError):
            sum("a", 7)
        with self.assertRaises(ValueError):
            sum(None, 7)
        
        
    

unittest.main()

