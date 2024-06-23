##################################################
# Imports
##################################################
import unittest
from unittest import TestCase

from src.halting.formulas.algebra import AlgebraFormulas

##################################################
# Algebra Test Case Implementation
##################################################
class AlgebraFormulasTestCase(TestCase):

    def setUp(self) -> None:
        self.algebra = AlgebraFormulas()
        return super().setUp()


if __name__ == "__main__":
    unittest.main()