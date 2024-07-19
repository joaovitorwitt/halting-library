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

    def test_pi(self):
        self.assertEqual(settings.PI, math.pi)

    def test_zero(self):
        self.assertEqual(settings.ZERO, 0)

    def test_eulers_constant(self):
        self.assertEqual(settings.EULER_CONSTANT, math.e)

    def test_phi(self):
        self.assertEqual(settings.PHI, ((1 + 5**0.5)/2))

    def test_speed_of_light(self):
        self.assertEqual(settings.SPEED_OF_LIGHT, 299792458)



if __name__ == "__main__":
    unittest.main()
