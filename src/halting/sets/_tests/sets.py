##################################################
# Imports
##################################################
import unittest
from unittest import TestCase
from src.halting.sets.sets import Sets

##################################################
# Sets Test Case Implementation
##################################################
class SetsTestCase(TestCase):
    def setUp(self) -> None:
        self.sets = Sets()
        return super().setUp()
    
    ##################################################
    # Whole Numbers Test Case Implementation
    ##################################################
    def test_is_number_whole(self):
        pass

    ##################################################
    # Integer Numbers Test Case Implementation
    ##################################################
    def test_is_number_integer(self):
        pass

    ##################################################
    # Rational Numbers Test Case Implementation
    ##################################################
    def test_is_number_rational(self):
        pass

    ##################################################
    # Irrational Numbers Test Case Implementation
    ##################################################
    def test_is_number_irrational(self):
        pass

if __name__ == "__main__":
    unittest.main()