##################################################
# Imports
##################################################
from src.halting.base import BaseHalting

##################################################
# Sets Class Implementation
##################################################
class Sets(BaseHalting):
    
    # TODO: create tests for the new include_zero flag
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
        pass

    def is_number_real(self, number: int | float) -> bool:
        """
        _summary_

        Args:
            number (int | float): _description_

        Returns:
            bool: _description_
        """
        pass

    def is_number_imaginary(self, number: int | float) -> bool:
        """
        I do not know anything about this.

        Args:
            number (int | float): _description_

        Returns:
            bool: _description_
        """
        pass

    

# to check if a number is rational we need to reverse enginner into a geratriz fraction
# if the number can be converted in a fraction, it means that it is rational.

    def convert_to_fraction(self, number: int | float) -> str | None:
        """
        _summary_

        Args:
            number (int | float): _description_

        Returns:
            str | None: _description_

        Example:
            >>> convert_to_fraction(5.45454)

        """

        ####################
        # dizima periodica simples é quando, após a vírgula, aparecem apenas
        #  algarismos que se repetem

        # 1.04545
        # x = 1.04545

        # multiply by 1000 since there is 3 different figures

        # 1000x = 1045.45
        # 
        pass
