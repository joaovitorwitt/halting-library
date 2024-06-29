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

    ##################################################
    # Set Union Test Case
    ##################################################
    def test_set_union(self):
        self.assertSetEqual(self.set_operations.set_union({2}, {45}), {2, 45})
        self.assertSetEqual(self.set_operations.set_union({'a'}, {'b', 'z'}), {'a', 'b', 'z'})
        self.assertSetEqual(self.set_operations.set_union({9, 73, 3, 2}, {1}), {1,2,3,9,73})
        self.assertSetEqual(self.set_operations.set_union({5, 10, 15, 20, 25}, {10, 20, 30, 40, 50}), {5, 10, 15, 20, 25, 30, 40, 50})
        self.assertSetEqual(self.set_operations.set_union({}, {1,2,3}), {1,2,3})

    def test_set_union_with_invalid_instance(self):
        with self.assertRaises(TypeError) as context:
            self.set_operations.set_union([1,2,3], [1,2,3])

        self.assertEqual(str(context.exception), "'list' is not allowed.")

if __name__ == "__main__":
    unittest.main()

