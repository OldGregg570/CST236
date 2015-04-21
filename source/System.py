class City():
    """
    A city specified by its name, distance from the main city, and connection speed
    """
    def __init__(self, name, distance, speed):
        self.__name = name
        self.__distance = distance
        self.__speed = speed
    @property
    def city(self):
        return self.__name

    @property
    def distance(self):
        return self.__distance

    @property
    def speed(self):
        return self.__speed


class SpeedBenchmarkSystem():
    """
    Class to benchmark city speed data
    """
    def __init__(self, filepath=None, cities=[], hd_size=2000):
        self.__cities = cities
        self.__speed_estimate = 0
        self.__network_speed = 300
        self.__hd_size = hd_size
        self.__speed_relative_description = 'general'

        if filepath:
                f = open(filepath, 'r')
                for line in f:
                    split = line.split()
                    self.__cities.append(City(split[0], split[1], split[2]))

        pass

    def add_city(self, city):
        """
        Add a new city and write its data to the file
        """
        self.__cities.append(city)
        self.rewrite_file()

    def set_speed_estimate(self, estimate, relative='general'):
        """
        Set the system's speed estimate
        """
        self.__speed_estimate = estimate
        self.__speed_relative_description = relative

    def network_is_faster(self):
        """
        Return true if the network is faster than the provided speed input
        """
        return self.__speed_estimate < self.__network_speed

    @property
    def cities(self):
        return self.__cities

    @property
    def hd_size(self):
        return self.__hd_size

    def get_best_path(self, city, speed, hd_size):
        """
        Returns true if the network is faster. Returns false if the HD is.
        """
        return self.network_is_faster()

    def get_speed_diff(self, city, speed, hd_size):
        """
        Return the speed difference between the HD and the network
        """
        return abs(speed - self.__speed_estimate)

    def rewrite_file(self):
        """
        Rewrtie the entire save file
        """
        pass