# ALGEBRA SECTION - https://www.calculatorsoup.com/calculators/algebra/

##################################################
# Imports
##################################################
from math import sqrt, cbrt

from src.halting.base import BaseHalting

##################################################
# Algebra Class Implementation
##################################################
class Algebra(BaseHalting):
    
    def calculate_exponent(self, base: int | float, exponent: int | float) -> int | float:
        """
        Calculatest the power of a real number.

        Args:
            base (int | float): The base number
            exponent (int | float): The exponent number

        Returns:
            int | float: The calculated exponent value.

        Example:
            >>> exponent_calculator(2, 3)
            8
        """
        self.validate_instance((int, float), base, exponent)

        result = pow(base, exponent)
        return result

    def square_root(self, value: int | float) -> int | float:
        """
        Calculates the square root of a given number.

        Args:
            value (int | float): The number to calculate its square root.

        Returns:
            int | float: The square root of the number.

        Example:
            >>> from src.halting.formulas.algebra import AlgebraFormulas
            >>> algebra = AlgebraFormulas()
            >>> algebra.square_root(25)
            5
        """
        self.validate(value)

        square_root = sqrt(value)
        return square_root

    def cubic_root(self, value: int | float) -> int | float:
        """
        Calculates the cubic root of a given integer.

        Args:
            value (int | float): The value to extract the cubic root.

        Returns:
            int | float: The cubic root for the given number.

        Example:
            >>> from src.halting.formulas.algebra import AlgebraFormulas
            >>> algebra = AlgebraFormulas()
            >>> algebra.cubic_root()
        """
        self.validate_instance((int, float), value)

        cubic_root = cbrt(value)
        return cubic_root
    
    def calculate_absolute_value(self, number: int | float) -> int | float:
        """
        Calculates the absolute value of a number, that is, the value without regarding its sign.

        Args:
            number (int | float): The number to get its absolute value.

        Returns:
            int | float: The absolute value of the number.

        Example:
            >>> from src.halting.formulas.algebra import AlgebraFormulas
            >>> algebra = AlgebraFormulas()
            >>> algebra.calculate_absolute_value(-3)
        """
        self.validate_instance((int, float), number)

        absolute_value = abs(number)
        return absolute_value



# Least commom multiple
# adding fractions
# subtracting fractions
# multiplying fractions
# dividing fractions