###########################################################################
# Imports
###########################################################################
from src.halting.base import BaseHalting

from src.halting import settings

###########################################################################
# Implementation
###########################################################################
class Logic(BaseHalting):


    def proposition(self, expression: str) -> bool:
        """
        In math, proposition is any statement that can be classified as either True or
        False. 

        This method takes two values and checks them against an operator. This operator
        can be either an equal sign, different sign, greater than sign.

        Args:
            expression (str): The expression

        Returns:
            bool: Boolean indicating whether the proposition is True of False.

        Example:
            >>> proposition("4 != 5")
            True

            >>> proposition("9 > 2")
            True

            >>> proposition("9 = 5")
            False
        """
        self.validate_instance((str), expression)
        token = expression.split()

        if len(token) == 3:
            return self._solve_expression(token[0], token[1], token[2])
        
        raise ValueError(f"Invalid expression: {expression}")
        
    def _solve_expression(self, first: str, operator: str, second: str) -> bool:
        """
        This private method is used to solve logical operations like equal, different,
        greater than, less than, and so on.

        Args:
            first (str): The first element of the operation
            operator (str): The operator used in the expression.
            second (str): The second element of the operation.

        Returns:
            bool: Boolean value indicating whether the expression is True or False.
        """
        if operator not in settings.LOGIC_OPERATORS:
            raise ValueError(f"Invalid operator: {operator}")
        
        if operator == "=":
            return first == second
        
        if operator == "!=":
            return first != second
        
        if operator == ">":
            return first > second
        
        if operator == "<":
            return first < second
        
        if operator == ">=":
            return first >= second
        
        if operator == "<=":
            return first <= second
        
        raise ValueError(f"Invalid operator: {operator}")













