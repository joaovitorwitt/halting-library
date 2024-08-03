##################################################
# Imports
##################################################
import unittest
from unittest import TestCase

from src.halting.core.algebra import AlgebraFormulas

##################################################
# Algebra Test Case Implementation
##################################################
class AlgebraFormulasTestCase(TestCase):

    def setUp(self) -> None:
        self.algebra = AlgebraFormulas()
        return super().setUp()
    
    ##################################################
    # Calculate Expoenent Test Case Implementation
    ##################################################
    def test_calculate_exponent(self):
        self.assertEqual(self.algebra.calculate_exponent(2, 5), 32)
        self.assertEqual(self.algebra.calculate_exponent(23, 2), 529)
        self.assertEqual(self.algebra.calculate_exponent(10, 0), 1)
        self.assertEqual(self.algebra.calculate_exponent(5, -2), 0.04)
        self.assertEqual(self.algebra.calculate_exponent(-5, 3), -125)

    def test_calculate_with_invalid_type_raises_error(self):
        with self.assertRaises(TypeError) as context:
            self.algebra.calculate_exponent(1, 'invalid')

        self.assertEqual(str(context.exception), "'str' is not allowed.")

    ##################################################
    # Square Root Test Case Implementation
    ##################################################
    def test_square_root(self):
        self.assertEqual(self.algebra.square_root(16), 4)
        self.assertEqual(self.algebra.square_root(144), 12)
        self.assertEqual(self.algebra.square_root(169), 13)

    def test_square_root_with_invalid_type_raises_error(self):
        with self.assertRaises(TypeError) as context:
            self.algebra.square_root('invalid')

        self.assertEqual(str(context.exception), "'str' is not allowed, only integer or float")

    def test_square_root_with_negative_value_raises_error(self):
        with self.assertRaises(ValueError) as context:
            self.algebra.square_root(-1)

        self.assertEqual(str(context.exception), "Negative values are not allowed.")

    ##################################################
    # Cubic Root Test Case Implementation
    ##################################################
    def test_cubic_root(self):
        self.assertEqual(self.algebra.cubic_root(-8), -2)
        self.assertEqual(self.algebra.cubic_root(729), 9)
        self.assertEqual(self.algebra.cubic_root(512), 8)

    def test_cubic_root_with_invalid_type_raises_error(self):
        with self.assertRaises(TypeError) as context:
            self.algebra.cubic_root(["list"])

        self.assertEqual(str(context.exception), "'list' is not allowed.")

    ##################################################
    # Absolute Value Test Case Implementation
    ##################################################
    def test_absolute_value(self):
        self.assertEqual(self.algebra.calculate_absolute_value(-2928), 2928)
        self.assertEqual(self.algebra.calculate_absolute_value(-9), 9)
        self.assertEqual(self.algebra.calculate_absolute_value(928), 928)

    def test_absolute_value_with_invalid_type_raises_error(self):
        with self.assertRaises(TypeError) as context:
            self.algebra.calculate_absolute_value({"key": "value"})

        self.assertEqual(str(context.exception), "'dict' is not allowed.")


if __name__ == "__main__":
    unittest.main()
