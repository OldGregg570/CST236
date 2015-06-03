from unittest import TestCase
from Turtle import Turtle


class TestTurtle(TestCase):
    def test_angles_positive(self):
        """
        the turtle will provide methods to get and set an angle. The angle value in the range of [0, 360)
        """
        turtle = Turtle()
        turtle.angle = 20
        self.assertEqual(20, turtle.angle)

    def test_angles_overflow(self):
        turtle = Turtle()
        turtle.angle = 370
        self.assertEqual(10, turtle.angle)

    def test_angles_negative(self):
        turtle = Turtle()
        turtle.angle = -30
        self.assertEqual(330, turtle.angle)

    def test_angles_zero(self):
        turtle = Turtle()
        turtle.angle = 0
        self.assertEqual(0, turtle.angle)

    def test_angles_threesixty(self):
        turtle = Turtle()
        turtle.angle = 360
        self.assertEqual(0, turtle.angle)

    def test_relative_rotate(self):
        """
        the turtle will provide a method to rotate it by a relative angle
        """
        self.assertEqual(120, Turtle().rotate(30).rotate(90).angle)

    def test_relative_move(self):
        """
        the turtle will provide a method to move it forward a specified distance
        """
        self.assertEqual((7.0, 7.0), Turtle((0.0, 7.0)).move(7).position)


class TestTurtleMove(TestCase):
    def test_move_directions(self):
        """
        the turtle should be able to move in all directions on the cartesian plane
        """
        C = 2**0.5 / 2  # sqrt(2)/2
        directions = [45, 135, 225, 315]
        positions = [(C, C), (-C, C), (-C, -C), (C, -C)]

        for pos, dir in zip(positions, directions):
            t = Turtle()
            t.angle = dir
            t.move(1)
            self.assertAlmostEqual(pos[0], t.x, 3)
            self.assertAlmostEqual(pos[1], t.y, 3)

    def test_square_walk(self):
        t = Turtle()
        for n in range(4):
            t.move(1)
            t.rotate(90)

        self.assertAlmostEqual(0, t.x, 3)
        self.assertAlmostEqual(0, t.y, 3)