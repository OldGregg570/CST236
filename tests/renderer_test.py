from unittest import TestCase
from Renderer import Renderer


class TestRenderer(TestCase):
    def test_construct_no_args(self):
        """
        creating a renderer with no arguments creates a 256x256px image with a white background.
        """
        r = Renderer()
        r.save('./test_construct_no_args.png')

    def test_draw_line(self):
        """
        the renderer should be able to draw an X from corner to corner
        """
        r = Renderer()
        r.line((0, 0), (255, 255))
        r.line((0, 255), (255, 0))
        r.save('./test_draw_line.png')