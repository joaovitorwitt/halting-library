######################################################
# Imports
######################################################
import unittest
from unittest import TestCase

from src.halting.core.algorithms import Algorithms

######################################################
# Implementation
######################################################
class AlgorithmsTestCase(TestCase):

    def setUp(self) -> None:
        self.algorithms = Algorithms()

    def test_sieve_of_erastosthenes(self):
        self.assertListEqual(self.algorithms.sieve_of_erastosthenes(20), [2, 3, 5, 7, 11, 13, 17, 19])
        self.assertListEqual(self.algorithms.sieve_of_erastosthenes(100), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])
        self.assertListEqual(self.algorithms.sieve_of_erastosthenes(2), [2])


if __name__ == "__main__":
    unittest.main()