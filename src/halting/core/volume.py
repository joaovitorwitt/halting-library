##################################################
# Imports
##################################################
from src.halting import settings

from src.halting.base import BaseHalting

##################################################
# Volume Formulas Implementation
##################################################
class VolumeFormulas(BaseHalting):
    """
    This class is used to calculate the volume of different polygons.
    """
    def calculate_cylinder_volume(self, height: int | float, base_radius: int | float) -> int | float:
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
        self.validate(height, base_radius)
        cylinder = height* settings.PI *(pow(base_radius, 2))
        return round(cylinder, 4)
    
    def calculate_sphere_volume(self, radius: int | float) -> int | float:
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
        self.validate(radius)

        sphere = (4 * settings.PI * (pow(radius, 3))) / 3
        return round(sphere, 4)
    
    def calculate_cube_volume(self, edge_length: int | float) -> int | float:
        """
        Calculate the volume of a cube.
        
        Args:
            edge_length (int, float): The edge length of the cube.
        
        Returns:
            int | float: The final calculated volume of the cube.
        
        Example:
            >>> from src.halting.formulas.formulas import GeneralFormulas
            >>> GeneralFormulas().calculate_volume_of_a_cube(3)
            27
        """
        self.validate(edge_length)

        cube = pow(edge_length, 3)
        return round(cube, 4)

    def calculate_cone_volume(self, base_radius: int | float, height: int | float) -> int | float:
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
        self.validate(base_radius, height)

        cone_formula = (settings.PI * pow(base_radius, 2) * height) / 3
        return round(cone_formula, 4)

    def calculate_rectangle_volume(self, length: int | float, height: int | float, width: int | float) -> int | float:
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
        self.validate(length, height, width)

        rectangle_formula = length * height * width
        return round(rectangle_formula, 4)

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
