"""
Test for source.Polygon
"""
from source.Polygon import Polygon
from unittest import TestCase

f_equal = Polygon.f_equal


class TestStaticMethods(TestCase):
    def test_f_equal_off_by_one(self):
        self.assertTrue(f_equal(10, 9, 1))
        self.assertFalse(f_equal(10, 9, 0.9))
        self.assertTrue(f_equal(10000, 9999, 1))
        self.assertFalse(f_equal(10000, 9998.9, 1))

    def test_f_equal_actually_equal(self):
        self.assertTrue(f_equal(10, 10, 2))

    def test_f_equal_off_by_tenth(self):
        self.assertTrue(f_equal(1.0, 1.1, 0.1))
        self.assertFalse(f_equal(1.0, 1.11, 0.1))

    def test_f_equal_off_by_hundredth(self):
        self.assertTrue(f_equal(0.05, 0.051))
        self.assertTrue(f_equal(0.05, 0.051, 0.001))

    def test_f_equal_long(self):
        self.assertTrue(f_equal(1.001, 1.002, 0.01))
        self.assertTrue(f_equal(1.001, 1.002, 0.001))
        self.assertFalse(f_equal(1.001, 1.002, 0.0001))
