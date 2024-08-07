##################################################
# Imports
##################################################
from src.halting import settings

from src.halting.base import BaseHalting

##################################################
# Implementation
##################################################
class Volume(BaseHalting):
    """
    This class is used to calculate the volume of different polygons.
    """
    def get_cylinder_volume(self, height: int | float, base_radius: int | float, rounding_factor: int = 2) -> int | float:
        """
        Calculates the volume of a cylinder.

        Args:
            height (int | float): The actual height of the cylinder
            base_radius (int | float): The base radius of the cyclinder
            rounding_factor (int, optional): The number of decimal places the result should have. Default is 2.

        Returns:
            int | float: The final volume of the cylinder.

        Example:
            >>> get_cylinder_volume(height=2, base_radius=2)
            25.12

            >>> get_cylinder_volume(height=2, base_radius=2, rounding_factor=4)
            25.1327
        """
        # TODO: Implement the key value validation
        self.validate_instance((int, float), height)
        self.validate_instance((int, float), base_radius)
        self.validate_instance(int, rounding_factor)

        cylinder = height * settings.PI * (pow(base_radius, 2))
        return round(cylinder, rounding_factor)
    
    
    def get_sphere_volume(self, radius: int | float, rounding_factor: int = 2) -> int | float:
        """
        Calculate the volume of a sphere.

        Args:
            radius(int, float): The radius of the sphere
            rounding_factor (int, optional): The number of decimal places in the final result. Default is 2
            
        Returns:
            int | float: The calculated volume of a sphere.

        Example:
            >>> calculate_volume_of_a_cylinder(3)
            113.04
        """
        self.validate_instance((int, float), radius)

        sphere = (4 * settings.PI * (pow(radius, 3))) / 3
        return round(sphere, rounding_factor)
    
    
    def get_cube_volume(self, edge_length: int | float, rounding_factor: int = 2) -> int | float:
        """
        Calculate the volume of a cube.
        
        Args:
            edge_length (int, float): The edge length of the cube.
            rounding_factor (int, optional): The number of decimal places the result should have. Default is 2.
        
        Returns:
            int | float: The final calculated volume of the cube.
        
        Example:
            >>> calculate_volume_of_a_cube(3)
            27
        """
        self.validate(edge_length)

        cube = pow(edge_length, 3)
        return round(cube, rounding_factor)


    def get_cone_volume(self, base_radius: int | float, height: int | float, rounding_factor: int = 2) -> int | float:
        """
        Calculate the volume of a cone

        Args:
            base_radius (int | float): The radius of the base of the cone.
            height (int | float): The height of the cone
            rounding_factor (int, optional): The number of decimal places the final result should have. Default is 2.

        Returns:
            int | float: The calculated volume of the cone.

        Example:
            >>> get_cone_volume(2, 2)
            8.38
        """
        self.validate_instance((int, float), base_radius)
        self.validate_instance((int, float), height)

        cone_formula = (settings.PI * pow(base_radius, 2) * height) / 3
        return round(cone_formula, rounding_factor)
    

    def get_rectangle_volume(self, length: int | float, height: int | float, width: int | float, rounding_factor: int = 2) -> int | float:
        """
        Calculate the volume of a rectangle

        Args:
            length (int | float): The length of the rectangle
            height (int | float): The height of the rectangle
            width (int | float): The width of the rectangle
            rounding_factor (int, optional): The number of decimal places in the final result. Default is 2

        Returns:
            int | float: The final calculated volume for the rectangle.

        Example:
            >>> from src.halting.formulas.formulas import GeneralFormulas()
            >>> general_formulas = GeneralFormulas()
            >>> general_formulas.calculate_volume_of_a_rectangle(2, 2, 2)
            8
        """
        self.validate_instance((int, float), length)
        self.validate_instance((int, float), height)
        self.validate_instance((int, float), width)

        rectangle_formula = length * height * width
        return round(rectangle_formula, rounding_factor)


    def calculate_spherical_cap_volume(self, height: int | float, ball_radius: int | float) -> int | float:
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
        self.validate(height, ball_radius)

        spherical_cap = (settings.PI / 3) * pow(height, 2) * (3*ball_radius - height)
        return round(spherical_cap, 4)

    def calculate_capsule_volume(self, base_radius: int | float, height: int | float) -> int | float:
        """
        Calculates the volume of a capsule.

        Args:
            base_radius (int | float): The radius of the capsule.
            height (int | float): The total height of the capsule.

        Returns:
            int | float: The calculated capsule volume.
            
        Example:    
            >>> from src.halting.formulas.formulas import GeneralFormulas
            >>> general_formulas = GeneralFormulas()
            >>> general_formulas.calculate_volume_of_a_capsule(2, 2)
            58.64
        """
        self.validate(base_radius, height)

        capsule = settings.PI * pow(base_radius, 2) * (((4/3)* base_radius) + height)
        return round(capsule, 4)

    def calculate_ellipsoid_volume(self, axis_a: int | float, axis_b: int | float, axis_c: int | float) -> int | float:
        """
        Calculate the volume of an ellipsoid

        Args:
            axis_a (int | float): The A axis of the ellipsoid.
            axis_b (int | float): The B axis of the ellipsoid.
            axis_c (int | float): The C axis of the ellipsoid.

        Returns:
            int | float: The calculated volume of the ellipsoid.

        Example:
            >>> from src.halting.formulas.volume import VolumeFormulas
            >>> volume = VolumeFormulas()
            >>> volume.calculate_ellipsoid_volume(2, 2, 2)
            33.5103            
        """
        self.validate(axis_a, axis_b, axis_c)

        ellipsoid = (4 * settings.PI * axis_a * axis_b * axis_c) / 3
        return round(ellipsoid, 4)
