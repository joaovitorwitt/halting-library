##################################################
# Imports
##################################################
import unittest
from unittest import TestCase

from src.halting.utils import Utils

##################################################
# Utils Test Case Implementation
##################################################
class UtilsTestCase(TestCase):

    ##########################################################
    # Multiplication Factor in Repeating Sequence Test Case
    ##########################################################
    def test_multiplication_factor_in_repeating_sequence(self):
        self.assertEqual(Utils.multiplication_factor_in_repeating_sequence(2), 100)
        self.assertEqual(Utils.multiplication_factor_in_repeating_sequence(1), 10)
        self.assertEqual(Utils.multiplication_factor_in_repeating_sequence(3), 1000)
        self.assertEqual(Utils.multiplication_factor_in_repeating_sequence(4), 10000)

    def test_multiplication_factor_in_repeating_sequence_raises_error_with_invalid_instance(self):
        with self.assertRaises(TypeError) as context:
            Utils.multiplication_factor_in_repeating_sequence('1')

        self.assertEqual(str(context.exception), "'str' is not allowed.")

    ##########################################################
    # Convert Integer to List Test Case
    ##########################################################
    def test_convert_integer_to_list(self):
        self.assertEqual(Utils.convert_integer_to_list(123), ['1', '2', '3'])
        self.assertEqual(Utils.convert_integer_to_list(345), ['3', '4', '5'])
        self.assertEqual(Utils.convert_integer_to_list(34.505050), ['3', '4', '.', '5', '0', '5', '0', '5'])

    def test_convert_integer_to_list_raises_error_with_invalid_instance(self):
        with self.assertRaises(TypeError) as context:
            Utils.convert_integer_to_list('evea')

        self.assertEqual(str(context.exception), "'str' is not allowed.")

if __name__ == "__main__":
    unittest.main()