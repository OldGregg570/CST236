"""
:module source.Turtle

Virtual turtle 'graphics' drawer. Essentially converts a list
of lengths and angles into a list of cartesian points.

Keeps track of current direction the turtle is facing. When the turtle
takes a step, it moves some distance in its current direction
"""
import math
from source.Polygon import Polygon

f_equal = Polygon.f_equal

DEG_TO_RAD = Polygon.DEG_TO_RAD

class Turtle ():
    """
    Turtle tracer. Traces a series of distances and angles in order to
    produce a list of (x, y) coordinates
    """
    def __init__(self):
        """ Initialize this Turtle to the origin and to be facing East"""
        self._x, self._y = 0.0, 0.0
        self._angle = Polygon.DIR_EAST

    def _move(self, distance):
        """
        Move forward the specified distance
        :param distance: The distance to move
        """
        self._x += (math.cos(self._angle * DEG_TO_RAD) * distance)
        self._y += (math.sin(self._angle * DEG_TO_RAD) * distance)

    def _turn(self, angle):
        """
        Turn by the specified angle where 90 is left
        :param angle: The angle to turn by
        """
        self._angle += angle

    def step(self, distance, angle):
        """
        Move by the specified distance and turn by the specified angle
        :param distance: The distance to move forward
        :param angle: The angle to turn after moving
        :return:
        """
        self._move(distance)
        self._turn(180.0 - angle)

    def get_position(self):
        """
        Return the current turtle (x, y) position
        :return: A tuple, the 2D coordinate
        """
        return self._x, self._y

    def walk_shape(self, shape):
        """
        Walk an entire shape and return the end position of the turtle
        :param shape: The shape to walk
        :return: The end point of the walk
        """
        for pair in zip(shape['sides'], shape['angles']):
            self.step(pair[0], pair[1])
        return self.get_position()

    @staticmethod
    def is_connected(shape):
        """
        Walks the shape and returns true if the end point is (0, 0)
        :param shape:
        :return:
        """
        x, y = Turtle().walk_shape(shape)
        return f_equal(x, 0.0) and f_equal(y, 0.0)