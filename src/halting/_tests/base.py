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

    def setUp(self) -> None:
        self.base_halting = BaseHalting()
        return super().setUp()
    
    def test_base_halting_initialization(self):
        pass

if __name__ == "__main__":
    unittest.main()
