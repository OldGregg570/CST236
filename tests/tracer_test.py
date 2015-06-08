from unittest import TestCase
from Tracer import Tracer


class TestTracer(TestCase):
    def assertListOfPointsAlmostEqual(self, left, right):
        for p1, p2 in zip(left, right):
            self.assertAlmostEqual(p1[0], p2[0], 3)
            self.assertAlmostEqual(p1[1], p2[1], 3)

    def test_get_turtle_position(self):
        """
        unless otherwise specified, the tracer's initial position shall be (0.0, 0.0). This initial position is saved
        on the tracer's path list
        """
        tracer = Tracer()
        self.assertEqual((0.0, 0.0), tracer.position)
        self.assertEqual([(0.0, 0.0)], tracer.path)

    def test_get_turtle_position(self):
        """
        the tracer will provide methods to get the current position of the turtle
        """
        tracer = Tracer()
        tracer.trace(1, 90)
        self.assertEqual((1.0, 0.0), tracer.position)

    def test_trace_turtle(self):
        """
        the tracer will provide a method to move and turn the turtle and push the resulting position to a list
        """
        tracer = Tracer()
        tracer.trace(1, 90)
        self.assertEqual([(0.0, 0.0), (1.0, 0.0)], tracer.path)

    def test_trace_nosave(self):
        """
        the tracer will provide a method to move and turn the turtle without pushing the resulting position to a list
        """
        tracer = Tracer()
        tracer.trace(1, 90, save=False)
        self.assertEqual([(0.0, 0.0)], tracer.path)

    def test_tracer_get_path(self):
        """
        the tracer will provide a method to return the path that has been traced as a list of points
        """
        tracer = Tracer()
        tracer.trace(1.0, 180.0)
        tracer.trace(1.0, 180.0)
        self.assertListOfPointsAlmostEqual(tracer.path, [(0.0, 0.0), (1.0, 0.0), (0.0, 0.0)])