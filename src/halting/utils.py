##################################################
# Imports
##################################################
from src.halting.base import BaseHalting

##################################################
# Utils Implementation
##################################################
class Utils(BaseHalting):
    """
    The `Utils` class is designed to keep helper methods
    that are being used throughout the entire code.

    A few example of these methods are functions that
    convert integer to list, slice lists, and so on.
    """
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
        fraction. For instance: "2.454545", this means there are two different
        figures after the decimal point, with that in mind we return 100.

        Args:
            set_length (set): The length of a set indicating how many figures will be inside.

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
        cls.validate_instance(cls, int, index)
        cls.validate_instance(cls, list, list_element)
        return list_element[:-index:]

    @classmethod
    def get_decimal_point_in_float_value(cls, float_element: list) -> int:
        """
        This function takes a float value converted to a list and
        returns the index of the decimal point. This function is
        useful for performing operations on numbers after the decimal
        value.

        Args:
            float_element (list): The float value formatted as a list

        Returns:
            int: The index of the first value after the decimal point.
        """
        # TODO: edge case where the last element is the actual '.'
        cls.validate_instance(cls, list, float_element)
        try:
            return float_element.index('.') + 1
        except ValueError as exc:
            raise ValueError("'.' is no in the list") from exc
        


    @classmethod
    def rotate(cls, char: str, key: int) -> str:
        """
        This helper method takes a single character as
        input and also a key indicating the number of 
        places in the alphabet that character should
        shift.

        Args:
            char (str): The single character for the rotation
            key (int): Number of places the character should shift

        Returns:
            str: The character now shifted by the number of `key`.

        Example:
            >>> rotate('plaintext', 5)
            'uqfnsyjcy'
        """

        # temporary variable to hold the character value
        temp = char

        if temp.isupper():
            # first the the ascii code of the character
            # then subtract 65
            # adds the key value
            # then get the remainder of the operation
            # then add 65 again

            # example:
            # temp === C
            # 67 - 65 = 2
            # 2 + 3 = 5
            # 5 % 26 = 5
            # 5 + 65 = 70
            # 70 converted to char gives the letter F
            char_to_ascii = (((ord(temp) - 65 ) + key) % 26) + 65

            ascii_to_char = chr(char_to_ascii)

            return ascii_to_char
        
        if temp.islower():
            # same idea of the uppercase, except for the values in the ascii table
            char_to_ascii = (((ord(temp) - 97 ) + key) % 26) + 97

            ascii_to_char = chr(char_to_ascii)

            return ascii_to_char
        
        if temp.isspace():
            return temp
        
        if not temp.isalnum() and not temp.isspace():
            return temp