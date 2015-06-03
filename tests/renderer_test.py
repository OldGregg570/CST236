from unittest import TestCase
from Renderer import Renderer
import autopy

RESULTS_DIR = './tests/results/'
EXPECTED_DIR = './tests/expected/'


class TestRenderer(TestCase):
    def assertImageEqualToExpected(self, f_name):
        expected = autopy.bitmap.Bitmap.open(EXPECTED_DIR + f_name)
        result = autopy.bitmap.Bitmap.open(RESULTS_DIR + f_name)
        self.assertEqual([(1, 1)], expected.find_every_bitmap(result))

    def test_construct_no_args(self):
        """
        creating a renderer with no arguments creates a 256x256px image with a white background.
        """
        img_name = 'test_construct_no_args.png'
        r = Renderer()
        r.save(RESULTS_DIR + img_name)
        self.assertImageEqualToExpected(img_name)

    def test_draw_line(self):
        """
        the renderer should be able to draw an X from corner to corner
        """
        img_name = 'test_draw_line.png'
        r = Renderer()
        r.line((0, 0), (64, 64))
        r.line((0, 64), (64, 0))
        r.save(RESULTS_DIR + img_name)
        self.assertImageEqualToExpected(img_name)

