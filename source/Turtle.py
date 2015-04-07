import math
FLOAT_THRESHOLD = 0.1
DEG_TO_RAD = (2 * math.pi / 360.0)

class Turtle ():
    def __init__(self):
        self._x = 0.0
        self._y = 0.0
        self._angle = 0.0 #East

    def move(self, distance):
        self._x += (math.cos(self._angle * DEG_TO_RAD) * distance)
        self._y += (math.sin(self._angle * DEG_TO_RAD) * distance)

    def turn(self, angle):
        self._angle += angle

    def step(self, distance, angle):
        self.move(distance)
        self.turn(180.0 - angle)

    def get_position(self):
        return (self._x, self._y)

    def walk_shape(self, lengths, angles):
        for pair in zip(lengths, angles):
            self.step(pair[0], pair[1])
        return self.get_position()

    @staticmethod
    def is_connected(lengths, angles):
        p = Turtle().walk_shape(lengths, angles)
        return -FLOAT_THRESHOLD < p[0] < FLOAT_THRESHOLD and -FLOAT_THRESHOLD < p[1] < FLOAT_THRESHOLD

