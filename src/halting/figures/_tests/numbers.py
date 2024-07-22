##################################################
# Imports
##################################################
import unittest
from unittest import TestCase

from src.halting.figures.numbers import ManageFigures

##################################################
# Manage Figures Test Case Implementation
##################################################
class ManageFiguresTestCase(TestCase):

    def setUp(self) -> None:
        self.figures = ManageFigures()
        return super().setUp()
    
    ######################################################
    # Calculate number of significant figures Test Case
    ######################################################
    def test_calculate_number_of_significant_figures(self):
        self.assertEqual(self.figures.calculate_number_of_significant_figures('1200200'), 5)
        self.assertEqual(self.figures.calculate_number_of_significant_figures('345'), 3)
        self.assertEqual(self.figures.calculate_number_of_significant_figures('40005000600'), 9)
        self.assertEqual(self.figures.calculate_number_of_significant_figures('900040000'), 5)
        
        self.assertEqual(self.figures.calculate_number_of_significant_figures('0.001'), 1)
        self.assertEqual(self.figures.calculate_number_of_significant_figures('0.01020'), 4)
        self.assertEqual(self.figures.calculate_number_of_significant_figures('3223.100'), 7)
        self.assertEqual(self.figures.calculate_number_of_significant_figures('0.02920'), 4)

    ######################################################
    # Convert Decimal to Fraction Test Case
    ######################################################
    def test_convert_decimal_to_fraction(self):
        self.assertEqual(self.figures.convert_decimal_to_fraction(0.161616), '16/99')
        self.assertEqual(self.figures.convert_decimal_to_fraction(4.555555), '41/9')
        self.assertEqual(self.figures.convert_decimal_to_fraction(2.777777), '25/9')


    ######################################################
    # Sieve Of Erastosthenes Algorithm Test Case
    ######################################################
    def test_sieve_of_erastosthenes(self):
        self.assertListEqual(self.figures.sieve_of_erastosthenes(20), [2, 3, 5, 7, 11, 13, 17, 19])
        self.assertListEqual(self.figures.sieve_of_erastosthenes(100), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])
        self.assertListEqual(self.figures.sieve_of_erastosthenes(2), [2])

    ######################################################
    # Is Number Prime Test Case
    ######################################################
    def test_is_number_prime(self):
        self.assertTrue(self.figures.is_number_prime(113))
        self.assertTrue(self.figures.is_number_prime(100003))
        self.assertTrue(self.figures.is_number_prime(100043))
        self.assertTrue(self.figures.is_number_prime(100057))

        self.assertFalse(self.figures.is_number_prime(100000))
        self.assertFalse(self.figures.is_number_prime(100001))
        self.assertFalse(self.figures.is_number_prime(100002))
        self.assertFalse(self.figures.is_number_prime(100004))
        self.assertFalse(self.figures.is_number_prime(-100005))

    ######################################################
    # Is Number Composite Test Case
    ######################################################
    def test_is_number_composite(self):
        self.assertTrue(self.figures.is_number_composite(100000))
        self.assertTrue(self.figures.is_number_composite(100001))
        self.assertTrue(self.figures.is_number_composite(100002))
        self.assertTrue(self.figures.is_number_composite(100004))

        self.assertFalse(self.figures.is_number_composite(113))
        self.assertFalse(self.figures.is_number_composite(100003))
        self.assertFalse(self.figures.is_number_composite(100043))
        self.assertFalse(self.figures.is_number_composite(100057))

if __name__ == "__main__":
    unittest.main()
