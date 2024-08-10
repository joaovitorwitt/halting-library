##################################################
# Imports
##################################################
from src.halting.base import BaseHalting

from src.halting import settings

##################################################
# Area Formulas Implementation
##################################################
class Area(BaseHalting):
    """
    This contains various methods used to calculate the area of different shapes.
    """
    def get_rectangle_area(self, length: int | float, width: int | float, rounding_factor: int = 2) -> int | float:
        """
        Calculates the area of a rectangle by multiplying the sides.

        Args:
            length (int | float): The length of the rectangle.
            width (int | float): The width of the width.
            rounding_factor (int, optional): The number of decimal places the result should have. Default is 2.

        Returns:
            int | float: The calculated value for the rectangle area.

        Example:
            >>> get_rectangle_area(12, 3)
            36
        """
        self.validate(length, width)
        self.validate_instance(int, rounding_factor)

        rectangle = width * length 
        return round(rectangle, rounding_factor)
    

    def get_triangle_area(self, base: int | float, height: int | float, rounding_factor: int = 2) -> int | float:
        """
        Calculates the area of a triangle.

        Args:
            base (int | float): The base of the triangle.
            height (int | float): The height of the triangle.
            rounding_factor (int, optional): The number of decimal places the final result should have. Default is 2.

        Returns:
            int | float: The area of the triangle.

        Example:
            >>> get_triangle_area(2, 4)
            2
        """
        self.validate(base, height)
        self.validate_instance(int, rounding_factor)

        triangle = (1 * base * height) / 2
        return round(triangle, rounding_factor)


    def get_trapezoid_area(self, base: int | float, small_base: int | float, height: int | float, rounding_factor: int = 2) -> int | float:
        """
        Calculate the area of a trapezoid.

        Args:
            base (int | float): The larger base of the trapezoid.
            small_base (int | float): The smaller base of the trapezoid.
            height (int | float): The height of the trapezoid.

        Returns:
            int | float: The calculated area for a trapezoid.

        Example:
            >>> get_trapezoid_area(3, 4, 6)
            21.0
        """
        self.validate(base, small_base, height)
        self.validate_instance(int, rounding_factor)

        trapezoid = ((base + small_base) * height) / 2
        return round(trapezoid, rounding_factor)
    
    
    def get_circle_area(self, radius: int | float, rounding_factor: int = 2) -> int | float:
        """
        Calculate the area of a circle.

        Args:
            radius (int | float): The radius of the circle.
            rounding_factor (int, optional): The number of decimal places the final result should have. Default is 2.

        Returns:
            int | float: The calculated area for the circle.

        Example:
            >>> get_circle_area(3)
            28.27
        """
        self.validate(radius)
        self.validate_instance(int, rounding_factor)

        circle = settings.PI * pow(radius, 2)
        return round(circle, rounding_factor)
