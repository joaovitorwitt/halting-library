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

    ###############################################################################
    # Milligrams to Grams Test Case
    ###############################################################################
    def test_convert_milligrams_to_grams(self):
        self.assertEqual(self.mass_conversion.convert_milligrams_to_grams(1000), 1.0)
        self.assertEqual(self.mass_conversion.convert_milligrams_to_grams(2332), 2.332)
        self.assertEqual(self.mass_conversion.convert_milligrams_to_grams(4.6), 0.0046)
        self.assertEqual(self.mass_conversion.convert_milligrams_to_grams(3.9053), 0.0039053)
        self.assertEqual(self.mass_conversion.convert_milligrams_to_grams(0), 0)

    def test_convert_milligrams_to_grams_with_invalid_type_raises_error(self):
        with self.assertRaises(TypeError) as context:
            self.mass_conversion.convert_milligrams_to_grams('string')

        self.assertEqual(str(context.exception), "'str' is not allowed, only integer or float")

    def test_convert_milligrams_to_grams_with_negative_value_raises_error(self):
        with self.assertRaises(ValueError) as context:
            self.mass_conversion.convert_milligrams_to_grams(-1)

        self.assertEqual(str(context.exception), "Negative values are not allowed.")

    ###############################################################################
    # Grams to Kilograms Test Case
    ###############################################################################
    def test_convert_grams_to_kilograms(self):
        self.assertEqual(self.mass_conversion.convert_grams_to_kilograms(0.9), 0.0009)
        self.assertEqual(self.mass_conversion.convert_grams_to_kilograms(2), 0.002)
        self.assertEqual(self.mass_conversion.convert_grams_to_kilograms(34), 0.034)
        self.assertEqual(self.mass_conversion.convert_grams_to_kilograms(286), 0.286)
        self.assertEqual(self.mass_conversion.convert_grams_to_kilograms(9736), 9.736)
        self.assertEqual(self.mass_conversion.convert_grams_to_kilograms(582902), 582.902)

    def test_convert_grams_to_kilograms_with_invalid_type_raises_error(self):
        with self.assertRaises(TypeError) as context:
            self.mass_conversion.convert_grams_to_kilograms('string')

        self.assertEqual(str(context.exception), "'str' is not allowed, only integer or float")

    def test_convert_grams_to_kilograms_with_negative_value_raises_error(self):
        with self.assertRaises(ValueError) as context:
            self.mass_conversion.convert_grams_to_kilograms(-1)

        self.assertEqual(str(context.exception), "Negative values are not allowed.")



if __name__ == "__main__":
    unittest.main()
    