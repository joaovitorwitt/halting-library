###########################################################################
# Imports
###########################################################################
from src.halting.base import BaseHalting

###########################################################################
# Implementation
###########################################################################
class Time(BaseHalting):
    def convert_milliseconds_to_seconds(self, milliseconds: int | float) -> int | float:
        """
        Convert a value represented in milliseconds to seconds by dividing by 1000.
        
        Args:
            milliseconds (int, float): The value in milliseconds to be converted to seconds.
        
        Returns:
            int, float: The converted value now represented in seconds.
        
        Example:
            >>> from src.halting.time.time import TimeConversion
            >>> time_conversion = TimeConversion()
            >>> time_conversion.convert_milliseconds_to_seconds(2928)
            2.928
        """
        self.validate(milliseconds)
        
        seconds = milliseconds / 1000
        return seconds

    def convert_seconds_to_minutes(self, seconds: int | float) -> int | float:
        """
        Convert a value in seconds to a value in minutes by dividing the value by 60.
        
        Args:
            seconds (int, float): The value in seconds to be converted to minutes
        
        Returns:
            int | float: The converted value now represented in minutes.
        
        Example:
            >>> from src.halting.time.time import TimeConversion
            >>> time_conversion = TimeConversion()
            >>> time_conversion.convert_seconds_to_minutes(360)
            6
        """
        self.validate(seconds)
        
        minutes = seconds / 60
        return minutes

    def convert_minutes_to_hours(self, minutes: int | float) -> int | float:
        """
        Convert a value represented in minutes to hours by dividing the value by 60.
        
        Args:
            minutes (int, float): The value in minutes to be converted.
        
        Returns:
            int | float: The converted value now in hours.
        
        Example:
            >>> from src.halting.time.time import TimeConversion
            >>> time_conversion = TimeConversion()
            >>> time_conversion.convert_minutes_to_hours(30)
            0.5
        """
        self.validate(minutes)
        
        hours = minutes / 60
        return hours

    def convert_hours_to_minutes(self, hours: int | float) -> int | float:
        """
        Convert a value from hours to minutes by multiplying the value by 60.
        
        Args:
            hours (int, float): The value to be converted to minutes.
        
        Returns:
            int | float: The converted value now represented in minutes
        
        Example:
            >>> from src.halting.time.time import TimeConversion
            >>> time_conversion = TimeConversion()
            >>> time_conversion.convert_hours_to_minutes(2)
            120
        """
        self.validate(hours)
        
        minutes = hours * 60
        return minutes

    def convert_minutes_to_seconds(self, minutes: int | float) -> int | float:
        """
        Convert a value from minutes to hours by multiplying the value by 60.
        
        Args:
            minutes (int, float): The value to be converted to seconds.
        
        Returns:
            int | float: The converted value now represented in seconds
        
        Example:
            >>> from src.halting.time.time import TimeConversion
            >>> time_conversion = TimeConversion()
            >>> time_conversion.convert_minutes_to_seconds(2)
            120
        """
        self.validate(minutes)
        
        seconds = minutes * 60
        return seconds

    def convert_seconds_to_milliseconds(self, seconds: int | float) -> int | float:
        """
        This function converts seconds to milliseconds by multiplying the seconds by 1000.
        
        Args:
            seconds (int, float): The value in seconds to be converted.
        
        Returns:
            int | float: The converted value now represented in milliseconds
        
        Example:
            >>> from src.halting.time.time import TimeConversion
            >>> time_conversion = TimeConversion()
            >>> time_conversion.convert_seconds_to_milliseconds(3)
            3000
        """
        self.validate(seconds)
        
        milliseconds = seconds * 1000
        return milliseconds

    def convert_milliseconds_to_minutes(self, milliseconds: int | float) -> int | float:
        """
        This function converts a value from milliseconds to minutes by dividing by 60000.
        
        Args:
            milliseconds (int, float): The value to be converted to minutes.
        
        Returns:
            int | float: The converted value now represented in minutes.
        
        Example:
            >>> from src.halting.time.time import TimeConversion
            >>> time_conversion = TimeConversion()
            >>> time_conversion.convert_milliseconds_to_minutes(60000)
            1
        """
        self.validate(milliseconds)
        
        minutes = milliseconds / 60000
        return minutes

    def convert_milliseconds_to_hours(self, milliseconds: int | float) -> int | float:
        """
        This function converts a value from milliseconds to hours by dividing the value by 3600000.
        
        Args:
            milliseconds (int, float): The value to be converted to hours.
        
        Returns:
            int | float: The converted value now represented in hours
        
        Example:
            >>> from src.halting.time.time import TimeConversion
            >>> time_conversion = TimeConversion()
            >>> time_conversion.convert_milliseconds_to_hours(1800000)
            0.5
        """
        self.validate(milliseconds)
        
        hours = milliseconds / 3600000
        return hours

    def convert_hours_to_seconds(self, hours: int | float) -> int | float:
        """
        This function converts a value from in hours to a value in seconds by multiplying by 3600.
        
        Args:
            hours (int, float): The value in hours to be converted.
        
        Returns:
            int | float: The converted value now represented in seconds.
        
        Example:
            >>> from src.halting.time.time import TimeConversion
            >>> time_conversion = TimeConversion()
            >>> time_conversion.convert_hours_to_seconds(4)
            14440
        """
        self.validate(hours)
        
        seconds = hours * 3600
        return seconds

    def convert_hours_to_milliseconds(self, hours: int | float) -> int | float:
        """
        This function converts a value from hours to milliseconds by multiplying the value by 3600000
        
        Args:
            hours (int, float): The value in hours to be converted.
        
        Returns:
            int | float: The converted value now represented in milliseconds
        
        Example:
            >>> from src.halting.time.time import TimeConversion
            >>> time_conversion = TimeConversion()
            >>> time_conversion.convert_hours_to_milliseconds(4)
            14400000

        """
        self.validate(hours)
        
        milliseconds = hours * 3600000
        return milliseconds

    def convert_seconds_to_hours(self, seconds: int | float) -> int | float:
        """
        This function converts the value from seconds to hours by dividing the value by 3600
        
        Args:
            seconds (int, float): The value in seconds to be converted.
        
        Returns:
            int | float: The converted value now represented in hours
        
        Example:
            >>> from src.halting.time.time import TimeConversion
            >>> time_conversion = TimeConversion()
            >>> time_conversion.convert_seconds_to_hours(7200)
            2
        """
        self.validate(seconds)
        
        hours = seconds / 3600
        return hours

    def convert_minutes_to_milliseconds(self, minutes: int | float) -> int | float:
        """
        This function converts a value from minutes to milliseconds by multiplying by 600000
        
        Args:
            minutes (int, float): The value in minutes to be converted.
        
        Returns:
            int | float: The converted value now represented in milliseconds
        
        Example:
            >>> from src.halting.time.time import TimeConversion
            >>> time_conversion = TimeConversion()
            >>> time_conversion.convert_minutes_to_milliseconds(32)
            1920000
        """
        self.validate(minutes)
        
        milliseconds = minutes * 60000
        return milliseconds


class Mass(BaseHalting):
    def convert_milligrams_to_grams(self, milligrams: int | float) -> int | float:
        """
        Converts milligrams to grams.
        This function converts milligrams to grams by dividing the value by 1000.

        Args:
            milligrams (int | float): The value of milligrams to be converted.
        
        Returns:
            int | float: The converted value as grams

        Example:
            >>> from halting.mass.mass import MassConversion
            >>> mass_conversion = MassConversion()
            >>> mass_conversion.convert_mg_to_g(1000)
            1
        """
        self.validate(milligrams)

        grams = milligrams / 1000
        return grams

    def convert_grams_to_kilograms(self, grams: int | float) -> int | float:
        """
        Converts grams to kilograms

        This function takes a value of grams and converted it to kilograms
        the standard SI unit, by dividing the value by 1000.

        Args:
            grams (int | float): The value of grams to be converted.
        
        Returns:
            int | float: The value converted to kilograms.

        Example:
            >>> from src.halting.mass.mass import MassConversion
            >>> mass_conversion = MassConversion()
            >>> mass_conversion.convert_grams_to_kilograms(10000)
            10
        """
        self.validate(grams)

        kilogramas = grams / 1000
        return kilogramas

    def convert_kilograms_to_tons(self, kilograms: int | float) -> int | float:
        """
        Convert kilogram value to tons.
        
        Args:
            kilgorams (int | float): The value of kilograms to be converted.
        
        Returns:
            int | float: The converted value.
        
        Example:
            >>> from src.halting.mass.mass import MassConversion
            >>> mass_conversion = MassConversion()
            >>> mass_conversion.convert_kilograms_to_tons(10000)
            10
        """
        self.validate(kilograms)
        
        tons = kilograms / 1000
        return tons

    def convert_tons_to_kilograms(self, tons: int | float) -> int | float:
        """
        Converts tons to kilograms by multiplying the ton value by 1000.
        
        Args:
            tons (int | float): The value to be converted to kilograms.
        
        Returns:
            int | float: The converted value.
        
        Example:
            >>> from src.halting.mass.mass import MassConversion
            >>> mass_conversion = MassConversion()
            >>> mass_conversion.convert_tons_to_kilograms(1)
            1000
        """
        self.validate(tons)

        kilograms = tons * 1000
        return kilograms
    
    def convert_kilograms_to_grams(self, kilograms: int | float) -> int | float:
        """
        Convert a value of kilograms to grams by multiplying by 1000.
        
        Args:
            kilograms (int | float): The value of kilograms to be converted.
        
        Returns:
            int | float: The converted value.
        
        Example:
            >>> from src.halting.mass.mass import MassConversion
            >>> mass_conversion = MassConversion()
            >>> mass_conversion.convert_kilograms_to_grams(1)
            1000
        """
        self.validate(kilograms)
     
        grams = kilograms * 1000
        return grams
    
    def convert_grams_to_milligrams(self, grams: int | float) -> int | float:
        """
        Convert grams to milligrams.
        
        Args:
            grams (int | float): The value of grams to be converted to milligrams.
        
        Returns:
            int | float: The converted value.
        
        Example:
            >>> from src.halting.mass.mass import MassConversion
            >>> mass_conversion = MassConversion()
            >>> mass_conversion.convert_grams_to_milligrams(1)
            1000
        """
        self.validate(grams)

        milligrams = grams * 1000    
        return milligrams
        
    def convert_milligrams_to_kilograms(self, milligrams: int | float) -> int | float:
        """
        Converts milligrams to the respective value in kilograms by dividing by 1000000 
        
        Args:
            milligrams (int | float): THe value in milligrams to be converted.
        
        Returns:
            int | float: The converted value to kilograms.
        
        Example:
            >>> from src.halting.mass.mass import MassConversion
            >>> mass_conversion = MassConversion()
            >>> mass_conversion.convert_milligrams_to_kilograms(1500)
            0.0015
        """
        self.validate(milligrams)
        
        kilograms = milligrams / 1000000
        return kilograms

    def convert_milligrams_to_tons(self, milligrams: int | float) -> int | float:
        """
        Convert milligrams to tons by dividing the value by 1000000000
        
        Args:
            milligrams (int, float): The value in milligrams to be converted.
        
        Returns:
            int | float: The converted value.
        
        Example:
            >>>  from src.halting.mass.mass import MassConversion
            >>> mass_conversion = MassConversion()
            >>> mass_conversion.convert_milligrams_to_tons(1500000000)
            1.5
        """
        self.validate(milligrams)
        
        tons = milligrams / 1000000000
        return tons

    def convert_grams_to_tons(self, grams: int | float) -> int | float:
        """
        Convert a value in grams to the respective value in tons 
        
        Args:
            grams (int, float): The value in grams to be converted to tons.
        
        Returns:
            int | float: The converted value in tons.
        
        Example:
            >>> from src.halting.mass.mass import MassConversion
            >>> mass_conversion = MassConversion()
            >>> mass_conversion.convert_grams_to_tons(1500000)
            1.5
        """
        self.validate(grams)
        
        tons = grams / 1000000
        return tons
    
    def convert_tons_to_grams(self, tons: int | float) -> int | float:
        """
        Convert tons to grams by multiplying by 1000000
        
        Args:
            tons (int, float): The value in tons to be converted to grams.
        
        Returns:
            int | float: The converted value to grams.
        
        Example:
            >>> from src.halting.mass.mass import MassConversion
            >>> mass_conversion = MassConversion()
            >>> mass_conversion.convert_tons_to_grams(1.5)
            1500000
        """
        self.validate(tons)
        
        grams = tons * 1000000
        return grams

    def convert_tons_to_milligrams(self, tons: int | float) -> int | float:
        """
        Convert tons to milligrams
        
        Args:
            tons (int, float): The value to be converted to milligrams
        
        Returns:
            int | float: The converted value in milligrams
        
        Example:
            >>> from src.halting.mass.mass import MassConversion
            >>> mass_conversion = MassConversion()
            >>> mass_conversion.convert_tons_to_milligrams(1.5)
            1500000000
        """
        self.validate(tons)

        milligrams = tons * 1000000000
        return milligrams

    def convert_kilograms_to_milligrams(self, kilograms: int | float) -> int | float:
        """
        Convert kilograms into milligrams
        
        Args:
            kilograms (int, float): The value in kilogrmas to be converted to milligrams.
        
        Returns:
            int | float: The value converted to milligrams.
        
        Example:
            >>> from src.halting.mass.mass import MassConversion
            >>> mass_conversion = MassConversion()
            >>> mass_conversion.convert_kilograms_to_milligrams(1.5)
            1500000
        """
        self.validate(kilograms)
        
        milligrams = kilograms * 1000000
        return milligrams
    

class Length(BaseHalting):
    def convert_millimeters_to_centimeters(self, millimeters: int | float) -> int | float:
        """
        Convert a length value from milliters to centimeters by dividing by 10.
        
        Args:
            millimeters (int, float): The value in millimeters to be converted.
        
        Returns:
            int | float: The converted value in centimeters.
        
        Example:
            >>> from src.halting.length.length import LengthConversion
            >>> length_conversion = LengthConversion()
            >>> length_conversion.convert_millimeters_to_centimeters(100)
            10
        """
        self.validate(millimeters)
        
        centimeters = millimeters / 10
        return centimeters
    
    def convert_centimeters_to_meters(self, centimeters: int | float) -> int | float:
        """
        Convert a value that's in centimeters to meters by dividing by 100.
        
        Args:
            centimeters (int, float): The value in centimeters to be converted.
        
        Returns:
            int | float: The converted value.
        
        Example:
            >>> from src.halting.length.length import LengthConversion
            >>> length_conversion = LengthConversion()
            >>> length_conversion.convert_centimeters_to_meters(1000)
            10
        """
        self.validate(centimeters)
        
        meters = centimeters / 100
        return meters
    
    def convert_meters_to_kilometers(self, meters: int | float) -> int | float:
        """
        Convert meters to kilometers by divinding the value by 1000
        
        Args:
            meters (int, float): The value in meters to be converted.
        
        Returns:
            int | float: The converted value to kilometers
        
        Example:
            >>> from src.halting.length.length import LengthConversion
            >>> length_conversion = LengthConversion()
            >>> length_conversion.convert_meters_to_kilometers(500)
            >>> 0.5
        """
        self.validate(meters)
        
        kilometers = meters / 1000
        return kilometers
    
    def convert_kilometers_to_meters(self, kilometers: int | float) -> int | float:
        """
        Convert kilometers unit to meters by multiplying by 1000
        
        Args:
            kilometers (int, float): The value in km to be converted to meters.
        
        Returns:
            int | float: The converted value in meters unit.
        
        Example:
            >>> from src.halting.length.length import LengthConversion
            >>> length_conversion = LengthConversion()
            >>> length_conversion.convert_kilometers_to_meters(29)
            29000
        """
        self.validate(kilometers)
        
        meters = kilometers * 1000
        return meters
    
    def convert_meters_to_centimeters(self, meters: int | float) -> int | float:
        """
        Convert meters to centimeters by multiplying the value of meters by 100
        
        Args:
            meters (int, float): The value in meters to be converted to centimeters.
        
        Returns:
            int | float: The converted value in centimeters unit.
        
        Example:
            >>> from src.halting.length.length import LengthConversion
            >>> length_conversion = LengthConversion()
            >>> length_conversion.convert_meters_to_centimeters(59)
            5900
        """
        self.validate(meters)
        
        centimeters = meters * 100
        return centimeters
            
    def convert_centimeters_to_millimeters(self, centimeters: int | float) -> int | float:
        """
        Convert a value from centimeters to millimeters by multiplying the value by 10
        
        Args:
            centimeters (int, float): The value in centimeters to be converted to millimeters.
        
        Returns:
            int | float: The converted value in millimeters units.
        
        Example:
            >>> from src.halting.length.length import LengthConversion
            >>> length_conversion = LengthConversion()
            >>> length_conversion.convert_centimeters_to_millimeters(894)
            8940
        """
        self.validate(centimeters)
        
        millimeters = centimeters * 10
        return millimeters

    def convert_millimeters_to_meters(self, millimeters: int | float) -> int | float:
        """
        Converts a value from millimeters to meters by dividing by 1000
        
        Args:
            millimeters (int, float): The value to be converted to meters
        
        Returns:
            int | float: The converted value represented in meters unit.
        
        Example:
            >>> from src.halting.length.length import LengthConversion
            >>> length_conversion = LengthConversion()
            >>> length_conversion.convert_millimeters_to_meters(4)
            0.004
        """
        self.validate(millimeters)
        
        meters = millimeters / 1000
        return meters
    
    def convert_millimeters_to_kilometers(self, millimeters: int | float) -> int | float:
        """
        Converts a value that's is millimeters to kilometers by dividing the value by 1000000.
        
        Args:
            millimeters (int, float): The value in millimeters to be converted.
        
        Returns:
            int | float: The converted value to kilometers.
        
        Example:
            >>> from src.halting.length.length import LengthConversion
            >>> length_conversion = LengthConversion()
            >>> length_conversion.convert_millimeters_to_kilometers(129)
            0.000129 
        """
        self.validate(millimeters)
        
        kilometers = millimeters / 1000000
        return kilometers
    
    def convert_kilometers_to_centimeters(self, kilometers: int | float) -> int | float:
        """
        Convert a value from kilometers to centimeters by multiplying the value by 100000
        
        Args:
            kilometers (int, float): The value to be converted to centimeters
        
        Returns:
            int | float: The converted value now represented in centimeters.
        
        Example:
            >>> from src.halting.length.length import LengthConversion
            >>> length_conversion = LengthConversion()
            >>> length_conversion.convert_kilometers_to_centimeters(3.4)
            340000
        """
        self.validate(kilometers)
        
        centimeters = kilometers * 100000
        return centimeters
    
    def convert_kilometers_to_millimeters(self, kilometers: int | float) -> int | float:
        """
        Convert a value from kilometers to millimeters by dividing the value by 1000000
        
        Args:
            kilometers (int, float): The value in kilometers to be converted.
        
        Returns:
            int | float: The converted value represented in millimeters.
        
        Example:
            >>> from src.halting.length.length import LengthConversion
            >>> length_conversion = LengthConversion()
            >>> length_conversion.convert_kilometers_to_millimeters(4)
            4000000
        """
        self.validate(kilometers)
        
        millimeters = kilometers * 1000000
        return millimeters
    
    def convert_meters_to_millimeters(self, meters: int | float) -> int | float:
        """
        Converts a value represented from meters to millimeters by multiplying by 1000.
        
        Args:
            meters (int, float): The value in meters to be converted.
        
        Returns:
            int | float: The converted value to millimeters.
        
        Example:
            >>> from src.halting.length.length import LengthConversion
            >>> length_conversion = LengthConversion()
            >>> length_conversion.convert_meters_to_millimeters(4)
            4000
        """
        self.validate(meters)
        
        millimeters = meters * 1000
        return millimeters
    
    def convert_centimeters_to_kilometers(self, centimeters: int | float) -> int | float:
        """
        Convert a value represented in centimeters to kilometers by dividing the value by 100000.
        
        Args:
            centimeters (int, float): The value to be converted to kilometers.
        
        Returns:
            int | float: The converted value now represented in kilometers.
        
        Example:
            >>> from src.halting.length.length import LengthConversion
            >>> length_conversion = LengthConversion()
            >>> length_conversion.convert_centimeters_to_kilometers(340)
            0.00340
        """
        self.validate(centimeters)
        
        kilometers = centimeters / 100000
        return kilometers
