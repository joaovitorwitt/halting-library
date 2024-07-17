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

    ##########################################################
    # Slice list from starting index Test Case
    ##########################################################
    def test_slice_list_from_starting_index(self):
        self.assertEqual(Utils.slice_list_from_starting_index(2, [1,2,3,4,5]), [3,4,5])
        self.assertEqual(Utils.slice_list_from_starting_index(1, ['a', 'b', 'c', 'd', 'e']), ['b', 'c', 'd', 'e'])
        self.assertEqual(Utils.slice_list_from_starting_index(4, [1,2,3,4,5]), [5])

    ##########################################################
    # Slice list from ending index Test Case
    ##########################################################
    def test_slice_list_from_ending_index(self):
        self.assertEqual(Utils.slice_list_from_ending_index(3, ['a', 'b', 'c', 'd', 'e', 'f']), ['a', 'b', 'c'])
        self.assertEqual(Utils.slice_list_from_ending_index(4, ['a', 'b', 'c', 'd', 'e', 'f']), ['a', 'b'])
        self.assertEqual(Utils.slice_list_from_ending_index(5, ['a', 'b', 'c', 'd', 'e', 'f']), ['a'])

if __name__ == "__main__":
    unittest.main()

