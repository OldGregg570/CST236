
class Turtle(object):
    def __init__(self):
        self.__angle = 0
        self.__position = (0, 0)
        pass

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
        self.position = position

    def rotate_to(self, angle):
        self.angle = angle
        return self

    def rotate_by(self, rhs):
        self.angle += rhs
        return self

    def translate_to(self, position):
        self.__position = position
        return self

    def translate_by(self, rhs):
        self.__position = (self.position[0] + rhs[0], self.position[1] + rhs[1])
        return self