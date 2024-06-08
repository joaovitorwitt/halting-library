


class MassConversion(object):

    def convert_mg_to_g(self, mg: int | float) -> int | float:
        """
        Converts milligrams to grams.

        This function converts milligrams to grams by dividing the value by 1000.

        Args:
            mg (int | float): The value of milligrams to be converted.
        
        Returns:
            int | float: The converted value as grams

        Usage:
            >>> from halting.mass.mass import MassConversion
            >>> mass_conversion = MassConversion()
            >>> mass_conversion.convert_mg_to_g(1000)
            1
        """
        return mg / 1000
    
    def convert_g_to_kg(self, g: int | float) -> int | float:
        """
        Converts grams to kilograms

        This function takes a value of grams and converted it to kilograms
        the standard SI unit, by dividing the value by 1000.

        Args:

        Returns:

        Usage:
            >>> from halting.mass.mass import MassConversion
        """
        return g / 1000
    
    def convert_kg_to_ton(self, kg: int | float) -> int | float:
        """
        divide the mass value by 1000
        """
        return kg / 1000

    def convert_ton_to_kg(self, ton: int | float) -> int | float:
        """
        multiply the mass value by 1000
        """
        return ton * 1000
    
    def convert_kg_to_g(self, kg: int | float) -> int | float:
        """
        multiply the mass value by 1000
        """
        return kg * 1000
    
    def convert_g_to_mg(self, g: int | float) -> int | float:
        """
        multiply the value by 1000
        """
        return g * 1000
