import unittest
import sys
import subprocess

from triangle_sort_2 import Triangle


class TestClassEnvelopeAnalysis(unittest.TestCase):
    def setUp(self):
        self.name = "name"
        self.a = 7.2
        self.b = 8.3
        self.c = 6.8
        self.square = 9.3

    def test_triangle_constructor(self):
        self.assertIsNotNone(Triangle(self.name, self.a, self.b, self.c))

    def test_wrong_side_type_error(self):
        self.assertRaises(TypeError, lambda: Triangle("str", True))
        self.assertRaises(TypeError, lambda: Triangle(9, "abc"))
        self.assertRaises(TypeError, lambda: Triangle(True, 5))
        self.assertRaises(TypeError, lambda: Triangle(False, 7.1))
        self.assertRaises(TypeError, lambda: Triangle(5, True))
        self.assertRaises(TypeError, lambda: Triangle(9.3, "bc"))
        self.assertRaises(TypeError, lambda: Triangle("qbc", 9.9))
        self.assertRaises(TypeError, lambda: Triangle(7, 8.1))
        self.assertRaises(TypeError, lambda: Triangle(5.0, 6))
        self.assertRaises(TypeError, lambda: Triangle(5, 5.0))

    def test_incorrect_value_sides_error(self):
        self.assertRaises(ValueError, lambda: Triangle("fe", 7.2, -2.9, 8.2))
        self.assertRaises(ValueError, lambda: Triangle("fw", -7.5, 6.2, 4.5))
        self.assertRaises(ValueError, lambda: Triangle("fq", 8.4, 8.3, -7.7))
        self.assertRaises(ValueError, lambda: Triangle("ft", -7.2, -2.9, 8.2))
        self.assertRaises(ValueError, lambda: Triangle("fy", -7.5, 6.2, -4.5))
        self.assertRaises(ValueError, lambda: Triangle("fu", 8.4, -8.3, -7.7))
        self.assertRaises(ValueError, lambda: Triangle("fj", -7.5, -6.2, -4.5))

    def test_area_calculating(self):
        triangle_obj = Triangle(self.name, self.a, self.b, self.c)
        result = triangle_obj.calculate_area()
        self.assertIsNotNone(result)

    def test_is_triangle_exists(self):
        self.assertFalse(Triangle.check_triangle(77.5, 6.2, 4.5))
        self.assertTrue(Triangle.check_triangle(77.2, 66.1, 44.2))
        self.assertFalse(Triangle.check_triangle(64.2, 1.2, 84.5))
        self.assertTrue(Triangle.check_triangle(12.3, 8.7, 10.8))
        self.assertFalse(Triangle.check_triangle(10.7, 84.2, 10.5))


if __name__ == '__main__':
    unittest.main()
    if '--unittest' in sys.argv:
        subprocess.call([sys.executable, '-m', 'unittest', 'discover'])
