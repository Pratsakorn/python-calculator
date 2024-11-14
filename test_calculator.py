import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:

    def test_add_neg(self):
        self.assertEqual(self.calc.add(-1, -2), -3)

    # Test subtract

    def test_sub(self):
        self.assertEqual(self.calc.subtract(1, 2), -1)

    def test_sub_neg(self):
        self.assertEqual(self.calc.subtract(-1, -2), 1)

    # Test multiply

    def test_mul(self):
        self.assertEqual(self.calc.multiply(1, 2), 2)

    def test_mul_neg(self):
        self.assertEqual(self.calc.multiply(1, -2), -2)

    # Test divide

    def test_div_byZero(self):
        self.assertEqual(self.calc.divide(2, 0), None)

    def test_div_neg(self):
        self.assertEqual(self.calc.divide(-2, 1), -2)
    
    # Test modulo

    def test_mod_byZero(self):
        self.assertEqual(self.calc.modulo(2, 0), None)

    def test_mod_neg(self):
        self.assertEqual(self.calc.modulo(-2, 3), 1)

if __name__ == '__main__':
    unittest.main()