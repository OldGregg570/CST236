"""
:mod: source.Polygon

Polygon abstract class. Polygons are defined by a
list of sides and a list of angles
"""
import math


class Polygon ():
    """
    :class: Polygon

    Polygon base class
    """
    FLOAT_THRESHOLD = 0.1

    # angle of a  3-4-5 triangle
    ANGLE_THREE_FOUR_FIVE = 36.86
    FLOAT_PRECISION = 2
    DEG_TO_RAD = (2 * math.pi / 360.0)
    DIR_EAST = 0.0

    def __init__(self):
        pass

    @staticmethod
    def f_equal(a, b, t=FLOAT_THRESHOLD):
        """
        Determines if two numbers are equal within the threshold
        :param a: first number
        :param b: second number
        :param t: threshold
        :return: boolean
        """
        return round(abs(a - b), max(2, len(str(t)) - 2)) <= t
