###########################################################################
# Imports
###########################################################################
from src.halting.base import BaseHalting
from src.halting.utils import Utils

###########################################################################
# Implementation
###########################################################################
class Cryptography(BaseHalting):
    """
    In mathematics and Computer Science, cryptography
    is the practice and study of techniques for secure
    communication.

    This class contains various cryptographic methods
    and algorithms widely used in the field.
    """
    def caesar_cipher(self, plaintext: str, key: int) -> str:
        """
        This functions takes a `plaintext` and rotates
        every single letter by a specific `key`.

        For instance, let's say the current letter
        is 'a' and the key is 3, 'a' would become 'd',
        shifting 3 positions in the alphabet.

        Args:
            plaintext (str): The plaintext that will be encrypted
            key (int): The number of positions the letter will be changed.

        Returns:
            str: The encrypted plaintext.

        Example:
            >>> caesar_chiper('hello', 3)
            'khoor'

            
        """
        # loop through the plaintext to get every letter
        encrypted_text = ''
        for char in plaintext: # pylint: disable=not-an-iterable
                encrypted_text += Utils.rotate(char, key)

        return encrypted_text

        # ASCII TABLE
        # A = 65
        # Z = 90

        # a = 97
        # z = 122


    