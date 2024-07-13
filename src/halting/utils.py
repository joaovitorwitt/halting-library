
from src.halting.base import BaseHalting

##################################################
# Utils
##################################################
class Utils(BaseHalting):
    @classmethod
    def multiplication_factor_in_repeating_sequence(cls, set_length: int) -> str:
        """
        Helper function that takes the length
        of a set and return a number accordingly.

        This function is used to identify the number of elements in a periodic 
        fraction. For instance: "2.454545", this 

        Args:
            set_length (set): _description_

        Returns:
            int: The number based on the length of the set

        Example:
            >>> multiplication_factor_in_repeating_sequence(1)
            10

            >>> multiplication_factor_in_repeating_sequence(2)
            100

            >>> multiplication_factor_in_repeating_sequence(3)
            1000
        """
        cls.validate_instance(cls, int, set_length)
        return int('1'.ljust(set_length + 1, '0'))




