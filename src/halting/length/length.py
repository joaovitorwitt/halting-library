###############################################################################
# Imports
###############################################################################
from src.halting.base import BaseHalting

###############################################################################
# Length Conversion Class Implementation
###############################################################################
class LengthConversion(BaseHalting):

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
    