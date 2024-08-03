##################################################
# Imports
##################################################
import unittest
from unittest import TestCase

from src.halting.math.cryptography import Cryptography

##################################################
# Base Halting Test Case
##################################################
class BaseHaltingTestCase(TestCase):

    def setUp(self) -> None:
        self.cryptography = Cryptography()


    def test_validate_instance(self):
        with self.assertRaises(TypeError) as context:
            self.cryptography.caesar_cipher(12, 1)

        self.assertEqual(str(context.exception), "'int' is not allowed.")


if __name__ == "__main__":
    unittest.main()
