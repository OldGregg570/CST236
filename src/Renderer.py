from PIL import Image, ImageDraw


class Renderer(object):
    """
    Used to draw and save bitmap images.
    """
    def __init__(self, img_size=(64,64)):
        self.__image = Image.new('RGB', img_size, "#fff")
        self.__draw = ImageDraw.Draw(self.__image)

    @property
    def size(self):
        return self.__image.size

    @property
    def middle(self):
        return self.size / 2

    def save(self, path):
        """
        Save the drawn image to a file.
        :param path: the path and name of the file
        :return: None
        """
        self.__image.save(path, 'PNG')

    def line(self, start, finish, color="#000"):
        """
        Draw a line on the current bitmap surface.
        :param start: Start point of the line
        :param finish: End point of the line
        :param color: Color of the line (Default: "#000")
        :return: None
        """
        self.__draw.line((start[0], start[1], finish[0], finish[1]), fill=color)