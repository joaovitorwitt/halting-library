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
    def test_multiplication_factor_in_repeating_sequence(self):
        self.assertEqual(Utils.multiplication_factor_in_repeating_sequence(2), 100)
        self.assertEqual(Utils.multiplication_factor_in_repeating_sequence(1), 10)
        self.assertEqual(Utils.multiplication_factor_in_repeating_sequence(3), 1000)
        self.assertEqual(Utils.multiplication_factor_in_repeating_sequence(4), 10000)


    def test_multiplication_factor_in_repeating_sequence_raises_error_with_invalid_instance(self):
        with self.assertRaises(TypeError) as context:
            Utils.multiplication_factor_in_repeating_sequence('1')

        self.assertEqual(str(context.exception), "'str' is not allowed.")


if __name__ == "__main__":
    unittest.main()