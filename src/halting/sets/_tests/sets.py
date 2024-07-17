##################################################
# Imports
##################################################
import unittest
from unittest import TestCase
from src.halting.sets.sets import Sets

##################################################
# Sets Test Case Implementation
##################################################
class SetsTestCase(TestCase):
    def setUp(self) -> None:
        self.sets = Sets()
        return super().setUp()
    
    ##################################################
    # Whole Numbers Test Case Implementation
    ##################################################
    def test_is_number_natural(self):
        self.assertTrue(self.sets.is_number_natural(2))
        self.assertTrue(self.sets.is_number_natural(112))
        self.assertTrue(self.sets.is_number_natural(2432))
        self.assertTrue(self.sets.is_number_natural(0))

        self.assertFalse(self.sets.is_number_natural(-2))
        self.assertFalse(self.sets.is_number_natural(2.3))
        self.assertFalse(self.sets.is_number_natural(0.1))
        self.assertFalse(self.sets.is_number_natural(-0.1))

    def test_is_number_natural_with_invalid_type(self):
        with self.assertRaises(TypeError) as context:
            self.sets.is_number_natural('123')

        self.assertEqual(str(context.exception), "'str' is not allowed.")

    ##################################################
    # Integer Numbers Test Case Implementation
    ##################################################
    def test_is_number_integer(self):
        self.assertTrue(self.sets.is_number_integer(2))
        self.assertTrue(self.sets.is_number_integer(-2))
        self.assertTrue(self.sets.is_number_integer(0))
        self.assertTrue(self.sets.is_number_integer(-323))

        self.assertFalse(self.sets.is_number_integer(3.2))
        self.assertFalse(self.sets.is_number_integer(3.14))
        self.assertFalse(self.sets.is_number_integer(-0.2))
        self.assertFalse(self.sets.is_number_integer(4/3))

    def test_is_number_integer_with_invalid_type_raises_error(self):
        with self.assertRaises(TypeError) as context:
            self.sets.is_number_integer('asd')

        self.assertEqual(str(context.exception), "'str' is not allowed.")

    ##################################################
    # Rational Numbers Test Case Implementation
    ##################################################
    def test_is_number_rational(self):
        pass

    ##################################################
    # Irrational Numbers Test Case Implementation
    ##################################################
    def test_is_number_irrational(self):
        pass

if __name__ == "__main__":
    unittest.main()

