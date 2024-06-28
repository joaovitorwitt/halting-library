##################################################
# Imports
##################################################
from typing import Any

##################################################
# Base Halting Implementation
##################################################
class BaseHalting:
    """
    This is the base class for the halting library

    It will contain a few methods which will be useful for handling and validating opereations.
    """
    def validate(self, *args: Any) -> bool:
        """
        This method validates a value passed as input into other functions.

        Args:
            value (Any): The value to be validated.

        Raises:
            TypeError: If the value is not an integer or float type.

        Returns:
            bool: True if the parameter is valid, false otherwise.
        """
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise TypeError(f"'{type(arg).__name__}' is not allowed, only integer or float")
            
            if arg < 0:
                raise ValueError("Negative values are not allowed.")

    def validate_instance(self, instance_type: tuple, *args) -> Any:
        for arg in args:
            if not isinstance(arg, (instance_type)):
                raise TypeError(f"'{type(arg).__name__}' is not allowed.")
            

    def __eq__(self, value: object) -> bool:
        return self.__dict__ == value.__dict__
    
    


    
        