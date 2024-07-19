##################################################
# Imports
##################################################
from src.halting.base import BaseHalting

from src.halting import settings

##################################################
# Area Formulas Implementation
##################################################
class AreaFormulas(BaseHalting):
    """
    This contains various methods used to calculate the area of different shapes.
    """
    def calculate_rectangle_area(self, length: int | float, width: int | float) -> int | float:
        """
        Calculates the area of a rectangle by multiplying the sides.

        Args:
            length (int | float): The length of the rectangle.
            width (int | float): The width of the width.

        Returns:
            int | float: The calculated value for the rectangle area.

        Example:
            >>> from src.halting.formulas.area import AreaFormulas
            >>> area = AreaFormulas()
            >>> area.calculate_rectangle_area(12, 3)
            36
        """
        self.validate(length, width)

        rectangle = width * length 
        return round(rectangle, 4)
    
    def calculate_triangle_area(self, base: int | float, height: int | float) -> int | float:
        """
        Calculates the area of a triangle.

        Args:
            base (int | float): The base of the triangle.
            height (int | float): The height of the triangle.

        Returns:
            int | float: The area of the triangle.

        Example:
            >>> from src.halting.formulas.area import AreaFormulas
            >>> area = AreaFormulas()
            >>> area.calculate_triangle_area(2, 4)
            2
        """
        self.validate(base, height)

        triangle = (1*base*height) / 2
        return round(triangle, 4)

    def calculate_trapezoid_area(self, base: int | float, small_base: int | float, height: int | float) -> int | float:
        """
        Calculate the area of a trapezoid.

        Args:
            base (int | float): The larger base of the trapezoid.
            small_base (int | float): The smaller base of the trapezoid.
            height (int | float): The height of the trapezoid.

        Returns:
            int | float: The calculated area for a trapezoid.

        Example:
            >>> from src.halting.formulas.area import AreaFormulas
            >>> area = AreaFormulas()
            >>> area.calculate_trapezoid_area(3, 4, 6)
            21.0
        """
        self.validate(base, small_base, height)

        trapezoid = ((base + small_base) * height) / 2
        return round(trapezoid, 4)
    
    def calculate_circle_area(self, radius: int | float) -> int | float:
        """
        Calculate the area of a circle.

        Args:
            radius (int | float): The radius of the circle.

        Returns:
            int | float: The calculated area for the circle.

        Example:
            >>> from src.halting.formulas.area import AreaFormulas
            >>> area = AreaFormulas()
            >>> area.calculate_circle_area(3)
            28.2743
        """
        self.validate(radius)

        circle = settings.PI * pow(radius, 2)
        return round(circle, 4)
