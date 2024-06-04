


class MassConversion(object):

    def convert_mg_to_g(self, mg: int | float) -> int | float:
        """
        divide the value by 1000 (or multiply by 0.001)
        """
        return mg / 1000
     
    def convert_g_to_kg(self, g: int | float) -> int | float:
        """
        divide the value by 1000
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
