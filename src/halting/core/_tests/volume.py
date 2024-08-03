##################################################
# Imports
##################################################
import unittest
from unittest import TestCase

from src.halting.core.volume import VolumeFormulas

##################################################
# Volume Class Test Case Implementation
##################################################
class VolumeFormulasTestCase(TestCase):
    
    def setUp(self) -> None:
        self.volume = VolumeFormulas()
        return super().setUp()
    
    ##################################################
    #  Cylinder Volume Test Case Implementation
    ##################################################
    def test_calculate_cylinder_volume(self):
        self.assertEqual(self.volume.calculate_cylinder_volume(2, 2), 25.1327)
        self.assertEqual(self.volume.calculate_cylinder_volume(598, 21), 828494.5314)
        self.assertEqual(self.volume.calculate_cylinder_volume(0.0298, 0.876), 0.0718)

    def test_calculate_cylinder_volume_with_invalid_type_raises_error(self):
        with self.assertRaises(TypeError) as context:
            self.volume.calculate_cylinder_volume(2, '1')

        self.assertEqual(str(context.exception), "'str' is not allowed, only integer or float")

    def test_calculate_cylinder_volume_with_negative_value_raises_error(self):
        with self.assertRaises(ValueError) as context:
            self.volume.calculate_cylinder_volume(1, -1)

        self.assertEqual(str(context.exception), "Negative values are not allowed.")

    ##################################################
    #  Sphere Volume Test Case Implementation
    ##################################################
    def test_calculate_sphere_volume(self):
        self.assertEqual(self.volume.calculate_sphere_volume(2), 33.5103)
        self.assertEqual(self.volume.calculate_sphere_volume(0.39), 0.2485)
        self.assertEqual(self.volume.calculate_sphere_volume(323), 141154970.7279)

    def test_calculate_sphere_volume_with_invalid_type_raises_error(self):
        with self.assertRaises(TypeError) as context:
            self.volume.calculate_sphere_volume('2')

        self.assertEqual(str(context.exception), "'str' is not allowed, only integer or float")

    def test_calulate_sphere_volume_with_negative_value_raises_error(self):
        with self.assertRaises(ValueError) as context:
            self.volume.calculate_sphere_volume(-1)

        self.assertEqual(str(context.exception), "Negative values are not allowed.")

    ##################################################
    #  Cube Volume Test Case Implementation
    ##################################################
    def test_calculate_cube_volume(self):
        self.assertEqual(self.volume.calculate_cube_volume(3), 27)
        self.assertEqual(self.volume.calculate_cube_volume(0.24), 0.0138)
        self.assertEqual(self.volume.calculate_cube_volume(98), 941192)

    def test_calculate_cube_volume_with_invalid_type_raises_error(self):
        with self.assertRaises(TypeError) as context:
            self.volume.calculate_cube_volume('3')

        self.assertEqual(str(context.exception), "'str' is not allowed, only integer or float")

    def test_calculate_cube_volume_with_negative_value_raises_error(self):
        with self.assertRaises(ValueError) as context:
            self.volume.calculate_cube_volume(-1)

        self.assertEqual(str(context.exception), "Negative values are not allowed.")
        
    ##################################################
    #  Cone Volume Test Case Implementation
    ##################################################
    def test_calculate_cone_volume(self):
        self.assertEqual(self.volume.calculate_cone_volume(2, 2), 8.3776)
        self.assertEqual(self.volume.calculate_cone_volume(0.98, 7.8), 7.8447)
        self.assertEqual(self.volume.calculate_cone_volume(12.4, 27.32), 4398.987)

    def test_calculate_cone_volume_with_invalid_type_raises_error(self):
        with self.assertRaises(TypeError) as context:
            self.volume.calculate_cone_volume({"key": "value"}, 1)

        self.assertEqual(str(context.exception), "'dict' is not allowed, only integer or float")

    def test_calculate_cone_volume_with_negative_value_raises_error(self):
        with self.assertRaises(ValueError) as context:
            self.volume.calculate_cone_volume(-1, 2)

        self.assertEqual(str(context.exception), "Negative values are not allowed.")

    ##################################################
    #  Rectangle Volume Test Case Implementation
    ##################################################
    def test_calculate_rectangle_volume(self):
        self.assertEqual(self.volume.calculate_rectangle_volume(2, 3, 4), 24)
        self.assertEqual(self.volume.calculate_rectangle_volume(1.92, 9.38, 2.5), 45.024)
        self.assertEqual(self.volume.calculate_rectangle_volume(134, 928, 292), 36310784)

    def test_calculate_rectangle_volume_with_invalid_type_raises_error(self):
        with self.assertRaises(TypeError) as context:
            self.volume.calculate_rectangle_volume(2, 3, ['list'])

        self.assertEqual(str(context.exception), "'list' is not allowed, only integer or float")

    def test_calculate_rectangle_volume_with_negative_value_raises_error(self):
        with self.assertRaises(ValueError) as context:
            self.volume.calculate_rectangle_volume(2, 3, -1)
        
        self.assertEqual(str(context.exception), "Negative values are not allowed.")

    ##################################################
    #  Spherical Cap Volume Test Case Implementation
    ##################################################
    def test_calculate_spherical_cap_volume(self):
        self.assertEqual(self.volume.calculate_spherical_cap_volume(2, 2), 16.7552)
        self.assertEqual(self.volume.calculate_spherical_cap_volume(32.8, 23.9), 43825.4018)
        self.assertEqual(self.volume.calculate_spherical_cap_volume(3.65, 2.9), 70.454)

    def test_calculate_spherical_cap_volume_with_invalid_type_raises_error(self):
        with self.assertRaises(TypeError) as context:
            self.volume.calculate_spherical_cap_volume(2, (2, 2))

        self.assertEqual(str(context.exception), "'tuple' is not allowed, only integer or float")

    def test_calculate_spherical_cap_volume_with_negative_value_raises_error(self):
        with self.assertRaises(ValueError) as context:
            self.volume.calculate_spherical_cap_volume(2, -2)

        self.assertEqual(str(context.exception), "Negative values are not allowed.")

    ##################################################
    #  Capsule Volume Test Case Implementation
    ##################################################
    def test_calculate_capsule_volume(self):
        self.assertEqual(self.volume.calculate_capsule_volume(2, 2), 58.6431)
        self.assertEqual(self.volume.calculate_capsule_volume(0.98, 2.9), 12.6923)
        self.assertEqual(self.volume.calculate_capsule_volume(83.202, 98), 4543920.0419)

    def test_calculate_capsule_volume_with_invalid_type_raises_error(self):
        with self.assertRaises(TypeError) as context:
            self.volume.calculate_capsule_volume(2, 'carnival')
        
        self.assertEqual(str(context.exception), "'str' is not allowed, only integer or float")

    def test_calculate_capsule_volume_with_negative_value_raises_error(self):
        with self.assertRaises(ValueError) as context:
            self.volume.calculate_capsule_volume(2, -1)

        self.assertEqual(str(context.exception), "Negative values are not allowed.")

    ##################################################
    #  Ellipsoid Volume Test Case Implementation
    ##################################################
    def test_calculate_ellipsoid_volume(self):
        self.assertEqual(self.volume.calculate_ellipsoid_volume(2, 22, 12), 2211.6812)
        self.assertEqual(self.volume.calculate_ellipsoid_volume(1.32, 3, 0.2), 3.3175)
        self.assertEqual(self.volume.calculate_ellipsoid_volume(2.32, 1.02, 0.22), 2.1807)

    def test_calculate_ellipsoid_volume_with_invalid_type_raises_error(self):
        with self.assertRaises(TypeError) as context:
            self.volume.calculate_ellipsoid_volume(2, 2, 'evea')

        self.assertEqual(str(context.exception), "'str' is not allowed, only integer or float")

    def test_calculate_ellipsoid_volume_with_negative_value_raises_error(self):
        with self.assertRaises(ValueError) as context:
            self.volume.calculate_ellipsoid_volume(2, 2, -1)

        self.assertEqual(str(context.exception), "Negative values are not allowed.")


if __name__ == "__main__":
    unittest.main()
