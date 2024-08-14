###########################################################################
# Imports
###########################################################################
from src.halting.base import BaseHalting

from src.halting import settings

###########################################################################
# Implementation
###########################################################################
class Logic(BaseHalting):

    def proposition(self, first: int, operation: str, second: int) -> bool:
        """
        In math, proposition is any statement that can be classified as either True or
        False. 

        This method takes two values and checks them against an operator. This operator
        can be either an equal sign, different sign, greater than sign.

        Args:
            first (int): The first element.
            operation (str): The operation that will be applied with both elements.
            second (int): The second element.

        Returns:
            bool: Boolean indicating whether the proposition is True of False.

        Example:
            >>> proposition(4, "!=", 5)
            True

            >>> proposition(9, ">", 2)
            True

            >>> proposition(9, "=", 5)
            False
        """
        self.validate_instance((int, float), second, first)

        if operation not in settings.LOGIC_OPERATIONS:
            raise ValueError(f"Invalid operator: {operation}")
        
        if operation == "=":
            return first == second
        
        if operation == "!=":
            return first != second
        
        if operation == ">":
            return first > second
        
        if operation == "<":
            return first < second
        
        if operation == ">=":
            return first >= second
        
        if operation == "<=":
            return first <= second
        

        

        












