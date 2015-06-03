from unittest import TestCase
from Tracer import Tracer


class TestTracer(TestCase):
    def test_get_turtle_position(self):
        """
        unless otherwise specified, the tracer's initial position shall be (0.0, 0.0). This initial position is saved
        on the tracer's path list
        """
        tracer = Tracer()
        self.assertEqual((0.0, 0.0), tracer.position)
        self.assertEqual([(0.0, 0.0)], tracer.path)
        pass

    def test_get_turtle_position(self):
        """
        the tracer will provide methods to get the current position of the turtle
        """
        tracer = Tracer()
        tracer.trace(1, 90)
        self.assertEqual((0.0, 1.0), tracer.position)
        pass

    def test_trace_turtle(self):
        """
        the tracer will provide a method to move and turn the turtle and push the resulting position to a list
        """
        tracer = Tracer()
        tracer.trace(1, 90)
        self.assertEqual([(0.0, 0.0), (0.0, 1.0)], tracer.path)
        pass

    def test_trace_nosave(self):
        """
        the tracer will provide a method to move and turn the turtle without pushing the resulting position to a list
        """
        tracer = Tracer()
        tracer.tracer(1, 90, save=False)
        self.assertEqual([(0.0, 0.0)], tracer.path)
        pass

    def test_tracer_reset(self):
        """
        the tracer will provide a method to reinitialize at a specified position
        """
        tracer = Tracer()
        tracer.trace(1, 90)
        tracer.trace(1, 90)
        tracer.reset((1.0, 1.0))
        self.assertEqual([(1.0, 1.0)], tracer.path)
        pass

    def test_tracer_get_path(self):
        """
        the tracer will provide a method to return the path that has been traced as a list of points
        """
        tracer = Tracer()
        tracer.trace(1, 90)
        self.assertEqual([(0.0, 0.0), (0.0, 1.0)], tracer.path)
        pass

    def test_tracer_list_input(self):
        """
        the tracer will provide a way to pass in a set of move commands
        """
        tracer = Tracer()
        tracer.trace([(1, 90), (1, 45)])
        self.assertEqual([(0.0, 0.0), (0.0, 1.0), (-1.0, 1.0)], tracer.path)
        pass

    def test_tracer_is_closed(self):
        """
        the tracer will provide a static method that will determine if a path is closed
        """
        self.assertTrue(Tracer.is_closed([(1, 90), (1, 90), (1, 90), (1, 90)]))
        self.assertFalse(Tracer.is_closed([(1, 90), (1, 90), (1, 90), (2, 90)]))
        pass