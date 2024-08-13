###########################################################################
# Imports
###########################################################################
import unittest
from unittest import TestCase
from src.halting.core.numbers import Numbers


###########################################################################
# Implementation
###########################################################################
class NumbersTestCase(TestCase):

    def setUp(self) -> None:
        self.numbers = Numbers()
        return super().setUp()


    def test_is_number_natural(self):
        self.assertTrue(self.numbers.is_number_natural(2))
        self.assertTrue(self.numbers.is_number_natural(2))
        self.assertTrue(self.numbers.is_number_natural(432))
        self.assertTrue(self.numbers.is_number_natural(0))
        self.assertFalse(self.numbers.is_number_natural(-9.3))
        self.assertFalse(self.numbers.is_number_natural(2.3))
        self.assertFalse(self.numbers.is_number_natural(0, include_zero=False))
        self.assertFalse(self.numbers.is_number_natural(0.2))


    def test_is_number_integer(self):
        self.assertTrue(self.numbers.is_number_integer(2))
        self.assertTrue(self.numbers.is_number_integer(-2))
        self.assertTrue(self.numbers.is_number_integer(3))
        self.assertTrue(self.numbers.is_number_integer(343))
        self.assertFalse(self.numbers.is_number_integer(-0.3))
        self.assertFalse(self.numbers.is_number_integer(9.2))
        self.assertFalse(self.numbers.is_number_integer(3.2))
        self.assertFalse(self.numbers.is_number_integer(9.2))


    def test_is_number_rational(self):
        pass


    def test_is_number_irrational(self):
        pass


    def test_is_number_real(self):
        pass


    def test_calculate_number_of_significant_figures(self):
        self.assertEqual(self.numbers.calculate_number_of_significant_figures('1200200'), 5)
        self.assertEqual(self.numbers.calculate_number_of_significant_figures('345'), 3)
        self.assertEqual(self.numbers.calculate_number_of_significant_figures('40005000600'), 9)
        self.assertEqual(self.numbers.calculate_number_of_significant_figures('900040000'), 5)
        
        self.assertEqual(self.numbers.calculate_number_of_significant_figures('0.001'), 1)
        self.assertEqual(self.numbers.calculate_number_of_significant_figures('0.01020'), 4)
        self.assertEqual(self.numbers.calculate_number_of_significant_figures('3223.100'), 7)
        self.assertEqual(self.numbers.calculate_number_of_significant_figures('0.02920'), 4)


    def test_scientific_notation_to_integer(self):
        pass


    # def test_convert_number_to_scientific_notation(self):
    #     self.assertEqual(self.numbers.convert_number_to_scientific_notation(50000000), '5e7')
    #     self.assertEqual(self.numbers.convert_number_to_scientific_notation(45600000), '4.56e7')
    #     self.assertEqual(self.numbers.convert_number_to_scientific_notation(0.00000000098), '9.8e-10')
    #     self.assertEqual(self.numbers.convert_number_to_scientific_notation(120000000, notation_type='n'), '1.2 x 10^-8')


    def test_convert_decimal_to_fraction(self):
        self.assertEqual(self.numbers.convert_decimal_to_fraction(0.161616), '16/99')
        self.assertEqual(self.numbers.convert_decimal_to_fraction(4.555555), '41/9')
        self.assertEqual(self.numbers.convert_decimal_to_fraction(2.777777), '25/9')

    
    def test_is_number_prime(self):
        self.assertTrue(self.numbers.is_number_prime(113))
        self.assertTrue(self.numbers.is_number_prime(100003))
        self.assertTrue(self.numbers.is_number_prime(100043))
        self.assertTrue(self.numbers.is_number_prime(100057))

        self.assertFalse(self.numbers.is_number_prime(100000))
        self.assertFalse(self.numbers.is_number_prime(100001))
        self.assertFalse(self.numbers.is_number_prime(100002))
        self.assertFalse(self.numbers.is_number_prime(100004))
        self.assertFalse(self.numbers.is_number_prime(-100005))


    def test_is_number_composite(self):
        self.assertTrue(self.numbers.is_number_composite(100000))
        self.assertTrue(self.numbers.is_number_composite(100001))
        self.assertTrue(self.numbers.is_number_composite(100002))
        self.assertTrue(self.numbers.is_number_composite(100004))

        self.assertFalse(self.numbers.is_number_composite(113))
        self.assertFalse(self.numbers.is_number_composite(100003))
        self.assertFalse(self.numbers.is_number_composite(100043))
        self.assertFalse(self.numbers.is_number_composite(100057))
    

if __name__ == "__main__":
    unittest.main()