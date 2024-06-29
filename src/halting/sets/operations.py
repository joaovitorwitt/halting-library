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
    
    def set_union(self, set1: set, set2: set) -> set:
        """
        Performs an union operation on two sets A U B
        then returns the resulting set.

        Args:
            set1 (set): The first set
            set2 (set): The second set

        Returns:
            set: The resulting of uniting both sets.

        Example:
            >>> set_union({1,2,3}, {3,4,5})
            {1,2,3,4,5}
        """
        self.validate_instance(set, set1, set2)
        resulting_set = set1.copy()
        for element in set2:
            if element not in resulting_set:
                resulting_set.add(element)

        return resulting_set
        
    def set_difference(self):
        pass

    def set_intersection(self):
        pass

