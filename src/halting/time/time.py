###############################################################################
# Imports
###############################################################################
from src.halting.base import BaseHalting

###############################################################################
# Time Conversion Class Implementation
###############################################################################
class TimeConversion(BaseHalting):

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
