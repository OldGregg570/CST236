"""
Test for source.Turtle.py
"""
from source.Turtle import Turtle
from unittest import TestCase
from source.Polygon import Polygon

ANGLE_THREE_FOUR_FIVE = Polygon.ANGLE_THREE_FOUR_FIVE
TRI_EQUILATERAL = {'sides': [2, 2, 2], 'angles': [60, 60, 60]}
PRECISION = Polygon.FLOAT_PRECISION


class TestTurtle (TestCase):
    def test_turtle_init(self):
        turtle = Turtle()
        x, y = turtle.get_position()
        self.assertAlmostEqual(x, 0.0)
        self.assertAlmostEqual(y, 0.0)
        self.assertAlmostEqual(turtle._angle, 0.0)

    def test_turtle_walk_ne(self):
        turtle = Turtle()
        turtle._turn(ANGLE_THREE_FOUR_FIVE)
        turtle._move(5)
        x, y = turtle.get_position()
        self.assertAlmostEqual(x, 4.0, PRECISION)
        self.assertAlmostEqual(y, 3.0, PRECISION)

    def test_turtle_walk_nw(self):
        turtle = Turtle()
        turtle._turn(ANGLE_THREE_FOUR_FIVE + 90)
        turtle._move(5)
        x, y = turtle.get_position()
        self.assertAlmostEqual(x, -3.0, PRECISION)
        self.assertAlmostEqual(y, 4.0, PRECISION)

    def test_turtle_walk_sw(self):
        turtle = Turtle()
        turtle._turn(ANGLE_THREE_FOUR_FIVE + 180)
        turtle._move(5)
        x, y = turtle.get_position()
        self.assertAlmostEqual(x, -4.0, PRECISION)
        self.assertAlmostEqual(y, -3.0, PRECISION)

    def test_turtle_walk_se(self):
        turtle = Turtle()
        turtle._turn(ANGLE_THREE_FOUR_FIVE + 270)
        turtle._move(5)
        x, y = turtle.get_position()
        self.assertAlmostEqual(x, 3.0, PRECISION)
        self.assertAlmostEqual(y, -4.0, PRECISION)

    def test_turtle_walk_round_trip(self):
        turtle = Turtle()
        turtle._turn(ANGLE_THREE_FOUR_FIVE)
        turtle._move(5)
        turtle._turn (180)
        turtle._move(5)
        x, y = turtle.get_position()
        self.assertAlmostEqual(x, 0.0, PRECISION)
        self.assertAlmostEqual(y, 0.0, PRECISION)

    def test_turtle_walk_square(self):
        turtle = Turtle()
        turtle._move(5)
        turtle._turn(90)
        x, y = turtle.get_position()
        self.assertAlmostEqual(x, 5.0, PRECISION)
        self.assertAlmostEqual(y, 0.0, PRECISION)
        turtle._move(5)
        turtle._turn(90)
        x, y = turtle.get_position()
        self.assertAlmostEqual(x, 5.0, PRECISION)
        self.assertAlmostEqual(y, 5.0, PRECISION)
        turtle._move(5)
        turtle._turn(90)
        x, y = turtle.get_position()
        self.assertAlmostEqual(x, 0.0, PRECISION)
        self.assertAlmostEqual(y, 5.0, PRECISION)
        turtle._move(5)
        turtle._turn(90)
        x, y = turtle.get_position()
        self.assertAlmostEqual(x, 0.0, PRECISION)
        self.assertAlmostEqual(y, 0.0, PRECISION)

    def test_turtle_is_connected_true(self):
        turtle = Turtle()
        self.assertTrue (turtle.is_connected(TRI_EQUILATERAL))

    def test_turtle_is_connected_false(self):
        turtle = Turtle()
        result = turtle.is_connected({'sides': [2, 2, 1], 'angles': [60, 60, 60]})
        self.assertFalse(result)

    def test_turtle_walk_equilateral_polygons(self):
        turtle = Turtle()
        expected = [180, 360, 540, 720, 900, 1080, 1260]
        def build_polygon_angle_series (k):
            return map(lambda n: (n - 2) * 180, range(3, k))

        self.assertListEqual(expected, build_polygon_angle_series(10))
        n = 3
        for angle_sum in build_polygon_angle_series(12):
            a = angle_sum / n
            polygon = {'sides': [1] * n, 'angles': [a] * n}
            self.assertTrue(turtle.is_connected(polygon))
            n += 1
