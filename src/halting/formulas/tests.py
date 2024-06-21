##################################################
# Imports
##################################################
import unittest
from unittest import TestCase

from src.halting.formulas.formulas import GeneralFormulas

##################################################
# Formulas Class Test Case Implementation
##################################################
class GeneralFormulasTestCase(TestCase):

    def setUp(self) -> None:
        self.formulas = GeneralFormulas()
        return super().setUp()
    
    def test_calculate_cylinder_volume(self):
        pass
    