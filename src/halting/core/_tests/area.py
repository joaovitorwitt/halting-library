##################################################
# Imports
##################################################
import unittest
from unittest import TestCase

from src.halting.core.area import Area

##################################################
# Areas Formulas Test Case Implementation
##################################################
class AreaFormulasTestCase(TestCase):

    def setUp(self) -> None:
        self.area = Area()
        return super().setUp()
    
    ##################################################
    # Rectangle Area Test Case Implementation
    ##################################################
    def test_get_rectangle_area(self):
        self.assertEqual(self.area.get_rectangle_area(12, 3), 36)
        self.assertEqual(self.area.get_rectangle_area(0.125, 4), 0.5)
        self.assertEqual(self.area.get_rectangle_area(21.3, 4.3), 91.59)


    ##################################################
    # Rectangle Area Test Case Implementation
    ##################################################
    def test_calculate_triangle_area(self):
        self.assertEqual(self.area.calculate_triangle_area(2, 4), 4)
        self.assertEqual(self.area.calculate_triangle_area(32, 23.3), 372.8)
        self.assertEqual(self.area.calculate_triangle_area(2.2, 9.3), 10.23)

    def test_calculate_triangle_area_with_invalid_type_raises_error(self):
        with self.assertRaises(TypeError) as context:
            self.area.calculate_triangle_area(1, '3')

        self.assertEqual(str(context.exception), "'str' is not allowed, only integer or float")

    def test_calculate_triangle_area_with_negative_value_raises_error(self):
        with self.assertRaises(ValueError) as context:
            self.area.calculate_triangle_area(1, -2)

        self.assertEqual(str(context.exception), "Negative values are not allowed.")

    ##################################################
    # Trapezoid Area Test Case Implementation
    ##################################################
    def test_calculate_trapezoid_area(self):
        self.assertEqual(self.area.calculate_trapezoid_area(3, 4, 6), 21)
        self.assertEqual(self.area.calculate_trapezoid_area(1.32, 2.3, 0.3), 0.543)
        self.assertEqual(self.area.calculate_trapezoid_area(45.4, 32.2, 23), 892.4)

    def test_calculate_trapezoid_area_with_invalid_type_raises_error(self):
        with self.assertRaises(TypeError) as context:
            self.area.calculate_trapezoid_area(2, 2, '3')

        self.assertEqual(str(context.exception), "'str' is not allowed, only integer or float")

    def test_calculate_trapezoid_area_with_negative_value_raises_error(self):
        with self.assertRaises(ValueError) as context:
            self.area.calculate_trapezoid_area(2, 2, -1)

        self.assertEqual(str(context.exception), "Negative values are not allowed.")

    ##################################################
    # Circle Area Test Case Implementation
    ##################################################
    def test_calculate_circle_area(self):
        self.assertEqual(self.area.calculate_circle_area(3), 28.2743)
        self.assertEqual(self.area.calculate_circle_area(32.3), 3277.5922)
        self.assertEqual(self.area.calculate_circle_area(0.09), 0.0254)

    def test_calculate_circle_area_with_invalid_type_raises_error(self):
        with self.assertRaises(TypeError) as context:
            self.area.calculate_circle_area('2')

        self.assertEqual(str(context.exception), "'str' is not allowed, only integer or float")

    def test_calculate_circle_area_with_negative_value_raises_error(self):
        with self.assertRaises(ValueError) as context:
            self.area.calculate_circle_area(-1)

        self.assertEqual(str(context.exception), "Negative values are not allowed.")

if __name__ == "__main__":
    unittest.main()
