"""
Test for source.source1
"""
from source.quadrilaterals import get_quadrilateral_type
from source.quadrilaterals import _is_normal
from source.quadrilaterals import _is_convex
from source.quadrilaterals import _is_disconnected
from source.quadrilaterals import _is_homogenous
from source.quadrilaterals import _is_length_equiadjacent
from source.quadrilaterals import _is_length_equiopposite
from source.quadrilaterals import _is_parallelogram

from unittest import TestCase

RT_2 = 2 ** (0.5)

SQUARE = {'sides': [4, 4, 4, 4], 'angles': [90, 90, 90, 90]}

RECTANGLE = {'sides': [4, 6, 4, 6], 'angles': [90, 90, 90, 90]}

RHOMBUS = {'sides': [4, 4, 4, 4], 'angles': [80, 100, 80, 100]}

KITE = {'sides': [1, 2.732, 2.732, 1], 'angles': [120, 30, 120, 90]}

PARALLELOGRAM = {'sides': [6, 4, 6, 4], 'angles': [60, 120, 60, 120]}

TRAPEZOID = {'sides': [4, RT_2, 2, RT_2], 'angles': [45, 135, 135, 45]}

BARELY_NORMAL = {'angles': [89.9, 90.1, 89.9, 90.1]}
NOT_NORMAL = {'angles': [89.9, 90.2, 89.9, 90.1]}

BARELY_HOMOGENOUS = {'sides': [2, 2, 2.1, 2], 'angles': [140, 140, 140, 140]}
NOT_HOMOGENOUS = {'sides': [1.9, 2, 2.1, 2], 'angles': [140, 140, 140, 140]}


CONCAVE = {'sides': [1, 1, 0.577, 0.577], 'angles': [60, 30, 240, 30]}

GENERIC_TRAPEZOID = {'sides': [1, 0.4, 0.535, 0.565], 'angles': [75, 110, 135, 50]}

DISCONNECTED = {'sides': [1, 2, 1, 1], 'angles': [90, 90, 90, 90]}


class TestPrivateHelpers(TestCase):
    def test_is_normal(self):
        self.assertTrue(_is_normal(SQUARE))
        self.assertTrue(_is_normal(RECTANGLE))
        self.assertTrue(_is_normal(BARELY_NORMAL))
        self.assertFalse(_is_normal(TRAPEZOID))
        self.assertFalse(_is_normal(NOT_NORMAL))

    def test_is_convex(self):
        self.assertTrue(_is_convex(SQUARE))
        self.assertTrue(_is_convex(KITE))
        self.assertTrue(_is_convex(RECTANGLE))
        self.assertTrue(_is_convex(RHOMBUS))
        self.assertTrue(_is_convex(PARALLELOGRAM))
        self.assertTrue(_is_convex(TRAPEZOID))
        self.assertFalse(_is_convex(CONCAVE))

    def test_is_homogeneous(self):

        self.assertTrue(_is_homogenous(SQUARE))
        self.assertTrue(_is_homogenous(BARELY_HOMOGENOUS))
        self.assertFalse(_is_homogenous(NOT_HOMOGENOUS))
        self.assertFalse(_is_homogenous(TRAPEZOID))

    def _is_parallelogram(self):
        self.assertTrue(_is_parallelogram(SQUARE))
        self.assertTrue(_is_parallelogram(RECTANGLE))
        self.assertTrue(_is_parallelogram(PARALLELOGRAM))
        self.assertTrue(_is_parallelogram(RHOMBUS))
        self.assertFalse(_is_parallelogram(KITE))
        self.assertFalse(_is_parallelogram(TRAPEZOID))

    def test_is_disconnected(self):
        self.assertFalse(_is_disconnected(KITE))
        self.assertFalse(_is_disconnected(RHOMBUS))
        self.assertFalse(_is_disconnected(SQUARE))
        self.assertFalse(_is_disconnected(RECTANGLE))
        self.assertFalse(_is_disconnected(TRAPEZOID))
        self.assertFalse(_is_disconnected(CONCAVE))
        self.assertTrue(_is_disconnected(DISCONNECTED))

    def test_is_length_equiopposite(self):
        self.assertTrue(_is_length_equiopposite(RECTANGLE))
        self.assertFalse(_is_length_equiopposite(GENERIC_TRAPEZOID))

    def test_is_length_equiadjacent(self):
        self.assertTrue(_is_length_equiadjacent(KITE))
        self.assertFalse(_is_length_equiadjacent(GENERIC_TRAPEZOID))

class TestGetQuadType(TestCase):
    def test_quadrilateral_type_passing(self):
        self.assertEqual(get_quadrilateral_type(SQUARE), 'square')
        self.assertEqual(get_quadrilateral_type(RECTANGLE), 'rectangle')
        self.assertEqual(get_quadrilateral_type(RHOMBUS), 'rhombus')
        self.assertEqual(get_quadrilateral_type(KITE), 'kite')
        self.assertEqual(get_quadrilateral_type(PARALLELOGRAM), 'parallelogram')
        self.assertEqual(get_quadrilateral_type(GENERIC_TRAPEZOID), 'trapezoid')
        self.assertEqual(get_quadrilateral_type(DISCONNECTED), 'disconnected')
        self.assertEqual(get_quadrilateral_type(CONCAVE), 'concave')

    def test_quadrilateral_type_errors(self):
        self.assertEqual(get_quadrilateral_type({'sides': 'not a list'}), 'Error: lengths must be list or tuple')
        self.assertEqual(get_quadrilateral_type({'sides': [2, 2, 2]}), 'Error: invalid number of sides')
        self.assertEqual(get_quadrilateral_type({'sides': [2, 2, 2, 2, 3]}), 'Error: invalid number of sides')
        self.assertEqual(get_quadrilateral_type({'sides': [-1, 2, 2, 2]}), 'Error: all side lengths must be > 0')
