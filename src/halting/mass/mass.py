###############################################################################
# Imports
###############################################################################
from src.halting.base import BaseHalting

###############################################################################
# Mass Conversion Class Implementation
###############################################################################
class MassConversion(BaseHalting):

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
    