##################################################
# Imports
##################################################


##################################################
# Significant Figures Implementation
##################################################

def calculate_number_of_significant_figures(figure: int | float) -> dict:
    """
    Significant figures are the digits of a number that are meaningful in terms of accuracy or precision.

    This function is designed to take a number, it can either be a integer or a float, 
    and return the number of significant figures, as well as the figures in the number that are significant

    Args:
        figure (int | float): The number that we want to calculate

    Usage:
        >>> from <module> import calculate_number_of_significant_figures
        >>> calculate_number_of_significant_figures(344.50)
        >>> {
        ...     'Number of Significant Figures': 5,
        ...     'Significant Figures': [3,4,4,5,0]
        >>> }
        
    Returns:
        dict: Representing the number of significant figures and the figures that are significant
    """

    # Significant Figures Rules
    # - non zero digits are Always significant
    # - zeros in between non-zero digits are always significant 
    # example: 80989
    # - leading zeros are never significant
    # 0,0009 ===> 1 significant figure
    # - trailing zeros are only significant if the number contains a decimal point

    # 3450 ===> 3 significant figures
    # 8009 ===> 4 significant figures
    # 32243 ===> 5 significant figures

    trailing_number_of_zeros = 0
    leading_number_of_zeros = 0

    if isinstance(figure, int):
        number_of_significant_figures = list(str(figure))

        if '0' not in number_of_significant_figures:
            return len(number_of_significant_figures)

        elif number_of_significant_figures[-1] == '0':
            for number in number_of_significant_figures[::-1]:
                if number == '0':
                    trailing_number_of_zeros += 1
                else:
                    break
            
            return len(number_of_significant_figures) - trailing_number_of_zeros
        
        elif number_of_significant_figures[0] == '0':
            for number in number_of_significant_figures:
                if number == 0:
                    leading_number_of_zeros += 1
                else:
                    continue
            return (len(number_of_significant_figures) - leading_number_of_zeros) * (-1)
    
    elif isinstance(figure, float):
        return figure
                    
            
            # if last number is zero
            # count the number of zeros starting from the last zero
            # get the total number of zeros and subtract it from the len of the original array



# print(calculate_number_of_significant_figures(340500))
# print(calculate_number_of_significant_figures(102030))
# print(calculate_number_of_significant_figures(4050600))
# print(calculate_number_of_significant_figures(700800900))
# print(calculate_number_of_significant_figures(1002003000))
# print(calculate_number_of_significant_figures(120030040))
# print(calculate_number_of_significant_figures(500060007000))
# print(calculate_number_of_significant_figures(18009000))
# print(calculate_number_of_significant_figures(900040000))
# print(calculate_number_of_significant_figures(306050))
print(calculate_number_of_significant_figures(40005000600))

# https://packaging.python.org/en/latest/tutorials/packaging-projects/