import math

class Orc():
    def __init__(self, name='', pos=(0, 0), dest=(0, 0), speed=1):
        self._name = name
        self._position = pos
        self._destination = dest
        self._speed = speed
        pass

    @property
    def position(self):
        return self._position

    @property
    def destination(self):
        return self._destination

    @property
    def name(self):
        return self._name


    def get_distance(self):
        x = self._destination[0] - self._position[0]
        y = self._destination[1] - self._position[1]
        return math.sqrt(x**2 + y**2)


    def get_velocity(self):
        x = self._destination[0] - self._position[0]
        y = self._destination[1] - self._position[1]

        if x == 0:
            return (0, self._speed)
        if y == 0:
            return (self._speed, 0)
        else:
            angle = math.atan(y / x)
            dx = self._speed * math.cos(angle)
            dy = self._speed * math.sin(angle)
            return (dx, dy)


class OrcCommander(Orc):
    def __init__(self, name='', pos=(0, 0), dest=(0, 0), speed=1, rank=0):
        name = 'Commander ' + name
        Orc.__init__(self, name, pos, dest, speed)
        self._rank = rank

    @property
    def rank(self):
        return self._rank