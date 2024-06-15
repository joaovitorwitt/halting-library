###############################################################################
# Imports
###############################################################################


###############################################################################
# Mass Conversion Class Implementation
###############################################################################
class MassConversion(object):

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
        try:
            if milligrams < 0:
                raise ValueError("Negative values are not allowed.")
            
            grams = milligrams / 1000
            return grams
        
        except TypeError:
            return f"Error: '{type(milligrams).__name__}' is not allowed, only integer or float values."
        
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
        try:
            if grams < 0:
                raise ValueError("Negative values are not allowed.")

            kilogramas = grams / 1000
            return kilogramas

        except TypeError:
            return f"Error: '{type(grams).__name__}' is not allowed, only integer or float values."
            
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
        try:
            if kilograms < 0:
                raise ValueError("Negative values are not allowed.")
            
            tons = kilograms / 1000
            return tons

        except TypeError:
            return f"Error: '{type(kilograms).__name__}' is not allowed, only integer or float values."

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
        try:
            if tons < 0:
                raise ValueError("Negative values are not allowed.")
            kilograms = tons * 1000
            return kilograms
        
        except TypeError:
            return f"Error: '{type(tons).__name__}' is not allowed, only integer or float values."
    
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
        try:
            if kilograms < 0:
                raise ValueError("Negative values are not allowed.")
            
            grams = kilograms * 1000
            return grams
    
        except TypeError:
            return f"Error: '{type(kilograms).__name__}' is not allowed, only integer or float values."

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
        try:
            if grams < 0:
                raise ValueError("Negative values are not allowed.")

            milligrams = grams * 1000    
            return milligrams
        
        except TypeError:
            return f"Error: '{type(grams).__name__}' is not allowed, only integer or float values."
