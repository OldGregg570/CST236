"""
Test for source.source1
"""
from source.triangles import get_triangle_type
from unittest import TestCase


class TestGetTriangleType(TestCase):
    def test_get_triangle_equilateral_all_int(self):
        self.assertEqual(get_triangle_type(1, 1, 1), 'equilateral')

    def test_get_triangle_scalene_all_int(self):
        self.assertEqual(get_triangle_type(1, 2, 3), 'scalene')

    def test_get_triangle_isosceles_all_int(self):
        self.assertEqual(get_triangle_type(1, 1, 2), 'isosceles')

    def test_get_triangle_tuple (self):
        self.assertEqual(get_triangle_type((1, 2, 3)), 'scalene')

    def test_get_triangle_dict (self):
        self.assertEqual(get_triangle_type({"wall": 1, "floor": 2, "ladder": 3}), 'scalene')

    def test_get_triangle_strings_invalid (self):
        self.assertEqual(get_triangle_type('wall', 'floor', 'ladder'), "invalid")
        self.assertEqual(get_triangle_type(1, 'floor', 'ladder'), "invalid")
        self.assertEqual(get_triangle_type(1, 1, 'ladder'), "invalid")

    def test_get_triangle_negative_invalid (self):
        self.assertEqual(get_triangle_type(-1, 1, 1), 'invalid')
        self.assertEqual(get_triangle_type(1, -1, 1), 'invalid')
        self.assertEqual(get_triangle_type(1, 1, -1), 'invalid')

    def test_get_triangle_zero_invalid (self):
        self.assertEqual(get_triangle_type(0, 1, 1), 'invalid')
        self.assertEqual(get_triangle_type(1, 0, 1), 'invalid')
        self.assertEqual(get_triangle_type(1, 1, 0), 'invalid')

    def test_get_triangle_no_args (self):
        self.assertEqual(get_triangle_type(), 'invalid')