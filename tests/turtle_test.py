from unittest import TestCase
from Turtle import Turtle


class TestTurtleTrace(TestCase):
    turtle = Turtle()
    def test_absolute_rotate(self):
        """
        the turtle will provide a method to rotate it to an absolute angle
        """
        self.turtle.rotate_to(90)
        self.assertEqual(90, self.turtle.angle)
        pass

    def test_relative_rotate(self):
        """
        the turtle will provide a method to rotate it by a relative angle
        """
        self.turtle.rotate_to(30).rotate_by(90)
        self.assertEqual(120, self.turtle.angle)
        pass

    def test_absolute_translate(self):
        """
        the turtle will provide a method to translate it to an absolute position
        """
        self.turtle.translate_to((5, 5))
        self.assertEqual((5, 5), self.turtle.position)
        pass

    def tesT_relative_translate(self):
        """
        the turtle will provide a method to translate it by a relative distance
        """
        self.turtle.translate_to((5, 5)).translate_by((2, 2))
        self.assertEqual((7, 7), self.turtle.position)
        pass