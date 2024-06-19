##################################################
# Imports
##################################################
from math import pi
from src.halting.base import BaseHalting

##################################################
# Formulas Class Implementation
##################################################
class GeneralFormulas(BaseHalting):

    def calculate_volume_of_a_cylinder(self, height: int | float, base_radius: int | float) -> int | float:
        """
        Calculates the volume of a cylinder.

        Args:
            height (int | float): The actual height of the cylinder
            base_radius (int | float): The base radius of the cyclinder

        Returns:
            int | float: The final volume of the cylinder.

        Example:
            >>> from src.halting.formulas.formulas import GeneralFormulas
            >>> GeneralFormulas().calculate_volume_of_a_cylinder(2, 2)
            25.12 (with pi as 3.14)
        """
        return height*pi*(pow(base_radius, 2))
    
    def calculate_volume_of_a_sphere(self, radius: int | float) -> int | float:
        """
        Calculate the volume of a sphere.

        Args:
            radius(int, float): The radius of the sphere

        Returns:
            int | float: The calculated volume of a sphere.

        Example:
            >>> from src.halting.formulas.formulas import GeneralFormulas
            >>> GeneralFormulas().calculate_volume_of_a_cylinder(3)
            113.04
        """
        return (4*pi*(pow(radius, 3))) / 3
    
    def calculate_volume_of_a_cube(self, edge_length: int | float) -> int | float:
        """
        Calculate the valume of a cube.
        
        Args:
            edge_length (int, float): The edge length of the cube.
        
        Returns:
            int | float: The final calculated volume of the cube.
        
        Example:
            >>> from src.halting.formulas.formulas import GeneralFormulas
            >>> GeneralFormulas().calculate_volume_of_a_cube(3)
            27
        """
        return pow(edge_length, 3)

    def calculate_volume_of_a_cone(self, base_radius: int | float, height: int | float) -> int | float:
        pass

    def calculate_volume_of_a_rectangle(self, length: int | float, height: int | float, width: int | float) -> int | float:
        pass



# AREA CALCULATOR - https://www.calculator.net/area-calculator.html
# VOLUEM CALCULATOR - https://www.calculator.net/volume-calculator.html