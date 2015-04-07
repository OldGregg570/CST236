"""
Test for source.source1
"""
from source.triangles import get_triangle_type
from unittest import TestCase

class TestGetTriangleType(TestCase):
    def test_get_triangle_equilateral_all_int(self):
        result = get_triangle_type(1, 1, 1)
        self.assertEqual(result, 'equilateral')

    def test_get_triangle_scalene_all_int(self):
        result = get_triangle_type(1, 2, 3)
        self.assertEqual(result, 'scalene')

    def test_get_triangle_isosceles_all_int(self):
        result = get_triangle_type(1, 1, 2)
        self.assertEqual(result, 'isosceles')

    def test_get_triangle_tuple (self):
        result = get_triangle_type((1, 2, 3))
        self.assertEqual(result, 'scalene')

    def test_get_triangle_dict (self):
        result = get_triangle_type({"wall": 1, "floor": 2, "ladder": 3})
        self.assertEqual (result, 'scalene')

    def test_get_triangle_strings_invalid (self):
        result = get_triangle_type('wall', 'floor', 'ladder')
        self.assertEqual(result, "invalid")

        result = get_triangle_type(1, 'floor', 'ladder')
        self.assertEqual(result, "invalid")

        result = get_triangle_type(1, 1, 'ladder')
        self.assertEqual(result, "invalid")

    def test_get_triangle_negative_invalid (self):
        result = get_triangle_type (-1, 1, 1)
        self.assertEqual (result, "invalid")

        result = get_triangle_type (1, -1, 1)
        self.assertEqual (result, "invalid")

        result = get_triangle_type (1, 1, -1)
        self.assertEqual (result, "invalid")

    def test_get_triangle_zero_invalid (self):
        result = get_triangle_type (0, 1, 1)
        self.assertEqual (result, "invalid")

        result = get_triangle_type (1, 0, 1)
        self.assertEqual (result, "invalid")

        result = get_triangle_type (1, 1, 0)
        self.assertEqual (result, "invalid")

    def test_get_triangle_no_args (self):
        result = get_triangle_type ()
        self.assertEqual (result, "invalid")