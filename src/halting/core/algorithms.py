##################################################
# Imports
##################################################
from src.halting.base import BaseHalting

##################################################
# Implementation
##################################################
class Algorithms(BaseHalting):
    """
    This class contains methods that perform
    different types of algorithms.
    """
    def sieve_of_erastosthenes(self, n: int) -> list:
        """
        This function lists all prime numbers between
        0 and `number_range` inclusive.

        Args:
            n (int): The limit number for listing the prime numbers.

        Returns:
            list: The all containing all prime numbers between 2 and n inclusive.

        Example:
            >>> sieve_of_erastosthenes(20)
            [2, 3, 5, 7, 11, 13, 17, 19]
        """
        self.validate_instance(int, n)

        list_of_primes = []

        prime = [True for i in range(n + 1)]
        p = 2

        while p * p <= n:

            if prime[p]:

                for i in range(p * p, n + 1, p):
                    prime[i] = False

            p += 1

        for p in range(2, n + 1):
            if prime[p]:
                list_of_primes.append(p)

        return list_of_primes