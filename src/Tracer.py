from Turtle import Turtle


class Tracer(object):
    """
    Path Tracer object. Uses a Turtle object to track a path and adds a list to save each point along the way
    """
    def __init__(self, position=(0.0, 0.0)):
        self.__turtle = Turtle(position)
        self.__path = [self.__turtle.position]

    @property
    def position(self):
        return self.__turtle.position

    @property
    def path(self):
        return self.__path

    def trace(self, distance, angle, save=True):
        """
        Move by the distance parameter in the current direction, rotate clockwise by the angle parameter, and save the
        resulting position to the path list.
        :param distance: The distance to move.
        :param angle: The angle to turn after moving.
        :param save: if False, the move will not be saved. (Default: True)
        :return:
        """
        self.__turtle.move(distance)
        self.__turtle.rotate(angle)
        if save:
            self.__path.append(self.position)
