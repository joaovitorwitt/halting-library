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
        """
        Calculate the volume of a cone

        Args:
            base_radius (int | float): The radius of the base of the cone.
            height (int | float): The height of the cone

        Returns:
            int | float: The calculated volume of the cone.

        Example:
            >>> from src.halting.formulas.formulas import GeneralFormulas()
            >>> general_formulas = GeneralFormulas()
            >>> general_formulas.calculate_volume_of_a_cone(2, 2)
            8.38
        """
        cone_formula = (pi * pow(base_radius, 2) * height) / 3
        return cone_formula

    def calculate_volume_of_a_rectangle(self, length: int | float, height: int | float, width: int | float) -> int | float:
        """
        Calculate the volume of a rectangle

        Args:
            length (int | float): The length of the rectangle
            height (int | float): The height of the rectangle
            width (int | float): The width of the rectangle

        Returns:
            int | float: The final calculated volume for the rectangle.

        Example:
            >>> from src.halting.formulas.formulas import GeneralFormulas()
            >>> general_formulas = GeneralFormulas()
            >>> general_formulas.calculate_volume_of_a_rectangle(2, 2, 2)
            8
        """
        rectangle_formula = length * height * width
        return rectangle_formula

    def calculate_spherical_cap_volume(self, base_radius: int | float, height: int | float, ball_radius: int | float) -> int | float:
        """
        Function calculates the volume of a spherical cap

        Args:
            base_radius (int | float): Base radius of the cap
            ball_radius (int | float): Radius of the ball
            height (int | float): Height from the base until the the top.

        Returns:
            int | float: The calculated volume for the spherical cap.

        Example:
            >>> from src.halting.formulas.formulas import GeneralFormulas()
            >>> general_formulas = GeneralFormulas()
            >>> general_formulas.calculate_spherical_cap_volume(2, 2, 2)
            16.75516
        """
        spherical_cap = (pi / 3) * pow(height, 2) * (3*ball_radius - height)
        return spherical_cap

    def calculate_volume_of_a_capsule(self, base_radius: int | float, height: int | float):
        """
        Calculates the volume of a capsule.

        Args:
            base_radius (int | float): The radius of the capsule.
            height (int | float): The total height of the capsule.

        Returns:    
            >>> from src.halting.formulas.formulas import GeneralFormulas
            >>> general_formulas = GeneralFormulas()
            >>> general_formulas.calculate_volume_of_a_capsule(2, 2)
            58.64
        """

    def calculate_conical_frustum_volume(self, top_radius: int | float, bottom_radius: int | float, height: int | float) -> int | float:
        pass


    

# AREA CALCULATOR - https://www.calculator.net/area-calculator.html
# VOLUEM CALCULATOR - https://www.calculator.net/volume-calculator.html
# ALGEBRA SECTION - https://www.calculatorsoup.com/calculators/algebra/