##################################################
# Imports
##################################################
from math import pi

##################################################
# Formulas Class Implementation
##################################################
class GeneralFormulas(object):

    def calculate_volume_of_a_cylinder(self, height: int | float, radius: int | float) -> int | float:
        """
        This function is used to calcute the volume of a cylinder

        Args:
            height: the specified height of the cylinder
            raidus: the radius of the cylinder 

        Returns:
            the result of applying the calculations
        """
        return height*pi*(pow(radius, 2))
    
    
    def calculate_volume_of_a_sphere(self, radius: int | float) -> int | float:
        """
        This function is used to calculate the volume of a sphere

        Args:
            radius: the radius of the sphere

        Returns:
            the result of applying the formula

        """
        return (4*pi*(pow(radius, 3))) / 3
    
    def calculate_volume_of_a_square(self, edge_length: int | float) -> int | float:
        """
        __description__
        
        Args:
            __input__ (__type__):
        
        Returns:
            __type__
        
        Example:
            >>> 
        """

    def calculate_volume_of_a_cone(self, base_radius: int | float, height: int | float) -> int | float:
        pass

    def calculate_volume_of_a_rectangle(self, length: int | float, height: int | float, width: int | float) -> int | float:
        pass



# AREA CALCULATOR - https://www.calculator.net/area-calculator.html
# VOLUEM CALCULATOR - https://www.calculator.net/volume-calculator.html