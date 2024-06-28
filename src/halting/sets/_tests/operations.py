##################################################
# Imports
##################################################
import unittest
from unittest import TestCase
from src.halting.sets.operations import SetOperations

##################################################
# Set Operations Test Case Implementation
##################################################
class SetOperationsTestCase(TestCase):
    def setUp(self) -> None:
        self.set_operations = SetOperations()
        return super().setUp()

    ##################################################
    # Set Empty Test Case
    ##################################################
    def test_is_set_empty(self):
        self.assertTrue(self.set_operations.is_set_empty([]))
        self.assertTrue(self.set_operations.is_set_empty({}))

    def test_is_set_empty_return_false(self):
        self.assertFalse(self.set_operations.is_set_empty([1,2,3,4]))
        self.assertFalse(self.set_operations.is_set_empty({1,2,3,4}))

    def test_is_set_empty_with_invalid_instance(self):
        with self.assertRaises(TypeError) as context:
            self.set_operations.is_set_empty('invalid string')

        self.assertEqual(str(context.exception), "'str' is not allowed.")

    ##################################################
    # Universal Set Test Case
    ##################################################
    def test_is_set_unitary(self):
        self.assertTrue(self.set_operations.is_set_unitary([1]))
        self.assertTrue(self.set_operations.is_set_unitary({1}))

    def test_is_set_unitary_return_false(self):
        self.assertFalse(self.set_operations.is_set_unitary([1,2,3,4]))
        self.assertFalse(self.set_operations.is_set_unitary({1,2,3,4}))

    def test_is_set_unitary_with_invalid_instance(self):
        with self.assertRaises(TypeError) as context:
            self.set_operations.is_set_empty('invalid instance')

        self.assertEqual(str(context.exception), "'str' is not allowed.")


if __name__ == "__main__":
    unittest.main()

