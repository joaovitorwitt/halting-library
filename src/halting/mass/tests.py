###############################################################################
# Imports
###############################################################################
import unittest
from unittest import TestCase

from src.halting.mass.mass import MassConversion

###############################################################################
# Mass Conversion Test Case Implementation
###############################################################################
class MassConversionTestCase(TestCase):

    def setUp(self) -> None:
        self.mass_conversion = MassConversion()
        return super().setUp()

    def test_convert_milligrams_to_grams(self):
        result = self.mass_conversion.convert_milligrams_to_grams(1000)
        self.assertEqual(result, 1.0)

    def test_convert_milligrams_to_grams_raises_error(self):
        with self.assertRaises(ValueError) as context:
            self.mass_conversion.convert_milligrams_to_grams('string')

        self.assertEqual(str(context.exception), "Error: 'str' is not allowed, only integer or float values.")

if __name__ == "__main__":
    unittest.main()
    