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

    ###############################################################################
    # Kilograms to Tons Test Case
    ###############################################################################
    def test_convert_kilograms_to_tons(self):
        self.assertEqual(self.mass_conversion.convert_kilograms_to_tons(0.9), 0.0009)
        self.assertEqual(self.mass_conversion.convert_kilograms_to_tons(7), 0.007)
        self.assertEqual(self.mass_conversion.convert_kilograms_to_tons(85), 0.085)
        self.assertEqual(self.mass_conversion.convert_kilograms_to_tons(726), 0.726)
        self.assertEqual(self.mass_conversion.convert_kilograms_to_tons(6208), 6.208)
        self.assertEqual(self.mass_conversion.convert_kilograms_to_tons(49807), 49.807)

    def test_convert_kilograms_to_tons_with_invalid_type_raises_error(self):
        with self.assertRaises(TypeError) as context:
            self.mass_conversion.convert_kilograms_to_tons({})

        self.assertEqual(str(context.exception), "'dict' is not allowed, only integer or float")

    def test_convert_kilograms_to_tons_with_negative_value_raises_error(self):
        with self.assertRaises(ValueError) as context:
            self.mass_conversion.convert_kilograms_to_tons(-9)

        self.assertEqual(str(context.exception), "Negative values are not allowed.")

    ###############################################################################
    # Tons to Kilograms Test Case
    ###############################################################################
    def test_convert_tons_to_kilograms(self):
        self.assertEqual(self.mass_conversion.convert_tons_to_kilograms(0.000000736), 0.000736)
        self.assertEqual(self.mass_conversion.convert_tons_to_kilograms(0.009), 9)
        self.assertEqual(self.mass_conversion.convert_tons_to_kilograms(0.9827), 982.7)
        self.assertEqual(self.mass_conversion.convert_tons_to_kilograms(100), 100000)

    def test_convert_tons_to_kilograms_with_invalid_type_raises_error(self):
        with self.assertRaises(TypeError) as context:
            self.mass_conversion.convert_tons_to_kilograms(['list'])

        self.assertEqual(str(context.exception), "'list' is not allowed, only integer or float")

    def test_convert_tons_to_kilograms_with_negative_value_raises_error(self):
        with self.assertRaises(ValueError) as context:
            self.mass_conversion.convert_tons_to_kilograms(-1)

        self.assertEqual(str(context.exception), "Negative values are not allowed.")
    
    ###############################################################################
    # Kilograms to Grams Test Case
    ###############################################################################
    def test_convert_kilograms_to_grams(self):
        self.assertEqual(self.mass_conversion.convert_kilograms_to_grams(0.0062), 6.2)
        self.assertEqual(self.mass_conversion.convert_kilograms_to_grams(9), 9000)
        self.assertEqual(self.mass_conversion.convert_kilograms_to_grams(50), 50000)

    def test_convert_kilograms_to_grams_with_invalid_type_raises_error(self):
        with self.assertRaises(TypeError) as context:
            self.mass_conversion.convert_kilograms_to_grams('string')

        self.assertEqual(str(context.exception), "'str' is not allowed, only integer or float")

    def test_convert_kilogrmas_to_grams_with_negative_value_raises_error(self):
        with self.assertRaises(ValueError) as context:
            self.mass_conversion.convert_kilograms_to_grams(-1)
        
        self.assertEqual(str(context.exception), "Negative values are not allowed.")

    ###############################################################################
    # Grams to Milligrams Test Case
    ###############################################################################
    def test_convert_grams_to_milligrams(self):
        self.assertEqual(self.mass_conversion.convert_grams_to_milligrams(0.006), 6)
        self.assertEqual(self.mass_conversion.convert_grams_to_milligrams(0.000007262), 0.007262)
        self.assertEqual(self.mass_conversion.convert_grams_to_milligrams(674387), 674387000)

    def test_convert_grams_to_milligrams_with_invalid_type_raises_error(self):
        with self.assertRaises(TypeError) as context:
            self.mass_conversion.convert_grams_to_milligrams('string')

        self.assertEqual(str(context.exception), "'str' is not allowed, only integer or float")

    def test_convert_grams_to_milligrams_with_negative_value_raises_error(self):
        with self.assertRaises(ValueError) as context:
            self.mass_conversion.convert_grams_to_milligrams(-1)

        self.assertEqual(str(context.exception), "Negative values are not allowed.")

    ###############################################################################
    # Milligrams to Kilograms Test Case
    ###############################################################################
    def test_convert_milligrams_to_kilograms(self):
        self.assertEqual(self.mass_conversion.convert_milligrams_to_kilograms(15), 0.000015)
        self.assertEqual(self.mass_conversion.convert_milligrams_to_kilograms(47328303), 47.328303)
        self.assertEqual(self.mass_conversion.convert_milligrams_to_kilograms(982), 0.000982)

    def test_convert_milligrams_to_kilograms_with_invalid_type_raises_error(self):
        with self.assertRaises(TypeError) as context:
            self.mass_conversion.convert_milligrams_to_kilograms('string')

        self.assertEqual(str(context.exception), "'str' is not allowed, only integer or float")

    def test_convert_milligrams_to_kilograms_with_negative_value_raises_error(self):
        with self.assertRaises(ValueError) as context:
            self.mass_conversion.convert_milligrams_to_kilograms(-1)

        self.assertEqual(str(context.exception), "Negative values are not allowed.")

    ###############################################################################
    # Milligrams to Tons Test Case
    ###############################################################################
    def test_convert_milligrams_to_tons(self):
        self.assertEqual(self.mass_conversion.convert_milligrams_to_tons(1500000000), 1.5)
        self.assertEqual(self.mass_conversion.convert_milligrams_to_tons(15), 0.000000015)
        self.assertEqual(self.mass_conversion.convert_milligrams_to_tons(93739000000000), 93739.0)

    def test_convert_milligrams_to_tons_with_invalid_type_raises_error(self):
        with self.assertRaises(TypeError) as context:
            self.mass_conversion.convert_milligrams_to_tons('string')

        self.assertEqual(str(context.exception), "'str' is not allowed, only integer or float")
    
    def test_convert_milligrams_to_tons_with_negative_value_raises_error(self):
        with self.assertRaises(ValueError) as context:
            self.mass_conversion.convert_milligrams_to_tons(-1)

        self.assertEqual(str(context.exception), "Negative values are not allowed.")

    ###############################################################################
    # Grams to Tons Test Case
    ###############################################################################
    def test_convert_grams_to_tons(self):
        self.assertEqual(self.mass_conversion.convert_grams_to_tons(1500000), 1.5)
        self.assertEqual(self.mass_conversion.convert_grams_to_tons(15), 0.000015)
        self.assertEqual(self.mass_conversion.convert_grams_to_tons(0.72), 0.00000072)

    def test_convert_grams_to_tons_with_invalid_type_raises_error(self):
        with self.assertRaises(TypeError) as context:
            self.mass_conversion.convert_grams_to_tons('string')

        self.assertEqual(str(context.exception), "'str' is not allowed, only integer or float")

    def test_convert_grams_to_tons_with_negative_value_raises_error(self):
        with self.assertRaises(ValueError) as context:
            self.mass_conversion.convert_grams_to_tons(-1)
        
        self.assertEqual(str(context.exception), "Negative values are not allowed.")

    ###############################################################################
    # Tons to Grams Test Case
    ###############################################################################
    def test_convert_tons_to_grams(self):
        self.assertEqual(self.mass_conversion.convert_tons_to_grams(1.5), 1500000)
        self.assertEqual(self.mass_conversion.convert_tons_to_grams(0.923), 923000)
        self.assertEqual(self.mass_conversion.convert_tons_to_grams(0.000028), 28)

    def test_convert_tons_to_grams_with_invalid_type_raises_error(self):
        with self.assertRaises(TypeError) as context:
            self.mass_conversion.convert_tons_to_grams('string')

        self.assertEqual(str(context.exception), "'str' is not allowed, only integer or float")

    def test_convert_tons_to_grams_with_negative_values_raises_error(self):
        with self.assertRaises(ValueError) as context:
            self.mass_conversion.convert_tons_to_grams(-1)

        self.assertEqual(str(context.exception), "Negative values are not allowed.")
    
    ###############################################################################
    # Tons to Milligrams Test Case
    ###############################################################################
    def test_convert_tons_to_milligrams(self):
        self.assertEqual(self.mass_conversion.convert_tons_to_milligrams(1.5), 1500000000)
        self.assertEqual(self.mass_conversion.convert_tons_to_milligrams(4234), 4234000000000)
        self.assertEqual(self.mass_conversion.convert_tons_to_milligrams(0.000000009), 9)

    def test_convert_tons_to_milligrams_with_invalid_type_raises_error(self):
        with self.assertRaises(TypeError) as context:
            self.mass_conversion.convert_tons_to_milligrams('string')

        self.assertEqual(str(context.exception), "'str' is not allowed, only integer or float")

    def test_convert_tons_to_milligrams_with_negative_value_raises_error(self):
        with self.assertRaises(ValueError) as context:
            self.mass_conversion.convert_tons_to_milligrams(-1)
        
        self.assertEqual(str(context.exception), "Negative values are not allowed.")

    ###############################################################################
    # Kilograms to Milligrams Test Case
    ###############################################################################
    def test_convert_kilograms_to_milligrams(self):
        self.assertEqual(self.mass_conversion.convert_kilograms_to_milligrams(5.6), 5600000)
        self.assertEqual(self.mass_conversion.convert_kilograms_to_milligrams(0.272029), 272029)
        self.assertEqual(self.mass_conversion.convert_kilograms_to_milligrams(709287), 709287000000)

    def test_convert_kilograms_to_milligrams_with_invalid_type_raises_error(self):
        with self.assertRaises(TypeError) as context:
            self.mass_conversion.convert_kilograms_to_milligrams('string')
        
        self.assertEqual(str(context.exception), "'str' is not allowed, only integer or float")

    def test_convert_kilograms_to_milligrams_with_negative_value_raises_error(self):
        with self.assertRaises(ValueError) as context:
            self.mass_conversion.convert_kilograms_to_milligrams(-1)

        self.assertEqual(str(context.exception), "Negative values are not allowed.")

if __name__ == "__main__":
    unittest.main()
    