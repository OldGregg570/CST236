from unittest import TestCase
from Drawable import Path
from Surface import Surface

RESULTS_DIR = './tests/results/'
EXPECTED_DIR = './tests/expected/'


class TestDrawables(TestCase):
    def test_constructor_noargs(self):
        """
        constructing a Path with no arguments should have an empty points list
        Path should have len overridden
        """
        self.assertEqual(len(Path()), 0)

    def test_constructor_withargs(self):
        """
        constructing a path with a list of points will initialize it with the point args
        """
        self.assertEqual(len(Path([(1, 1), (2, 2)])), 2)

    def test_path_add(self):
        """
        points can be added to the Path's list
        the add method will return a reference to the calling object so
        calls can be chained
        """
        self.assertEqual(len(Path().add((1, 1).add(2, 2))), 2)

    def test_path_draw(self):
        """
        testing a path around the edge of the surface
        """
        img_name = 'test_path_draw.png'
        s = Surface()

        Path([(28, 28), (-28, 28), (-28, -28), (28, -28)]).draw(s)
        s.save(RESULTS_DIR + img_name)
        self.assertImageEqualToExpected(img_name)