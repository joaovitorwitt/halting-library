##################################################
# Imports
##################################################
from os.path import pat


##################################################
# Significant Figures Implementation
##################################################
class SignificantFigures(object):

    def __init__(self) -> None:
        pass

    def calculate_number_of_significant_figures(self, figure: int | float) -> dict:
        """
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
        return {
            'number of significant figures': figure,
            'figures that are significant': [3, 4, 4, 5, 0]
        }