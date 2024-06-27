##################################################
# Imports
##################################################
import unittest
from unittest import TestCase
from src.halting.sets.operations import SetOperations

##################################################
# Set Operations Test Case Implementation
##################################################
class SetOperationsTestCase(TestCase):
    def setUp(self) -> None:
        self.set_operations = SetOperations()
        return super().setUp()


    def test_is_set_empty(self):
        pass


if __name__ == "__main__":
    unittest.main()


