##################################################
# Imports
##################################################
import unittest
from unittest import TestCase
from src.halting.base import BaseHalting

##################################################
# Base Halting Test Case Implementation
##################################################

class BaseHaltingTestCase(TestCase):

    # TODO: there are validation tests being made through the entire codebase
    # those tests should be moved here

    def setUp(self) -> None:
        self.base_halting = BaseHalting()
        return super().setUp()
    
    def test_base_halting_initialization(self):
        pass

    def test_validate_instance(self):
        pass

if __name__ == "__main__":
    unittest.main()
