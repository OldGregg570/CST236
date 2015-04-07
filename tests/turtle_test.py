"""
Test for source.Turtle.py
"""
from source.Turtle import Turtle
from unittest import TestCase

ANGLE_THREE_FOUR_FIVE = 36.86

class TestTurtle (TestCase):
    def test_turtle_init(self):
        turtle = Turtle()
        pos = turtle.get_position()
        self.assertAlmostEqual(pos[0], (0.0, 0.0)[0])
        self.assertAlmostEqual(pos[1], (0.0, 0.0)[1])
        self.assertAlmostEqual(turtle._angle, 0.0)

    def test_turtle_walk_ne(self):
        turtle = Turtle()
        turtle.turn(ANGLE_THREE_FOUR_FIVE)             # angle of a  3-4-5 triangle
        turtle.move(5)
        pos = turtle.get_position()
        self.assertAlmostEqual(pos[0], (4.0, 3.0)[0], 2)
        self.assertAlmostEqual(pos[1], (4.0, 3.0)[1], 2)

    def test_turtle_walk_nw(self):
        turtle = Turtle()
        turtle.turn(ANGLE_THREE_FOUR_FIVE + 90)
        turtle.move(5)
        pos = turtle.get_position()
        self.assertAlmostEqual(pos[0], (-3.0, 4.0)[0], 2)
        self.assertAlmostEqual(pos[1], (-3.0, 4.0)[1], 2)

    def test_turtle_walk_sw(self):
        turtle = Turtle()
        turtle.turn(ANGLE_THREE_FOUR_FIVE + 180)
        turtle.move(5)
        pos = turtle.get_position()
        self.assertAlmostEqual(pos[0], (-4.0, -3.0)[0], 2)
        self.assertAlmostEqual(pos[1], (-4.0, -3.0)[1], 2)

    def test_turtle_walk_se(self):
        turtle = Turtle()
        turtle.turn(ANGLE_THREE_FOUR_FIVE + 270)
        turtle.move(5)
        pos = turtle.get_position()
        self.assertAlmostEqual(pos[0], (3.0, -4.0)[0], 2)
        self.assertAlmostEqual(pos[1], (3.0, -4.0)[1], 2)

    def test_turtle_walk_round_trip(self):
        turtle = Turtle()
        turtle.turn(ANGLE_THREE_FOUR_FIVE)
        turtle.move(5)
        turtle.turn (180)
        turtle.move(5)
        pos = turtle.get_position()
        self.assertAlmostEqual(pos[0], (0.0, 0.0)[0], 2)
        self.assertAlmostEqual(pos[1], (0.0, 0.0)[1], 2)

    def test_turtle_walk_square(self):
        turtle = Turtle()
        turtle.move(5)
        turtle.turn(90)
        pos = turtle.get_position()
        self.assertAlmostEqual(pos[0], (5.0, 0.0)[0], 2)
        self.assertAlmostEqual(pos[1], (5.0, 0.0)[1], 2)
        turtle.move(5)
        turtle.turn(90)
        pos = turtle.get_position()
        self.assertAlmostEqual(pos[0], (5.0, 5.0)[0], 2)
        self.assertAlmostEqual(pos[1], (5.0, 5.0)[1], 2)
        turtle.move(5)
        turtle.turn(90)
        pos = turtle.get_position()
        self.assertAlmostEqual(pos[0], (0.0, 5.0)[0], 2)
        self.assertAlmostEqual(pos[1], (0.0, 5.0)[1], 2)
        turtle.move(5)
        turtle.turn(90)
        pos = turtle.get_position()
        self.assertAlmostEqual(pos[0], (0.0, 0.0)[0], 2)
        self.assertAlmostEqual(pos[1], (0.0, 0.0)[1], 2)

    def test_turtle_is_connected_true(self):
        turtle = Turtle()
        result = turtle.is_connected([2,2,2], [60,60,60])

    def test_turtle_is_connected_false(self):
        turtle = Turtle()
        result = turtle.is_connected([2,2,1], [60,60,60])
        self.assertFalse(result)


'''
Make    Spoiler Doors
P       R1      2
P       R2      4
P       R3      5
P       N       5
B       R1      2
B       R2      4
B       R3      5
B       N       4
A       R1      2
A       R2      4
A       R3      5
A       N       2
M       R1      2
M       R2      4
M       R3      5
M       N       4
V       R1      2
V       R2      4
V       R3      5
V       N       5
'''