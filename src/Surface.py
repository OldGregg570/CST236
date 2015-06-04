from PIL import Image, ImageDraw


class Surface(object):
    """
    Used to draw and save bitmap images.
    """
    def __init__(self, img_size=(64,64)):
        self.__image = Image.new('RGB', img_size, "#fff")
        self.__draw = ImageDraw.Draw(self.__image)
        self.__origin = self.__image.size[0] / 2,

    def save(self, path):
        """
        Save the drawn image to a file.
        :param path: the path and name of the file
        :return: None
        """
        self.__image.save(path, 'PNG')

    def line(self, start, finish, color="#000"):
        """
        Draw a line on the current bitmap surface offset by the origin
        :param start: Start point of the line
        :param finish: End point of the line
        :param color: Color of the line (Default: "#000")
        :return: None
        """
        self._line(self.__origin_transform(start), self.__origin_transform(finish), color)

    def _line(self, start, finish, color="#000"):
        """
        Draw a line on the current bitmap surface.
        :param start: Start point of the line
        :param finish: End point of the line
        :param color: Color of the line (Default: "#000")
        :return: None
        """
        self.__draw.line((start[0], start[1], finish[0], finish[1]), fill=color)

    def __origin_transform(self, point):
        """
        Transforms the
        :param point: point to transform
        :return: the transformed point as a 2-tuple
        """
        return (point[0] + self.__image.size[0] / 2,
                point[1] + self.__image.size[1] / 2)