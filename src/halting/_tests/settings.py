##################################################
# Imports
##################################################
import unittest
from unittest import TestCase

import math

from src.halting import settings


##################################################
# Settings Test Case Implementation
##################################################
class SettingsTestCase(TestCase):

    def setUp(self) -> None:
        self.setttings  = settings
        

    def test_pi(self):
        self.assertEqual(settings.PI, math.pi)



if __name__ == "__main__":
    unittest.main()
