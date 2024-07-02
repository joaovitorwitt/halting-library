##################################################
# Imports
##################################################
from src.halting.base import BaseHalting

##################################################
# Sets Class Implementation
##################################################
class Sets(BaseHalting):
    
    def is_number_natural(self, number: int | float) -> bool:
        """
        A natural number is a number that starts at zero and goes to infinity.
        We have two types of operations with natural numbers: multiplication and
        addition, if we multiply or add two natural numbers the result will always
        be a natural number as well.

        To be considered a natural number, the number has to be greater than 
        zero and not be a float.

        Args:
            number (int | float): The number to be checked as a natural.

        Returns:
            bool: True if the number is natural, False otherwise.
        """
        self.validate_instance((int, float), number)
        return int(number) >= 0 and not isinstance(number, float)

    def is_number_integer(self, number: int | float) -> bool:
        return not isinstance(number, float)

    def is_number_rational(self, number: int | float) -> bool:
        pass

    def is_number_irrational(self, number: int | float) -> bool:
        """
        I = R - Q 

        Irrational number are composed by the difference of Real numbers
        and the rational numbers.
        """
        pass

    def is_number_real(self, number: int | float) -> bool:
        pass

    


