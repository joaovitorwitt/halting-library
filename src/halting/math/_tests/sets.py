###########################################################################
# Imports
###########################################################################
import unittest
from unittest import TestCase

from src.halting.math.sets import Sets

###########################################################################
# Implementation
###########################################################################
class SetsTestCase(TestCase):

    def setUp(self) -> None:
        self.set_operations = Sets()
        return super().setUp()

    def test_is_set_empty(self):
        self.assertTrue(self.set_operations.is_set_empty([]))
        self.assertTrue(self.set_operations.is_set_empty({}))


    def test_is_set_unitary(self):
        self.assertTrue(self.set_operations.is_set_unitary([1]))
        self.assertTrue(self.set_operations.is_set_unitary({1}))
        self.assertFalse(self.set_operations.is_set_unitary([1,2,3,4]))
        self.assertFalse(self.set_operations.is_set_unitary({1,2,3,4}))


    def test_set_union(self):
        self.assertSetEqual(self.set_operations.set_union({2}, {45}), {2, 45})
        self.assertSetEqual(self.set_operations.set_union({'a'}, {'b', 'z'}), {'a', 'b', 'z'})
        self.assertSetEqual(self.set_operations.set_union({9, 73, 3, 2}, {1}), {1,2,3,9,73})
        self.assertSetEqual(self.set_operations.set_union({5, 10, 15, 20, 25}, {10, 20, 30, 40, 50}), {5, 10, 15, 20, 25, 30, 40, 50})
        self.assertSetEqual(self.set_operations.set_union({}, {1,2,3}), {1,2,3})
        self.assertSetEqual(self.set_operations.set_union({1,2,3}, {}), {1,2,3})


    def test_set_intersection(self):
        self.assertSetEqual(self.set_operations.set_intersection({0,1,2,3,4,5,6,7}, {0,2,4,6,8}), {0,2,4,6})
        self.assertSetEqual(self.set_operations.set_intersection({21, 22, 23, 24, 25, 26, 27}, {2, 3, 5, 7, 11, 13, 17, 19, 23, 27}), {23, 27})
        self.assertEqual(self.set_operations.set_intersection({21, 22, 24, 25, 26}, {2, 3, 5, 7, 11, 13, 17, 19, 23, 27}), {})
        self.assertEqual(self.set_operations.set_intersection({1,2,3}, {4,5,6}), {})


    def test_set_difference(self):
        self.assertSetEqual(self.set_operations.set_difference({21,22,23,27}, {2,7,9,11,23,27}), {21,22})
        self.assertSetEqual(self.set_operations.set_difference({21,22,23,24,25,26,27}, {2,7,11,13,23,27}), {21,22,24,25,26})
        self.assertSetEqual(self.set_operations.set_difference({1,2,3}, {}), {1,2,3})
        self.assertEqual(self.set_operations.set_difference({}, {1,2,3}), {})
        self.assertEqual(self.set_operations.set_difference({}, {1,2,3}), {})
        self.assertEqual(self.set_operations.set_difference({1,2,-3}, {1,2,3}), {-3})


    def test_element_belongs_to_set(self):
        self.assertTrue(self.set_operations.element_belongs_to_set(1, {1,2,3}))
        self.assertTrue(self.set_operations.element_belongs_to_set(3, {1,2,3}))
        self.assertFalse(self.set_operations.element_belongs_to_set(5, {1,2,3}))


    def test_set_is_subset(self):
        self.assertTrue(self.set_operations.set_is_subset({1,2,3}, {0,1,2,3,4}))
        self.assertTrue(self.set_operations.set_is_subset({10, 20, 30, 40, 50}, {5, 10,15,20,25,30,35,40,45,50}))
        self.assertTrue(self.set_operations.set_is_subset({}, {1,2,3}))
        self.assertTrue(self.set_operations.set_is_subset({1,2,3}, {1,2,3}))

        self.assertFalse(self.set_operations.set_is_subset({1,2,6}, {1,2,3,4,5}))
        self.assertFalse(self.set_operations.set_is_subset({1,2,3}, {}))

if __name__ == "__main__":
    unittest.main()
