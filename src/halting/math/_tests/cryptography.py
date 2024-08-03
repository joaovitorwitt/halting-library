###########################################################################
# Imports
###########################################################################
import unittest
from unittest import TestCase

from src.halting.math.cryptography import Cryptography

###########################################################################
# Implementation
###########################################################################
class CryptographyTestCase(TestCase):
    
    def setUp(self) -> None:
        self.cryptography = Cryptography()

    def test_caesar_cipher(self):
        self.assertEqual(self.cryptography.caesar_cipher('abc', 3), 'def')
        self.assertEqual(self.cryptography.caesar_cipher('xyz', 3), 'abc')
        self.assertEqual(self.cryptography.caesar_cipher('ABC', 3), 'DEF')
        self.assertEqual(self.cryptography.caesar_cipher('AbC', 3), 'DeF')
        self.assertEqual(self.cryptography.caesar_cipher('a.b,c!', 3), 'd.e,f!')
        self.assertEqual(self.cryptography.caesar_cipher('y z', -2), 'w x')
        self.assertEqual(self.cryptography.caesar_cipher('abcdefghijklmnopqrstuvwxyz', 13), 'nopqrstuvwxyzabcdefghijklm')
        self.assertEqual(self.cryptography.caesar_cipher('abc', 29), 'def')


if __name__ == "__main__":
    unittest.main()
