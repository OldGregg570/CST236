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

    def test_absolute_rotate(self):
        """
        the turtle will provide a method to rotate it to an absolute angle
        """
        self.assertEqual(90, Turtle().rotate_to(90).angle)

    def test_relative_rotate(self):
        """
        the turtle will provide a method to rotate it by a relative angle
        """
        self.assertEqual(120, Turtle().rotate_to(30).rotate_by(90).angle)

    def test_absolute_move(self):
        """
        the turtle will provide a method to move it to an absolute position
        """
        self.assertEqual((5, 5), Turtle().move_to((5, 5)).position)

    def test_relative_translate(self):
        """
        the turtle will provide a method to move it forward a specified distance
        """
        self.assertEqual((7.0, 7.0), Turtle((0.0, 7.0)).move(7).position)
