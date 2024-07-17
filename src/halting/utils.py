##################################################
# Imports
##################################################
from src.halting.base import BaseHalting

##################################################
# Utils Implementation
##################################################
class Utils(BaseHalting):
    @classmethod
    def multiplication_factor_in_repeating_sequence(cls, set_length: int) -> str:
        """
        When we are trying to find the fraction from which the rational number
        was generated we need to multiply the decimal numbers by a specific factor.

        For instance, lets say that our number is '2.454545'.

        After the decimal point we are able to tell that we have 2 different numbers,
        the '4' and the '5'. Since there are 2 we must multiply in the calculation by
        100. If it was only '1', like in this example: 2.777, we would multiply later
        in the equation by 10.

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
    
    @classmethod
    def convert_integer_to_list(cls, number: int | float) -> list:
        """
        This function takes a number as argument, it can be either 
        an integer or float, and converts to a list by first 
        converting the value to a string then casting the value to 
        a list.

        Args:
            number (int | float): The number to be casted to list.

        Returns:
            list: The new converted list.

        Example:
            >>> Utils.convert_integer_to_list(123)
            ['1', '2', '3']
        """
        cls.validate_instance(cls, (int, float), number)
        return list(str(number))

    @classmethod
    def slice_list_from_starting_index(cls, index: int, list_element: list) -> list:
        """
        This function takes a list and an index as arguments
        and slices the list starting from the given `index`. In other words

        Args:
            index (int): The index element to perform the slicing.
            list_element (list): The list to be sliced.

        Returns:
            list: The new sliced list.

        Example:
            >>> Utils.slice_list_from_starting_index(2, ['a', 'b', 'c', 'd', 'e', 'f'])
            ['c', 'd', 'e', 'f']
        """
        cls.validate_instance(cls, (int, list), index, list_element) # validation is not working as expected
        return list_element[index::]

    @classmethod
    def slice_list_from_ending_index(cls, index: int, list_element: list) -> list:
        """
        This function takes a list and an index as arguments and slices the list starting
        from the end at the given `index`.

        Args:
            index (int): The index element to perform the slicing.
            list_element (list): The list to be sliced.

        Returns:
            list: The new sliced list.

        Example:
            >>> Utils.slice_list_from_ending_index(3, ['a', 'b', 'c', 'd', 'e', 'f'])
            ['a', 'b', 'c']
        """
        return list_element[:-index:]
