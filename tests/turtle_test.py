from unittest import TestCase
from Turtle import Turtle


class TestTurtleTrace(TestCase):
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

    def test_absolute_translate(self):
        """
        the turtle will provide a method to translate it to an absolute position
        """
        self.assertEqual((5, 5), Turtle().translate_to((5, 5)).position)

    def test_relative_translate(self):
        """
        the turtle will provide a method to translate it by a relative distance
        """
        self.assertEqual((7, 7), Turtle().translate_to((5, 5)).translate_by((2, 2)).position)

