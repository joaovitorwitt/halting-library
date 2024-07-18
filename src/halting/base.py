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
        """
        Condition that we define for both objects
        to be equal. In this case we are saying that
        two objects will be equal if their dictionary
        is the same.

        Args:
            value (object): the object to be validated against the instance

        Returns:
            bool: True, if the objects are equal, False otherwise.
        """
        return self.__dict__ == value.__dict__
    


    def key_value_validation(self, **kwargs: Any) -> bool:
        """
        The purpose of this method is to validate the value and its
        instance when the function has more than one inputs.
        

        Args:
            **kwargs: The key value pair containing the

        Returns:
            bool: _description_
        """
        breakpoint()
        for key, value in kwargs.items():
            if not isinstance(key, value):
                raise TypeError("Invalid instance.")
            
        return "niggas"
    
    


    
        