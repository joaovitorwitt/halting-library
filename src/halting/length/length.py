###############################################################################
# Imports
###############################################################################


###############################################################################
# Length Conversion Class Implementation
###############################################################################
class LengthConversion(object):

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
        if not isinstance(millimeters, (int, float)):
            raise TypeError(f"'{type(millimeters).__name__}' is not allowed, only integer or float")
        
        if millimeters < 0:
            raise ValueError("Negative values are not allowed.")
        
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
        if not isinstance(centimeters, (int, float)):
            raise TypeError(f"'{type(centimeters).__name__}' is not allowed, only integer or float")

        if centimeters < 0:
            raise ValueError("Negative values are not allowed.")
        
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
        if not isinstance(meters, (int, float)):
            raise TypeError(f"'{type(meters).__name__}' is not allowed, only integer or float")
        
        if meters < 0:
            raise ValueError("Negative values are not allowed.")
        
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
        if not isinstance(kilometers, (int, float)):
            raise TypeError(f"'{type(kilometers).__name__}' is not allowed, only integer or float")
        
        if kilometers < 0:
            raise ValueError("Negative values are not allowed.")
        
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
        if not isinstance(meters, (int, float)):
            raise TypeError(f"'{type(meters).__name__}' is not allowed, only integer or float")
        
        if meters < 0:
            raise ValueError("Negative values are not allowed.")
        
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
        if not isinstance(centimeters, (int, float)):
            raise TypeError(f"'{type(centimeters).__name__}' is not allowed, only integer or float")
        
        if centimeters < 0:
            raise ValueError("Negative values are not allowed.")
        
        millimeters = centimeters * 10
        return millimeters

