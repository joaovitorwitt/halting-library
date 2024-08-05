###########################################################################
# Imports
###########################################################################
from src.halting.base import BaseHalting
from src.halting.core.algorithms import Algorithms
from src.halting.utils import Utils

###########################################################################
# Implementation
###########################################################################
class Numbers(BaseHalting):
    """
    The `Numbers` class is designed to handle the checking of
    mathematical rules or the manipulation of numbers.
    """
    def is_number_natural(self, number: int | float, include_zero: bool = True) -> bool: 
        """
        A natural number is a number that starts at zero and goes to infinity.
        We have two types of operations with natural numbers: multiplication and
        addition, if we multiply or add two natural numbers the result will always
        be a natural number as well.

        To be considered a natural number, the number has to be greater than 
        zero and not be a float.

        Args:
            number (int | float): The number to be checked as a natural.
            include_zero (bool): Flag to check if we consider the zero in our set. ℕ*

        Returns:
            bool: True if the number is natural, False otherwise.

        Example:
            >>> is_number_natural(1)
            True

            >>> is_number_natural(0)
            True
            
            >>> is_number_natural(0, include_zero=False)
            False
        """
        self.validate_instance((int, float), number)
        if not include_zero:
            return int(number) > 0 and not isinstance(number, float)
        return int(number) >= 0 and not isinstance(number, float)


    def is_number_integer(self, number: int | float) -> bool:
        """
        In set theory, the integer numbers are represented
        by all negative numbers and natural numbers. Now, integer
        numbers support subtraction operations as well.

        To be considered an integer value, the number still needs
        to be whole.

        Args:
            number (int | float): The number to be checked as an integer.

        Returns:
            bool: True if the number is integer, False otherwise.

        Example:
            >>> is_number_integer(-2)
            True

            >>> is_number_integer(5)
            True
        """
        self.validate_instance((int, float), number)
        return not isinstance(number, float)


    # to check if a number is rational we need to reverse enginner into a geratriz fraction
    # if the number can be converted in a fraction, it means that it is rational.
    def is_number_rational(self, number: int | float) -> bool:
        """
        Rational numbers came with the necessity of express measures.

        The set of all rational numbers is represented by all the
        numbers that can be written in the form of A/B, with A ∈ Z
        and B ∈ Z*.

        Args:
            number (int | float): The number to be checked as rational.

        Returns:
            bool: True if the number is rational, False otherwise.
        """
        self.validate_instance((float, int), number)
        return isinstance(number, (float, int))


    def is_number_irrational(self, number: int | float) -> bool:
        """
        Irrational numbers are numbers that cannot be expressed in
        A/B, with A ∈ Z and B ∈ Z*. They are usually not finite and
        not a periodic decimal.

        I = R - Q 

        Irrational number are composed by the difference of Real numbers
        and the rational numbers.
        """
        pass # pylint: disable=unnecessary-pass


    def is_number_real(self, number: int | float) -> bool:
        """
        In set theory, real numbers include irrational, rational, integers,
        and whole numbers.

        Args:
            number (int | float): The number to be validated.

        Returns:
            bool: True, if the number is considered a real number. False otherwise.
        """
        return isinstance(number, (int, float))


    def is_number_imaginary(self, number: int | float) -> bool:
        """
        I do not know anything about this.

        Args:
            number (int | float): The number to be checked as imaginary.

        Returns:
            bool: True, if the number is imaginary, False otherwise.
        """
        pass # pylint: disable=unnecessary-pass


    def calculate_number_of_significant_figures(self, figures: str) -> int:
        """
        Significant figures are the digits of a number that are meaningful in terms of accuracy or precision.

        This function is designed to take a number, it can either be a integer or a float, 
        and return the number of significant figures, following the significant figures rules.
        Non-zero digits are always significant, zeros between non-zero digits are always significant (9009)

        Args:
            figures (str): The number formatted in string.

        Returns:
            int: The number of significant figures.

        Usage:
            >>> from src.halting.figures.numbres import ManageFigures
            >>> figures = ManageFigures()
            >>> figures.calculate_number_of_significant_figures(344.50)
            >>> 5
        """
        trailing_number_of_zeros = 0
        leading_number_of_zeros = 0

        # deal with numbers without decimal point
        try:
            if isinstance(int(figures), int):
                if '0' not in figures:
                    return len(figures)
                
                if figures[-1] == '0':
                    for number in figures[::-1]:
                        if number == '0':
                            trailing_number_of_zeros += 1
                        else:
                            break
                    return len(figures) - trailing_number_of_zeros
                
        # if we have a Value Error means that there was a '.' in the integer conversion
        # # dont know if this was the best approach 
        except ValueError:
            to_list = list(figures)
            
            for number in to_list:
                if number == '0':
                    leading_number_of_zeros += 1
                
                elif number == '.':
                    continue

                else:
                    break
            return len(to_list) - (leading_number_of_zeros + 1)

    # TODO
    def scientific_notation_to_integer(self, scientific_notation: int | float) -> int | float:
        """
        Takes a scientific notation if the format: `4.4e5` and converts to its integer value.
        `4.4e5` represents `4.4 * 10 ^5`

        Args:
            scientific_notation (int | float): The number to be converted into its integer form.

        Returns:
            int | float: The formatted number now in integer or float form.

        Example:
            >>> from src.halting.figures.numbers import ManageFigures
            >>> figures = ManageFigures()
            >>> figures.scientific_notation_to_integer(5.6)
        """
        return scientific_notation
    
    # TODO: add 'written' notation type 
    def convert_number_to_scientific_notation(self, number: int | float, notation_type: str = 'e') -> str:
        """
        Scientific notation is a way of representing numbers that are either
        too low or to large, for instance the radius of an atom.

        This function takes a number as argument and returns that same
        number now is scientific notation format.

        Args:
            number (int): The number to be converted to scientif notation.
            notation_type (str): The way you wish the number is represented, the options are `e`, `n`, and `eng`. Defaults to `e`.

        Returns:
            str: The number now in scientific notation.

        Example:
            >>> convert_number_to_scientific_notation(50000000)
            '5e7'

            >>> convert_number_to_scientific_notation(0.00000000098)
            '9.8e-10'

            >>> convert_number_to_scientific_notation(120000000, notation_type='n')
            '1.2 x 10^-8'
        """
        self.validate_instance((int, float), number)
        self.validate_instance(str, notation_type)

        # ['5', '0', '0', '0', '0']
        converted = Utils.convert_integer_to_list(number)
        
        # number greater than zero means move the decimal to the left
        # 50000 === 5.0000 === 5e4
        if number > 1:
            # ['5', '.', '0', '0', '0', '0']
            converted.insert(1, '.')
                        #|| need to create a new list starting from this value and count the number of elements
            # ['5', '.', '0', '0', '0', '0']
            decimal_dot = Utils.get_decimal_point_in_float_value(converted)

            # ['0', '0', '0', '0'] === 4 
            new_list = len(Utils.slice_list_from_starting_index(decimal_dot, converted))

            coefficient = ''.join([x for x in converted if x != '0'])

            return f'{coefficient}e{new_list}'
        
        # number less than zero means move the decimal to the right
        # 0.0005 == 00005. === 5e-4
        if number < 1:
            # ['0', '.', '0', '0', '0', '.', '5']
            
            converted.append('.')

            # remove the first decimal dot from the list
            first_decimal_occurrence = converted.index('.')
            del converted[first_decimal_occurrence]

            # get number of places the decimal moved
            exponent = len(converted[first_decimal_occurrence:-1])

            coefficient = converted[-2]

            return f'{coefficient}e-{exponent}'



        # for the exponent
        # loop through the list
        # if the number is different than zero
        # we stop and get the index of the next place


        

    
    # TODO: currently, this only works for simple decimal numbers. Like these ones:
    # 0.161616 , 2.77777
    def convert_decimal_to_fraction(self, number: int | float) -> str | None:
        """
        This function takes a float value and converts to a fraction
        to check if the number is rational.

        Args:
            number (float): The number with decimal point for checking.

        Returns:
            str | None: The fraction representation of the number if possible, othewise returns None.

        Example:
            >>> convert_to_fraction(1.3535)
            '134/99'
        """
        x = number

        # convert the number to a list of strings
        to_list = Utils.convert_integer_to_list(number)

        # get the index of the dot
        decimal_dot_index = Utils.get_decimal_point_in_float_value(to_list)
        
        # slice the list starting after the dot to extract all the decimals
        decimal = len(set(Utils.slice_list_from_starting_index(decimal_dot_index, to_list)))
        periodic = Utils.multiplication_factor_in_repeating_sequence(decimal)

        x_value = periodic * number
        
        first_op = x_value - x

        second_op = periodic - 1 # this 1 shouldnt be hardcoded (this will only work if the repeating sequence is up to 2)

        return f'{round(first_op)}/{second_op}'

    def is_number_prime(self, number: int) -> bool:
        """
        A prime number is a whole number greater
        than one that has only two factors one
        and itself. In other words, it can only
        be divided by one and itself.
        
        This function checks whether a number is prime
        or not by returing a boolean value.

        Args:
            number (int): The number to be checked as prime.

        Returns:
            bool: True if the number is a prime number, False otherwise.

        Example:
            >>> is_number_prime(17)
            True

            >>> is_number_prime(2)
            True

            >>> is_number_prime(10)
            False
        """
        self.validate_instance(int, number)
        return_value = Algorithms().sieve_of_erastosthenes(number)
        return number in return_value
    
    def is_number_composite(self, number: int) -> bool:
        """
        This function checks if the given `number` is
        a composite number or not.

        A composite number is a number obtained after
        multiplying two prime numbers.

        Args:
            number (int): The number that will be checked as composite.

        Returns:
            bool: True if the number is composite, False otherwise.

        Example:
            >>> is_number_composite(2)
            False

            >>> is_number_composite(10)
            True

            >>> is_number_composite(13)
            False
        """
        self.validate_instance(int, number)
        return_value = Algorithms().sieve_of_erastosthenes(number)
        return number not in return_value



    # TODO
    def check_if_number_is_multiple_of_another_number(self, x: int, y: int) -> bool:
        """
        This function checks wheter x is a proper multiple of y

        A proper multiple of a number x is a number greater
        than x and divisible by x
        """
        pass