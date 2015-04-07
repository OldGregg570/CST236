"""
Test for source.source1
"""
from source.quadrilaterals import get_quadrilateral_type

from unittest import TestCase

SQUARE = ([4, 4, 4, 4],
          [90, 90, 90, 90])

RECTANGLE = ([4, 6, 4, 6],
             [90, 90, 90, 90])

RHOMBUS = ([6, 4, 6, 4],
           [80, 100, 80, 100])

KITE = ([1, 2.732, 2.732, 1],
        [120, 30, 120, 90])


class TestGetQuadType(TestCase):
    def test_quadrilateral_square(self):
        result = get_quadrilateral_type(SQUARE[0], SQUARE[1])
        self.assertEqual(result, 'square')

    def test_quadrilateral_rect(self):
        result = get_quadrilateral_type(RECTANGLE[0], RECTANGLE[1])
        self.assertEqual(result, 'rectangle')

    def test_quadrilateral_rhombus(self):
        result = get_quadrilateral_type(RHOMBUS[0], RHOMBUS[1])
        self.assertEqual(result, 'rhombus')

    def test_quadrilateral_kite(self):
        result = get_quadrilateral_type(KITE[0], KITE[1])
        self.assertEqual(result, 'kite')
