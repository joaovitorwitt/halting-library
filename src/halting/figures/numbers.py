##################################################
# Imports
##################################################
# https://packaging.python.org/en/latest/tutorials/packaging-projects/
from src.halting.base import BaseHalting
from src.halting.utils import Utils

##################################################
# Significant Figures Implementation
##################################################
class ManageFigures(BaseHalting):

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
    
    # currently, this only works for simple decimal numbers
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
        to_list = list(str(number))
        # get the index of the dot
        decimal_dot_index = to_list.index('.') + 1
        # slice the list starting after the dot to extract all the decimals
        decimal = len(set(to_list[decimal_dot_index::]))
        periodic = Utils.multiplication_factor_in_repeating_sequence(decimal)

        x_value = periodic * number
        
        first_op = x_value - x

        second_op = periodic - 1 # this 1 shouldnt be hardcoded (this will only work if the repeating sequence is up to 2)

        return f'{round(first_op)}/{second_op}'

        


