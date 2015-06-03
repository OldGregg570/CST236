import math

DEG_TO_RAD = (2 * math.pi / 360.0)


class Turtle(object):
    """
    Turtle class. Defines methods to track position and a facing direction. The turtle can be rotated and moved in the
    current direction.
    """
    def __init__(self, position=(0.0, 0.0)):
        self.__angle = 0
        self.__position = position

    @property
    def x(self):
        return self.__position[0]

    @property
    def y(self):
        return self.__position[1]

    @property
    def angle(self):
        return self.__angle

    @angle.setter
    def angle(self, angle):
        self.__angle = angle % 360

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        self.__position = position

    def rotate(self, angle):
        """
        Rotate the turtle by the provided angle ammount
        :param angle: the angle to rotate by (clockwise)
        :return: self
        """
        self.angle += angle
        return self

    def move(self, distance):
        """
        Move the turtle by the provided distance. Turtle is to move in the direction of self.angle where 0 is East
        :param distance: the distance to move by
        :return: self
        """
        self.position = (self.__position[0] + (math.cos(self.__angle * DEG_TO_RAD) * distance),
                         self.__position[1] + (math.sin(self.__angle * DEG_TO_RAD) * distance))
        return self