##################################################
# Imports
##################################################
import unittest
from unittest import TestCase

from src.halting.core.area import Area

##################################################
# Areas Formulas Test Case Implementation
##################################################
class AreaTestCase(TestCase):

    def setUp(self) -> None:
        self.area = Area()
        return super().setUp()
    

    def test_get_rectangle_area(self):
        self.assertEqual(self.area.get_rectangle_area(12, 3), 36)
        self.assertEqual(self.area.get_rectangle_area(0.125, 4), 0.5)
        self.assertEqual(self.area.get_rectangle_area(21.3, 4.3), 91.59)
        self.assertEqual(self.area.get_rectangle_area(0.0393, 2.2002, 4), 0.0865)


    def test_get_triangle_area(self):
        self.assertEqual(self.area.get_triangle_area(2, 4), 4)
        self.assertEqual(self.area.get_triangle_area(32, 23.3), 372.8)
        self.assertEqual(self.area.get_triangle_area(2.2, 9.3), 10.23)
        self.assertEqual(self.area.get_triangle_area(0.092, 2.233, 4), 0.1027)


    def test_get_trapezoid_area(self):
        self.assertEqual(self.area.get_trapezoid_area(3, 4, 6), 21)
        self.assertEqual(self.area.get_trapezoid_area(1.32, 2.3, 0.3), 0.54)
        self.assertEqual(self.area.get_trapezoid_area(45.4, 32.2, 23), 892.4)
        self.assertEqual(self.area.get_trapezoid_area(4.402, 0.002, 2.3, 4), 5.0646)


    def test_get_circle_area(self):
        self.assertEqual(self.area.get_circle_area(3), 28.27)
        self.assertEqual(self.area.get_circle_area(32.3, 4), 3277.5922)
        self.assertEqual(self.area.get_circle_area(0.09, 4), 0.0254)


if __name__ == "__main__":
    unittest.main()
