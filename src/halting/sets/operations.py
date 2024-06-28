# this file will have sets properties and representations

##################################################
# Imports
##################################################
from src.halting.base import BaseHalting

##################################################
# Set Operations Class Implementation
##################################################
class SetOperations(BaseHalting):

    def is_set_empty(self, set_value: list) -> bool:
        """
        An empty set is a set that does not have any elements.

        This functions checks of a set is empty by returing a boolean value.

        Args:
            set_value (list): THe set for checking.

        Returns:
            bool: True if the set does not contain any elements, False otherwise.
        """
        self.validate_instance((list, set, dict), set_value)
        return len(set_value) == 0

    def is_set_unitary(self, set_value: list) -> bool:
        """
        A unitary set is a set that has only one element.

        This function checks if a set has only one element
        by returning a boolean value.

        Args:
            set (list): The set for checking.

        Returns:
            bool: True if the set contains only one element, False otherwise.
        """
        self.validate_instance((list, set, dict), set_value)

        return len(set_value) == 1 
    
    def set_union(self):
        pass

    # def set_inter

