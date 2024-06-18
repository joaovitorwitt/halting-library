###############################################################################
# Imports
###############################################################################
import unittest
from unittest import TestCase
from src.halting.time.time import TimeConversion

###############################################################################
# Time Conversion Test Case Implementation
###############################################################################
class TimeConversionTestCase(TestCase):
    
    def setUp(self) -> None:
        self.time_conversion = TimeConversion()
        return super().setUp()

    ###############################################################################
    # Milliseconds to Seconds Test Case
    ###############################################################################
    def test_convert_milliseconds_to_seconds(self):
        self.assertEqual(self.time_conversion.convert_milliseconds_to_seconds(3920), 3.920)
        self.assertEqual(self.time_conversion.convert_milliseconds_to_seconds(0.298), 0.000298)
        self.assertEqual(self.time_conversion.convert_milliseconds_to_seconds(293), 0.293)

    def test_convert_milliseconds_to_seconds_with_invalid_type_raises_error(self):
        with self.assertRaises(TypeError) as context:
            self.time_conversion.convert_milliseconds_to_seconds('string')

        self.assertEqual(str(context.exception), "'str' is not allowed, only integer or float")

    def test_convert_milliseconds_to_seconds_with_negative_value_raises_error(self):
        with self.assertRaises(ValueError) as context:
            self.time_conversion.convert_milliseconds_to_seconds(-1)

        self.assertEqual(str(context.exception), "Negative values are not allowed.")

    ###############################################################################
    # Seconds to Minutes Test Case
    ###############################################################################
    def test_convert_seconds_to_minutes(self):
        self.assertEqual(self.time_conversion.convert_seconds_to_minutes(720), 12)
        self.assertEqual(self.time_conversion.convert_seconds_to_minutes(30), 0.5)
        self.assertEqual(self.time_conversion.convert_seconds_to_minutes(1440), 24)
        self.assertEqual(self.time_conversion.convert_seconds_to_minutes(240), 4)

    def test_convert_seconds_to_minutes_with_invalid_type_raises_error(self):
        with self.assertRaises(TypeError) as context:
            self.time_conversion.convert_seconds_to_minutes('string')

        self.assertEqual(str(context.exception), "'str' is not allowed, only integer or float")

    def test_convert_seconds_to_minutes_with_negative_value_raises_error(self):
        with self.assertRaises(ValueError) as context:
            self.time_conversion.convert_seconds_to_minutes(-1)

        self.assertEqual(str(context.exception), "Negative values are not allowed.")

    ###############################################################################
    # Minutes to Hours Test Case
    ###############################################################################
    def test_convert_minutes_to_hours(self):
        self.assertEqual(self.time_conversion.convert_minutes_to_hours(39), 0.65)
        self.assertEqual(self.time_conversion.convert_minutes_to_hours(6), 0.1)
        self.assertEqual(self.time_conversion.convert_minutes_to_hours(402), 6.7)

    def test_convert_minutes_to_hours_with_invalid_type_raises_error(self):
        with self.assertRaises(TypeError) as context:
            self.time_conversion.convert_minutes_to_hours('list')

        self.assertEqual(str(context.exception), "'str' is not allowed, only integer or float")

    def test_convert_minutes_to_hours_with_negative_value_raises_error(self):
        with self.assertRaises(ValueError) as context:
            self.time_conversion.convert_minutes_to_hours(-1)

        self.assertEqual(str(context.exception), "Negative values are not allowed.")

    ###############################################################################
    # Hours to Minutes Test Case
    ###############################################################################
    def test_convert_hours_to_minutes(self):
        self.assertEqual(self.time_conversion.convert_hours_to_minutes(2), 120)
        self.assertEqual(self.time_conversion.convert_hours_to_minutes(0.5), 30)
        self.assertEqual(self.time_conversion.convert_hours_to_minutes(23), 1380)

    def test_convert_hours_to_minutes_with_invalid_type_raises_error(self):
        with self.assertRaises(TypeError) as context:
            self.time_conversion.convert_hours_to_minutes('string')

        self.assertEqual(str(context.exception), "'str' is not allowed, only integer or float")

    def test_convert_hours_to_minutes_with_negative_value_raises_error(self):
        with self.assertRaises(ValueError) as context:
            self.time_conversion.convert_hours_to_minutes(-1)

        self.assertEqual(str(context.exception), "Negative values are not allowed.")

    ###############################################################################
    # Minutes to Seconds Test Case
    ###############################################################################
    def test_convert_minutes_to_seconds(self):
        self.assertEqual(self.time_conversion.convert_minutes_to_seconds(30), 1800)
        self.assertEqual(self.time_conversion.convert_minutes_to_seconds(98), 5880)
        self.assertEqual(self.time_conversion.convert_minutes_to_seconds(0.7), 42)

    def test_convert_minutes_to_seconds_with_invalid_type_raises_error(self):
        with self.assertRaises(TypeError) as context:
            self.time_conversion.convert_minutes_to_seconds('string')

        self.assertEqual(str(context.exception), "'str' is not allowed, only integer or float")

    def test_convert_minutes_to_seconds_with_negative_value_raises_error(self):
        with self.assertRaises(ValueError) as context:
            self.time_conversion.convert_minutes_to_seconds(-1)

        self.assertEqual(str(context.exception), "Negative values are not allowed.")

    ###############################################################################
    # Seconds to Milliseconds Test Case
    ###############################################################################
    def test_convert_seconds_to_milliseconds(self):
        self.assertEqual(self.time_conversion.convert_seconds_to_milliseconds(39), 39000)
        self.assertEqual(self.time_conversion.convert_seconds_to_milliseconds(0.098), 98)
        self.assertEqual(self.time_conversion.convert_seconds_to_milliseconds(293), 293000)

    def test_convert_seconds_to_milliseconds_with_invalid_type_raises_error(self):
        with self.assertRaises(TypeError) as context:
            self.time_conversion.convert_seconds_to_milliseconds('string')

        self.assertEqual(str(context.exception), "'str' is not allowed, only integer or float")
    
    def test_convert_seconds_to_milliseconds_with_negative_value_raises_error(self):
        with self.assertRaises(ValueError) as context:
            self.time_conversion.convert_seconds_to_milliseconds(-1)

        self.assertEqual(str(context.exception), "Negative values are not allowed.")

    ###############################################################################
    # Milliseconds to Minutes Test Case
    ###############################################################################
    def test_convert_milliseconds_to_minutes(self):
        self.assertEqual(self.time_conversion.convert_milliseconds_to_minutes(120000), 2)
        self.assertEqual(self.time_conversion.convert_milliseconds_to_minutes(30000), 0.5)
        self.assertEqual(self.time_conversion.convert_milliseconds_to_minutes(15000), 0.25)

    def test_convert_milliseconds_to_minutes_with_invalid_type_raises_error(self):
        with self.assertRaises(TypeError) as context:
            self.time_conversion.convert_milliseconds_to_minutes('string')

        self.assertEqual(str(context.exception), "'str' is not allowed, only integer or float")
        
    def test_convert_milliseconds_to_minutes_with_negative_value_raises_error(self):
        with self.assertRaises(ValueError) as context:
            self.time_conversion.convert_milliseconds_to_minutes(-1)

        self.assertEqual(str(context.exception), "Negative values are not allowed.")

    ###############################################################################
    # Milliseconds to Hours Test Case
    ###############################################################################
    def test_convert_milliseconds_to_hours(self):
        self.assertEqual(self.time_conversion.convert_milliseconds_to_hours(1800000), 0.5)
        self.assertEqual(self.time_conversion.convert_milliseconds_to_hours(900000), 0.25)
        self.assertEqual(self.time_conversion.convert_milliseconds_to_hours(450000), 0.125)

    def test_convert_milliseconds_to_hours_with_invalid_type_raises_error(self):
        with self.assertRaises(TypeError) as context:
            self.time_conversion.convert_milliseconds_to_hours('string')

        self.assertEqual(str(context.exception), "'str' is not allowed, only integer or float")

    def test_convert_milliseconds_to_hours_with_negative_value_raises_error(self):
        with self.assertRaises(ValueError) as context:
            self.time_conversion.convert_milliseconds_to_hours(-1)

        self.assertEqual(str(context.exception), "Negative values are not allowed.")

    ###############################################################################
    # Hours to Seconds Test Case
    ###############################################################################
    def test_convert_hours_to_seconds(self):
        self.assertEqual(self.time_conversion.convert_hours_to_seconds(3), 10800)
        self.assertEqual(self.time_conversion.convert_hours_to_seconds(0.25), 900)
        self.assertEqual(self.time_conversion.convert_hours_to_seconds(20), 72000)

    def test_convert_hours_to_seconds_with_invalid_type_raises_error(self):
        with self.assertRaises(TypeError) as context:
            self.time_conversion.convert_hours_to_seconds('string')

        self.assertEqual(str(context.exception), "'str' is not allowed, only integer or float")

    def test_convert_hours_to_seconds_with_negative_value_raises_error(self):
        with self.assertRaises(ValueError) as context:
            self.time_conversion.convert_hours_to_seconds(-1)

        self.assertEqual(str(context.exception), "Negative values are not allowed.")

    ###############################################################################
    # Hours to Milliseconds Test Case
    ###############################################################################
    def test_convert_hours_to_milliseconds(self):
        self.assertEqual(self.time_conversion.convert_hours_to_milliseconds(2), 7200000)
        self.assertEqual(self.time_conversion.convert_hours_to_milliseconds(0.5), 1800000)
        self.assertEqual(self.time_conversion.convert_hours_to_milliseconds(0.2), 720000)

    def test_convert_hours_to_milliseconds_with_invalid_type_raises_error(self):
        with self.assertRaises(TypeError) as context:
            self.time_conversion.convert_hours_to_milliseconds('string')

        self.assertEqual(str(context.exception), "'str' is not allowed, only integer or float")

    def test_convert_hours_to_milliseconds_with_negative_value_raises_error(self):
        with self.assertRaises(ValueError) as context:
            self.time_conversion.convert_hours_to_milliseconds(-1)
        
        self.assertEqual(str(context.exception), "Negative values are not allowed.")

    ###############################################################################
    # Seconds to Hours Test Case
    ###############################################################################
    def test_convert_seconds_to_hours(self):
        self.assertEqual(self.time_conversion.convert_seconds_to_hours(720), 0.2)
        self.assertEqual(self.time_conversion.convert_seconds_to_hours(360), 0.1)
        self.assertEqual(self.time_conversion.convert_seconds_to_hours(7200), 2)

    def test_convert_seconds_to_hours_with_invalid_type_raises_error(self):
        with self.assertRaises(TypeError) as context:
            self.time_conversion.convert_seconds_to_hours('string')

        self.assertEqual(str(context.exception), "'str' is not allowed, only integer or float")

    def test_convert_seconds_to_hours_with_negative_value_raises_error(self):
        with self.assertRaises(ValueError) as context:
            self.time_conversion.convert_seconds_to_hours(-1)

        self.assertEqual(str(context.exception), "Negative values are not allowed.")

    ###############################################################################
    # Minutes to Milliseconds Test Case
    ###############################################################################
    def test_convert_minutes_to_milliseconds(self):
        self.assertEqual(self.time_conversion.convert_minutes_to_milliseconds(32), 1920000)
        self.assertEqual(self.time_conversion.convert_minutes_to_milliseconds(0.5), 30000)
        self.assertEqual(self.time_conversion.convert_minutes_to_milliseconds(0.25), 15000)

    def test_convert_minutes_to_milliseconds_with_invalid_type_raises_error(self):
        with self.assertRaises(TypeError) as context:
            self.time_conversion.convert_minutes_to_milliseconds('string')

        self.assertEqual(str(context.exception), "'str' is not allowed, only integer or float")

    def test_convert_minutes_to_milliseconds_with_negative_value_raises_error(self):
        with self.assertRaises(ValueError) as context:
            self.time_conversion.convert_minutes_to_milliseconds(-1)

        self.assertEqual(str(context.exception), "Negative values are not allowed.")

if __name__ == "__main__":
    unittest.main()
    



