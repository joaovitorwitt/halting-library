##################################################
# Imports
##################################################
import unittest
from unittest import TestCase

from src.halting.core.algebra import Algebra

###########################################################################
# Implementation
###########################################################################
class AlgebraTestCase(TestCase):

    def setUp(self) -> None:
        self.algebra = Algebra()
        return super().setUp()
    

    def test_exponent(self):
        self.assertEqual(self.algebra.exponent(2, 5), 32)
        self.assertEqual(self.algebra.exponent(23, 2), 529)
        self.assertEqual(self.algebra.exponent(10, 0), 1)
        self.assertEqual(self.algebra.exponent(5, -2), 0.04)
        self.assertEqual(self.algebra.exponent(-5, 3), -125)


    def test_square_root(self):
        self.assertEqual(self.algebra.square_root(16), 4)
        self.assertEqual(self.algebra.square_root(144), 12)
        self.assertEqual(self.algebra.square_root(169), 13)


    def test_cubic_root(self):
        self.assertEqual(self.algebra.cubic_root(-8), -2)
        self.assertEqual(self.algebra.cubic_root(729), 9)
        self.assertEqual(self.algebra.cubic_root(512), 8)


    def test_absolute_value(self):
        self.assertEqual(self.algebra.absolute_value(-2928), 2928)
        self.assertEqual(self.algebra.absolute_value(-9), 9)
        self.assertEqual(self.algebra.absolute_value(928), 928)


if __name__ == "__main__":
    unittest.main()
