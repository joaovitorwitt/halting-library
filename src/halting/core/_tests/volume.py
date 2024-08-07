##################################################
# Imports
##################################################
import unittest
from unittest import TestCase

from src.halting.core.volume import Volume

##################################################
# Volume Class Test Case Implementation
##################################################
class VolumeTestCase(TestCase):
    
    def setUp(self) -> None:
        self.volume = Volume()
        return super().setUp()
    

    def test_get_cylinder_volume(self):
        self.assertEqual(self.volume.get_cylinder_volume(2, 2), 25.13)
        self.assertEqual(self.volume.get_cylinder_volume(598, 21), 828494.53)
        self.assertEqual(self.volume.get_cylinder_volume(0.0298, 0.876), 0.07)
        self.assertEqual(self.volume.get_cylinder_volume(0.0298, 0.876, 4), 0.0718)
        self.assertEqual(self.volume.get_cylinder_volume(0.0298, 0.876, 10), 0.0718413276)


    def test_get_sphere_volume(self):
        self.assertEqual(self.volume.get_sphere_volume(2), 33.51)
        self.assertEqual(self.volume.get_sphere_volume(0.39), 0.25)
        self.assertEqual(self.volume.get_sphere_volume(323, 4), 141154970.7279)
        self.assertEqual(self.volume.get_sphere_volume(323, 10), 141154970.72787648)


    def test_get_cube_volumee(self):
        self.assertEqual(self.volume.get_cube_volume(3), 27)
        self.assertEqual(self.volume.get_cube_volume(0.24), 0.01)
        self.assertEqual(self.volume.get_cube_volume(98), 941192)
        self.assertEqual(self.volume.get_cube_volume(98, 3), 941192)
        self.assertEqual(self.volume.get_cube_volume(98.9, 10),  967361.6690000001)

        
    def test_get_cone_volume(self):
        self.assertEqual(self.volume.get_cone_volume(2, 2), 8.38)
        self.assertEqual(self.volume.get_cone_volume(0.98, 7.8), 7.84)
        self.assertEqual(self.volume.get_cone_volume(12.4, 27.32), 4398.99)
        self.assertEqual(self.volume.get_cone_volume(12.4, 27.32, 10), 4398.9870482947)


    def test_calculate_rectangle_volume(self):
        self.assertEqual(self.volume.calculate_rectangle_volume(2, 3, 4), 24)
        self.assertEqual(self.volume.calculate_rectangle_volume(1.92, 9.38, 2.5), 45.024)
        self.assertEqual(self.volume.calculate_rectangle_volume(134, 928, 292), 36310784)


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
