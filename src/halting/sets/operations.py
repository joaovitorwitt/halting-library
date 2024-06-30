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
        if set1 == {}:
            set1 = set(set1)

        if set2 == {}:
            set2 = set(set2)
            
        self.validate_instance(set, set1, set2)
        resulting_set = set1.copy()
        for element in set2:
            if element not in resulting_set:
                resulting_set.add(element)

        return resulting_set

    def set_intersection(self, set1: set, set2: set) -> set:
        """
        Given two sets, A and B, the intersection of two sets
        are the elements that belong to both sets A and B.

        This function takes two sets as input and calculates
        the intersection A ∩ B.

        Args:
            set1 (set): The first set.
            set2 (set): The second set.

        Returns:
            set: A brand new set with the elements that are present in both sets.

        Example:
            >>> set_intersection({1,2,3,4}, {3,4,5,6})
            {3,4}
        """
        if set1 == {}:
            set1 = set(set1)

        if set2 == {}:
            set2 = set(set2)

        resulting_set = set()
        merge_sets = []

        for element in set1:
            merge_sets.append(element)

        for element in set2:
            merge_sets.append(element)

        self.validate_instance(set, set1, set2)
        merge_sets.sort()

        for index, element in enumerate(merge_sets):
            if merge_sets[index] == merge_sets[index - 1]:
                resulting_set.add(merge_sets[index])

        if len(resulting_set) == 0:
            resulting_set = {}
        return resulting_set

    def set_difference(self, set1: set, set2: set) -> set:
        """
        Given the sets A and B, the difference of the sets
        are the elements that belong to set A but do not belong
        to set B.

        This function takes two sets and calculates the difference
        between them, A - B.

        Args:
            set1 (set): The set to perform the difference.
            set2 (set): The second set of elements.

        Returns:
            set: The set of elements that are on the first set but no in the second set.

        Example:
            >>> set_difference({21,22,23,24,25,26,27}, {2,7,11,13,23,27})
            {21,22,24,25,26}
        """
        if set1 == {}:
            set1 = set(set1)

        if set2 == {}:
            set2 = set(set2)

        self.validate_instance(set, set1, set2)
        for element in set2:
            if element in set1:
                set1.remove(element)

        if len(set1) == 0:
            set1 = {}
        return set1

    def element_belongs_to_set(self, element: int | str | float, set1: set) -> bool:
        """
        This function returns a boolean indicating whether an element
        belongs to a set or not by perfomring the following operation:
        x ∈ A

        Args:
            element (int | str | float): The element to check if is in the set.
            set1 (set): The set to be used.

        Returns:
            bool: True if the element is in the set, False otherwise.

        Example:
            >>> element_belongs_to_set(3, {1,2,3})
            True
        """
        self.validate_instance(set, set1)
        self.validate(element)
        return element in set1

    def set_is_subset(self, subset: set, set2: set) -> bool:
        """
        A set is considered a subset of another set if 
        all the elements from a set A belong to a set B.

        In other words, A is a subset of B if, only if, all
        elements from A also belong to B. A ⊆ B.

        Args:
            subset (set): The `subset` will be used as the subset.
            set2 (set): The `set2` will be the outer set.

        Returns:
            bool: True if ``subset`` is a subset of `set2`, False otherwise.

        Example:
            >>> set_is_subset({1,2,3}, {0,1,2,3,4})
            True
        """
        true_counter = 0
        length_set = len(subset)


        for element in subset:
            if element in set2:
                true_counter += 1

        return true_counter == length_set



        
