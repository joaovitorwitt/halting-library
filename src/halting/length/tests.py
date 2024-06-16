###############################################################################
# Imports
###############################################################################
import unittest
from unittest import TestCase
from src.halting.length.length import LengthConversion

###############################################################################
# Imports
###############################################################################
class LengthConversionTestCase(TestCase):

    def setUp(self) -> None:
        self.length_conversion = LengthConversion()
        return super().setUp()

    ###############################################################################
    # Millimeters to Centimeters Test Case
    ###############################################################################
    def test_convert_millimeters_to_centimeters(self):
        self.assertEqual(self.length_conversion.convert_millimeters_to_centimeters(1), 0.1)
        self.assertEqual(self.length_conversion.convert_millimeters_to_centimeters(3827), 382.7)
        self.assertEqual(self.length_conversion.convert_millimeters_to_centimeters(0.92828), 0.092828)
        self.assertEqual(self.length_conversion.convert_millimeters_to_centimeters(829273), 82927.3)

    def test_convert_millimeters_to_centimeters_with_invalid_type_raises_error(self):
        with self.assertRaises(TypeError) as context:
            self.length_conversion.convert_millimeters_to_centimeters('string')

        self.assertEqual(str(context.exception), "'str' is not allowed, only integer or float")

    def test_convert_millimeters_to_centimeters_with_negative_value_raises_error(self):
        with self.assertRaises(ValueError) as context:
            self.length_conversion.convert_millimeters_to_centimeters(-1)

        self.assertEqual(str(context.exception), "Negative values are not allowed.")

    ###############################################################################
    # Centimeters to Meters Test Case
    ###############################################################################
    def test_convert_centimeters_to_meters(self):
        self.assertEqual(self.length_conversion.convert_centimeters_to_meters(0.00928), 0.0000928)
        self.assertEqual(self.length_conversion.convert_centimeters_to_meters(9280), 92.80)
        self.assertEqual(self.length_conversion.convert_centimeters_to_meters(920232000), 9202320.00)
        
    def test_convert_centimeters_to_meters_with_invalid_type_raises_error(self):
        with self.assertRaises(TypeError) as context:
            self.length_conversion.convert_centimeters_to_meters('string')

        self.assertEqual(str(context.exception), "'str' is not allowed, only integer or float")

    def test_convert_centimeters_to_meters_with_negative_value_raises_error(self):
        with self.assertRaises(ValueError) as context:
            self.length_conversion.convert_centimeters_to_meters(-1)

        self.assertEqual(str(context.exception), "Negative values are not allowed.")
            
    ###############################################################################
    # Meters to Kilometers Test Case
    ###############################################################################
    def test_convert_meters_to_kilometers(self):
        self.assertEqual(self.length_conversion.convert_meters_to_kilometers(372), 0.372)
        self.assertEqual(self.length_conversion.convert_meters_to_kilometers(9827), 9.827)
        self.assertEqual(self.length_conversion.convert_meters_to_kilometers(9829029), 9829.029)

    def test_convert_meters_to_kilometers_with_invalid_type_raises_error(self):
        with self.assertRaises(TypeError) as context:
            self.length_conversion.convert_meters_to_kilometers(['list'])

        self.assertEqual(str(context.exception), "'list' is not allowed, only integer or float")

    def test_convert_meters_to_kilometers_with_negative_value_raises_error(self):
        with self.assertRaises(ValueError) as context:
            self.length_conversion.convert_meters_to_kilometers(-1)
        
        self.assertEqual(str(context.exception), "Negative values are not allowed.")

    ###############################################################################
    # Kilometers to Meters Test Case
    ###############################################################################
    def test_convert_kilometers_to_meters(self):
        self.assertEqual(self.length_conversion.convert_kilometers_to_meters(6.5), 6500)
        self.assertEqual(self.length_conversion.convert_kilometers_to_meters(0.0876), 87.6)
        self.assertEqual(self.length_conversion.convert_kilometers_to_meters(93820), 93820000)

    def test_convert_kilometers_to_meters_with_invalid_type_raises_error(self):
        with self.assertRaises(TypeError) as context:
            self.length_conversion.convert_kilometers_to_meters('string')

        self.assertEqual(str(context.exception), "'str' is not allowed, only integer or float")

    def test_convert_kilometers_to_meters_with_negative_value_raises_error(self):
        with self.assertRaises(ValueError) as context:
            self.length_conversion.convert_kilometers_to_meters(-1)

        self.assertEqual(str(context.exception), "Negative values are not allowed.")

    ###############################################################################
    # Meters to Centimeters Test Case
    ###############################################################################
    def test_convert_meters_to_centimeters(self):
        self.assertEqual(self.length_conversion.convert_meters_to_centimeters(10), 1000)
        self.assertEqual(self.length_conversion.convert_meters_to_centimeters(208320832), 20832083200)
        self.assertEqual(self.length_conversion.convert_meters_to_centimeters(0.89082), 89.082)

    def test_convert_meters_to_centimeters_with_invalid_type_raises_error(self):
        with self.assertRaises(TypeError) as context:
            self.length_conversion.convert_meters_to_centimeters({"key": "value"})

        self.assertEqual(str(context.exception), "'dict' is not allowed, only integer or float")

    def test_convert_meters_to_centimeters_with_negative_value_raises_error(self):
        with self.assertRaises(ValueError) as context:
            self.length_conversion.convert_meters_to_centimeters(-1)
        
        self.assertEqual(str(context.exception), "Negative values are not allowed.")

    ###############################################################################
    # Centimeters to Millimeters Test Case
    ###############################################################################
    def test_convert_centimeters_to_millimeters(self):
        self.assertEqual(self.length_conversion.convert_centimeters_to_millimeters(0.0289), 0.289)
        self.assertEqual(self.length_conversion.convert_centimeters_to_millimeters(9202), 92020)
        self.assertEqual(self.length_conversion.convert_centimeters_to_millimeters(8272.9092), 82729.092)

    def test_convert_centimeters_to_millimeters_with_invalid_type_raises_error(self):
        with self.assertRaises(TypeError) as context:
            self.length_conversion.convert_centimeters_to_millimeters('str')

        self.assertEqual(str(context.exception), "'str' is not allowed, only integer or float")

    def test_convert_centimeters_to_millimeters_with_negative_value_raises_error(self):
        with self.assertRaises(ValueError) as context:
            self.length_conversion.convert_centimeters_to_millimeters(-1)

        self.assertEqual(str(context.exception), "Negative values are not allowed.")

    ###############################################################################
    # Millimeters to Meters Test Case
    ###############################################################################
    def test_convert_millimeters_to_meters(self):
        self.assertEqual(self.length_conversion.convert_millimeters_to_meters(49), 0.049)
        self.assertEqual(self.length_conversion.convert_millimeters_to_meters(872), 0.872)
        self.assertEqual(self.length_conversion.convert_millimeters_to_meters(0.292), 0.000292)
        self.assertEqual(self.length_conversion.convert_millimeters_to_meters(29827), 29.827)

    def test_convert_millimeters_to_meters_with_invalid_type_raises_error(self):
        with self.assertRaises(TypeError) as context:
            self.length_conversion.convert_millimeters_to_meters('string')

        self.assertEqual(str(context.exception), "'str' is not allowed, only integer or float")

    def test_convert_millimeters_to_meters_with_negative_value_raises_error(self):
        with self.assertRaises(ValueError) as context:
            self.length_conversion.convert_millimeters_to_meters(-1)

        self.assertEqual(str(context.exception), "Negative values are not allowed.")

    ###############################################################################
    # Millimeters to Kilometers Test Case
    ###############################################################################
    def test_convert_millimeters_to_kilometers(self):
        self.assertEqual(self.length_conversion.convert_millimeters_to_kilometers(1), 0.000001)
        self.assertEqual(self.length_conversion.convert_millimeters_to_kilometers(1292083), 1.292083)
        self.assertEqual(self.length_conversion.convert_millimeters_to_kilometers(0.00928), 0.00000000928)
        self.assertEqual(self.length_conversion.convert_millimeters_to_kilometers(182), 0.000182)

    def test_convert_millimeters_to_kilometers_with_invalid_type_raises_error(self):
        with self.assertRaises(TypeError) as context:
            self.length_conversion.convert_millimeters_to_kilometers('string')

        self.assertEqual(str(context.exception), "'str' is not allowed, only integer or float")

    def test_convert_millimeters_to_kilometers_with_negative_value_raises_error(self):
        with self.assertRaises(ValueError) as context:
            self.length_conversion.convert_millimeters_to_kilometers(-1)
        
        self.assertEqual(str(context.exception), "Negative values are not allowed.")

    ###############################################################################
    # Kilometers to Centimeters Test Case
    ###############################################################################
    def test_convert_kilometers_to_centimeters(self):
        self.assertEqual(self.length_conversion.convert_kilometers_to_centimeters(9), 900000)
        self.assertEqual(self.length_conversion.convert_kilometers_to_centimeters(0.21), 21000)
        self.assertEqual(self.length_conversion.convert_kilometers_to_centimeters(2920), 292000000)
        self.assertEqual(self.length_conversion.convert_kilometers_to_centimeters(7), 700000)

    def test_convert_kilometers_to_centimeters_with_invalid_type_raises_error(self):
        with self.assertRaises(TypeError) as context:
            self.length_conversion.convert_kilometers_to_centimeters('string')

        self.assertEqual(str(context.exception), "'str' is not allowed, only integer or float")

    def test_convert_kilometers_to_centimeters_with_negative_value_raises_error(self):
        with self.assertRaises(ValueError) as context:
            self.length_conversion.convert_kilometers_to_centimeters(-1)

        self.assertEqual(str(context.exception), "Negative values are not allowed.")

    ###############################################################################
    # Kilometers to Millimeters Test Case
    ###############################################################################
    def test_convert_kilometers_to_millimeters(self):
        self.assertEqual(self.length_conversion.convert_kilometers_to_millimeters(9), 9000000)
        self.assertEqual(self.length_conversion.convert_kilometers_to_millimeters(0.000008), 8)
        self.assertEqual(self.length_conversion.convert_kilometers_to_millimeters(290.87), 290870000)

    def test_convert_kilometers_to_millimeters_with_invalid_type_raises_error(self):
        with self.assertRaises(TypeError) as context:
            self.length_conversion.convert_kilometers_to_millimeters('string')

        self.assertEqual(str(context.exception), "'str' is not allowed, only integer or float")

    def test_convert_kilometers_to_millimeters_with_negative_value_raises_error(self):
        with self.assertRaises(ValueError) as context:
            self.length_conversion.convert_kilometers_to_millimeters(-1)

        self.assertEqual(str(context.exception), "Negative values are not allowed.")
            
    ###############################################################################
    # Meters to Millimeters Test Case
    ###############################################################################
    def test_convert_meters_to_millimeters(self):
        self.assertEqual(self.length_conversion.convert_meters_to_millimeters(0.003), 3)
        self.assertEqual(self.length_conversion.convert_meters_to_millimeters(34), 34000)
        self.assertEqual(self.length_conversion.convert_meters_to_millimeters(9.28), 9280)

    def test_convert_meters_to_millimeters_with_invalid_type_raises_error(self):
        with self.assertRaises(TypeError) as context:
            self.length_conversion.convert_meters_to_millimeters('string')

        self.assertEqual(str(context.exception), "'str' is not allowed, only integer or float")

    def test_convert_meters_to_millimeters_with_negative_value_raises_error(self):
        with self.assertRaises(ValueError) as context:
            self.length_conversion.convert_meters_to_millimeters(-1)

        self.assertEqual(str(context.exception), "Negative values are not allowed.")
        
    ###############################################################################
    # Centimeters to Kilometers Test Case
    ###############################################################################
    def test_convert_centimeters_to_kilometers(self):
        self.assertEqual(self.length_conversion.convert_centimeters_to_kilometers(340), 0.00340)
        self.assertEqual(self.length_conversion.convert_centimeters_to_kilometers(29834), 0.29834)
        self.assertEqual(self.length_conversion.convert_centimeters_to_kilometers(0.098), 0.00000098)

    def test_convert_centimeters_to_kilometers_with_invalid_type_raises_error(self):
        with self.assertRaises(TypeError) as context:
            self.length_conversion.convert_centimeters_to_kilometers('sad')

        self.assertEqual(str(context.exception), "'str' is not allowed, only integer or float")

    def test_convert_centimeters_to_kilometers_with_negative_value_raises_error(self):
        with self.assertRaises(ValueError) as context:
            self.length_conversion.convert_centimeters_to_kilometers(-1)

        self.assertEqual(str(context.exception), "Negative values are not allowed.")

if __name__ == "__main__":
    unittest.main()
