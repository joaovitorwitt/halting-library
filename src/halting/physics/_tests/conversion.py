
import unittest
from unittest import TestCase

from src.halting.physics.conversion import Time, Mass, Length

###########################################################################
# Time Test Case
###########################################################################
class TimeTestCase(TestCase):

    def setUp(self) -> None:
        self.time_conversion = Time()
        return super().setUp()


    def test_convert_milliseconds_to_seconds(self):
        self.assertEqual(self.time_conversion.convert_milliseconds_to_seconds(3920), 3.920)
        self.assertEqual(self.time_conversion.convert_milliseconds_to_seconds(0.298), 0.000298)
        self.assertEqual(self.time_conversion.convert_milliseconds_to_seconds(293), 0.293)


    def test_convert_seconds_to_minutes(self):
        self.assertEqual(self.time_conversion.convert_seconds_to_minutes(720), 12)
        self.assertEqual(self.time_conversion.convert_seconds_to_minutes(30), 0.5)
        self.assertEqual(self.time_conversion.convert_seconds_to_minutes(1440), 24)
        self.assertEqual(self.time_conversion.convert_seconds_to_minutes(240), 4)


    def test_convert_minutes_to_hours(self):
        self.assertEqual(self.time_conversion.convert_minutes_to_hours(39), 0.65)
        self.assertEqual(self.time_conversion.convert_minutes_to_hours(6), 0.1)
        self.assertEqual(self.time_conversion.convert_minutes_to_hours(402), 6.7)


    def test_convert_hours_to_minutes(self):
        self.assertEqual(self.time_conversion.convert_hours_to_minutes(2), 120)
        self.assertEqual(self.time_conversion.convert_hours_to_minutes(0.5), 30)
        self.assertEqual(self.time_conversion.convert_hours_to_minutes(23), 1380)


    def test_convert_minutes_to_seconds(self):
        self.assertEqual(self.time_conversion.convert_minutes_to_seconds(30), 1800)
        self.assertEqual(self.time_conversion.convert_minutes_to_seconds(98), 5880)
        self.assertEqual(self.time_conversion.convert_minutes_to_seconds(0.7), 42)


    def test_convert_seconds_to_milliseconds(self):
        self.assertEqual(self.time_conversion.convert_seconds_to_milliseconds(39), 39000)
        self.assertEqual(self.time_conversion.convert_seconds_to_milliseconds(0.098), 98)
        self.assertEqual(self.time_conversion.convert_seconds_to_milliseconds(293), 293000)


    def test_convert_milliseconds_to_minutes(self):
        self.assertEqual(self.time_conversion.convert_milliseconds_to_minutes(120000), 2)
        self.assertEqual(self.time_conversion.convert_milliseconds_to_minutes(30000), 0.5)
        self.assertEqual(self.time_conversion.convert_milliseconds_to_minutes(15000), 0.25)

        
    def test_convert_milliseconds_to_hours(self):
        self.assertEqual(self.time_conversion.convert_milliseconds_to_hours(1800000), 0.5)
        self.assertEqual(self.time_conversion.convert_milliseconds_to_hours(900000), 0.25)
        self.assertEqual(self.time_conversion.convert_milliseconds_to_hours(450000), 0.125)


    def test_convert_hours_to_seconds(self):
        self.assertEqual(self.time_conversion.convert_hours_to_seconds(3), 10800)
        self.assertEqual(self.time_conversion.convert_hours_to_seconds(0.25), 900)
        self.assertEqual(self.time_conversion.convert_hours_to_seconds(20), 72000)


    def test_convert_hours_to_milliseconds(self):
        self.assertEqual(self.time_conversion.convert_hours_to_milliseconds(2), 7200000)
        self.assertEqual(self.time_conversion.convert_hours_to_milliseconds(0.5), 1800000)
        self.assertEqual(self.time_conversion.convert_hours_to_milliseconds(0.2), 720000)


    def test_convert_seconds_to_hours(self):
        self.assertEqual(self.time_conversion.convert_seconds_to_hours(720), 0.2)
        self.assertEqual(self.time_conversion.convert_seconds_to_hours(360), 0.1)
        self.assertEqual(self.time_conversion.convert_seconds_to_hours(7200), 2)


    def test_convert_minutes_to_milliseconds(self):
        self.assertEqual(self.time_conversion.convert_minutes_to_milliseconds(32), 1920000)
        self.assertEqual(self.time_conversion.convert_minutes_to_milliseconds(0.5), 30000)
        self.assertEqual(self.time_conversion.convert_minutes_to_milliseconds(0.25), 15000)

###########################################################################
# Mass Test Case
###########################################################################
class MassTestCase(TestCase):

    def setUp(self) -> None:
        self.mass_conversion = Mass()
        return super().setUp()

    
    def test_convert_milligrams_to_grams(self):
        self.assertEqual(self.mass_conversion.convert_milligrams_to_grams(1000), 1.0)
        self.assertEqual(self.mass_conversion.convert_milligrams_to_grams(2332), 2.332)
        self.assertEqual(self.mass_conversion.convert_milligrams_to_grams(4.6), 0.0046)
        self.assertEqual(self.mass_conversion.convert_milligrams_to_grams(3.9053), 0.0039053)
        self.assertEqual(self.mass_conversion.convert_milligrams_to_grams(0), 0)


    def test_convert_grams_to_kilograms(self):
        self.assertEqual(self.mass_conversion.convert_grams_to_kilograms(0.9), 0.0009)
        self.assertEqual(self.mass_conversion.convert_grams_to_kilograms(2), 0.002)
        self.assertEqual(self.mass_conversion.convert_grams_to_kilograms(34), 0.034)
        self.assertEqual(self.mass_conversion.convert_grams_to_kilograms(286), 0.286)
        self.assertEqual(self.mass_conversion.convert_grams_to_kilograms(9736), 9.736)
        self.assertEqual(self.mass_conversion.convert_grams_to_kilograms(582902), 582.902)


    def test_convert_kilograms_to_tons(self):
        self.assertEqual(self.mass_conversion.convert_kilograms_to_tons(0.9), 0.0009)
        self.assertEqual(self.mass_conversion.convert_kilograms_to_tons(7), 0.007)
        self.assertEqual(self.mass_conversion.convert_kilograms_to_tons(85), 0.085)
        self.assertEqual(self.mass_conversion.convert_kilograms_to_tons(726), 0.726)
        self.assertEqual(self.mass_conversion.convert_kilograms_to_tons(6208), 6.208)
        self.assertEqual(self.mass_conversion.convert_kilograms_to_tons(49807), 49.807)


    def test_convert_tons_to_kilograms(self):
        self.assertEqual(self.mass_conversion.convert_tons_to_kilograms(0.000000736), 0.000736)
        self.assertEqual(self.mass_conversion.convert_tons_to_kilograms(0.009), 9)
        self.assertEqual(self.mass_conversion.convert_tons_to_kilograms(0.9827), 982.7)
        self.assertEqual(self.mass_conversion.convert_tons_to_kilograms(100), 100000)

    
    def test_convert_kilograms_to_grams(self):
        self.assertEqual(self.mass_conversion.convert_kilograms_to_grams(0.0062), 6.2)
        self.assertEqual(self.mass_conversion.convert_kilograms_to_grams(9), 9000)
        self.assertEqual(self.mass_conversion.convert_kilograms_to_grams(50), 50000)


    def test_convert_grams_to_milligrams(self):
        self.assertEqual(self.mass_conversion.convert_grams_to_milligrams(0.006), 6)
        self.assertEqual(self.mass_conversion.convert_grams_to_milligrams(0.000007262), 0.007262)
        self.assertEqual(self.mass_conversion.convert_grams_to_milligrams(674387), 674387000)


    def test_convert_milligrams_to_kilograms(self):
        self.assertEqual(self.mass_conversion.convert_milligrams_to_kilograms(15), 0.000015)
        self.assertEqual(self.mass_conversion.convert_milligrams_to_kilograms(47328303), 47.328303)
        self.assertEqual(self.mass_conversion.convert_milligrams_to_kilograms(982), 0.000982)


    def test_convert_milligrams_to_tons(self):
        self.assertEqual(self.mass_conversion.convert_milligrams_to_tons(1500000000), 1.5)
        self.assertEqual(self.mass_conversion.convert_milligrams_to_tons(15), 0.000000015)
        self.assertEqual(self.mass_conversion.convert_milligrams_to_tons(93739000000000), 93739.0)


    def test_convert_grams_to_tons(self):
        self.assertEqual(self.mass_conversion.convert_grams_to_tons(1500000), 1.5)
        self.assertEqual(self.mass_conversion.convert_grams_to_tons(15), 0.000015)
        self.assertEqual(self.mass_conversion.convert_grams_to_tons(0.72), 0.00000072)


    def test_convert_tons_to_grams(self):
        self.assertEqual(self.mass_conversion.convert_tons_to_grams(1.5), 1500000)
        self.assertEqual(self.mass_conversion.convert_tons_to_grams(0.923), 923000)
        self.assertEqual(self.mass_conversion.convert_tons_to_grams(0.000028), 28)
    

    def test_convert_tons_to_milligrams(self):
        self.assertEqual(self.mass_conversion.convert_tons_to_milligrams(1.5), 1500000000)
        self.assertEqual(self.mass_conversion.convert_tons_to_milligrams(4234), 4234000000000)
        self.assertEqual(self.mass_conversion.convert_tons_to_milligrams(0.000000009), 9)


    def test_convert_kilograms_to_milligrams(self):
        self.assertEqual(self.mass_conversion.convert_kilograms_to_milligrams(5.6), 5600000)
        self.assertEqual(self.mass_conversion.convert_kilograms_to_milligrams(0.272029), 272029)
        self.assertEqual(self.mass_conversion.convert_kilograms_to_milligrams(709287), 709287000000)


###########################################################################
# Length Test Case
###########################################################################
class LengthTestCase(TestCase):
    
    def setUp(self) -> None:
        self.length_conversion = Length()
        return super().setUp()

    
    def test_convert_millimeters_to_centimeters(self):
        self.assertEqual(self.length_conversion.convert_millimeters_to_centimeters(1), 0.1)
        self.assertEqual(self.length_conversion.convert_millimeters_to_centimeters(3827), 382.7)
        self.assertEqual(self.length_conversion.convert_millimeters_to_centimeters(0.92828), 0.092828)
        self.assertEqual(self.length_conversion.convert_millimeters_to_centimeters(829273), 82927.3)


    def test_convert_centimeters_to_meters(self):
        self.assertEqual(self.length_conversion.convert_centimeters_to_meters(0.00928), 0.0000928)
        self.assertEqual(self.length_conversion.convert_centimeters_to_meters(9280), 92.80)
        self.assertEqual(self.length_conversion.convert_centimeters_to_meters(920232000), 9202320.00)
        
            
    def test_convert_meters_to_kilometers(self):
        self.assertEqual(self.length_conversion.convert_meters_to_kilometers(372), 0.372)
        self.assertEqual(self.length_conversion.convert_meters_to_kilometers(9827), 9.827)
        self.assertEqual(self.length_conversion.convert_meters_to_kilometers(9829029), 9829.029)


    def test_convert_kilometers_to_meters(self):
        self.assertEqual(self.length_conversion.convert_kilometers_to_meters(6.5), 6500)
        self.assertEqual(self.length_conversion.convert_kilometers_to_meters(0.0876), 87.6)
        self.assertEqual(self.length_conversion.convert_kilometers_to_meters(93820), 93820000)


    def test_convert_meters_to_centimeters(self):
        self.assertEqual(self.length_conversion.convert_meters_to_centimeters(10), 1000)
        self.assertEqual(self.length_conversion.convert_meters_to_centimeters(208320832), 20832083200)
        self.assertEqual(self.length_conversion.convert_meters_to_centimeters(0.89082), 89.082)


    def test_convert_centimeters_to_millimeters(self):
        self.assertEqual(self.length_conversion.convert_centimeters_to_millimeters(0.0289), 0.289)
        self.assertEqual(self.length_conversion.convert_centimeters_to_millimeters(9202), 92020)
        self.assertEqual(self.length_conversion.convert_centimeters_to_millimeters(8272.9092), 82729.092)


    def test_convert_millimeters_to_meters(self):
        self.assertEqual(self.length_conversion.convert_millimeters_to_meters(49), 0.049)
        self.assertEqual(self.length_conversion.convert_millimeters_to_meters(872), 0.872)
        self.assertEqual(self.length_conversion.convert_millimeters_to_meters(0.292), 0.000292)
        self.assertEqual(self.length_conversion.convert_millimeters_to_meters(29827), 29.827)


    def test_convert_millimeters_to_kilometers(self):
        self.assertEqual(self.length_conversion.convert_millimeters_to_kilometers(1), 0.000001)
        self.assertEqual(self.length_conversion.convert_millimeters_to_kilometers(1292083), 1.292083)
        self.assertEqual(self.length_conversion.convert_millimeters_to_kilometers(0.00928), 0.00000000928)
        self.assertEqual(self.length_conversion.convert_millimeters_to_kilometers(182), 0.000182)


    def test_convert_kilometers_to_centimeters(self):
        self.assertEqual(self.length_conversion.convert_kilometers_to_centimeters(9), 900000)
        self.assertEqual(self.length_conversion.convert_kilometers_to_centimeters(0.21), 21000)
        self.assertEqual(self.length_conversion.convert_kilometers_to_centimeters(2920), 292000000)
        self.assertEqual(self.length_conversion.convert_kilometers_to_centimeters(7), 700000)


    def test_convert_kilometers_to_millimeters(self):
        self.assertEqual(self.length_conversion.convert_kilometers_to_millimeters(9), 9000000)
        self.assertEqual(self.length_conversion.convert_kilometers_to_millimeters(0.000008), 8)
        self.assertEqual(self.length_conversion.convert_kilometers_to_millimeters(290.87), 290870000)


    def test_convert_meters_to_millimeters(self):
        self.assertEqual(self.length_conversion.convert_meters_to_millimeters(0.003), 3)
        self.assertEqual(self.length_conversion.convert_meters_to_millimeters(34), 34000)
        self.assertEqual(self.length_conversion.convert_meters_to_millimeters(9.28), 9280)

        
    def test_convert_centimeters_to_kilometers(self):
        self.assertEqual(self.length_conversion.convert_centimeters_to_kilometers(340), 0.00340)
        self.assertEqual(self.length_conversion.convert_centimeters_to_kilometers(29834), 0.29834)
        self.assertEqual(self.length_conversion.convert_centimeters_to_kilometers(0.098), 0.00000098)


if __name__ == "__main__":
    unittest.main()
