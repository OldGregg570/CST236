from unittest import TestCase
from ReqTracer import requirements
from Turtle import Turtle


class TestTurtleTrace(TestCase):
    turtle = Turtle()
    @requirements(['#000000'])
    def test_absolute_rotate(self):
        """
        the turtle will provide a method to rotate it to an absolute angle
        """
        #self.turtle.rotate_to(90)
        #self.assertEqual(90, self.turtle.angle)
        pass

    @requirements(['#000001'])
    def test_relative_rotate(self):
        """
        the turtle will provide a method to rotate it by a relative angle
        """
        #00self.turtle.rotate_by()
        pass

    @requirements(['#000002'])
    def test_absolute_translate(self):
        """
        the turtle will provide a method to translate it to an absolute position
        """
        pass

    @requirements(['#000003'])
    def tesT_relative_translate(self):
        """
        the turtle will provide a method to translate it by a relative distance
        """
        pass

    @requirements(['#000004'])
    def test_pen_raise(self):
        """
        the turtle will provide a method to toggle whether a path is drawn on the next move
        """
        pass


class TestGeometrySolve(TestCase):
    @requirements(['#001000'])
    def test_geometry_connected(self):
        """
        the turtle will provide a method to return whether a path is "connected" or "disconnected"
        """
        pass

    @requirements(['#001001'])
    def test_geometry_concavity(self):
        """
        the turtle will provide a method to return whether a path is "concave" or "convex"
        """
        pass

    @requirements(['#001002'])
    def test_geometry_intersecting(self):
        """
        the turtle will provide a method to return whether a path is "simple" or "complex"
        """
        pass

    @requirements(['#001003'])
    def test_polyline_length(self):
        """
        the turtle will provide a method to return the length of the polyline
        """
        pass


class TestBale(TestCase):
    @requirements(['#002000'])
    def test_turtle_multi(self):
        """
        the system will be able to track multiple turtles to produce an aggregate path
        """
        pass

    @requirements(['#002001'])
    def test_turtle_split(self):
        """
        the system will provide a way to split the current turtle into two or more turtles with different initial orientations
        """
        pass


class TestRender(TestCase):
    @requirements(['#003000'])
    def test_render_canvas(self):
        """
        the turtle renderer will allow the path stored in the turtle to be output graphically to a canvas
        """
        pass

    @requirements(['#003001'])
    def test_render_bitmap(self):
        """
        the turtle renderer will allow the path stored in the turtle to be output graphically to a bitmap
        """
        pass

    @requirements(['#003002'])
    def test_render_line_weight(self):
        """
        the turtle renderer will allow a line weight to be specified as a float value [0.0, 1.0]
        """
        pass

    @requirements(['#003004'])
    def test_render_line_color(self):
        """
        #000014 the turtle renderer will allow a line color to be specified as a string or a hex value (#00RRGGBB)
        """
        pass


class TestErrorHandling(TestCase):

    @requirements(['#004000'])
    def test_error_invalid_input(self):
        """
        #000015 the turtle will raise an exception if an invalid angle or distance is input
        """
        pass

    @requirements(['#004001'])
    def test_error_invalid_graphic_out(self):
        """
        #000016 the turtle will raise an exception if an invalid graphic output option is chosen
        """
        pass

    @requirements(['#004002'])
    def test_error_position_bounds(self):
        """
        #000017 the turtle will raise an exception if an input moves a turtle out of range [RANGE_MIN, RANGE_MAX]
        """
        pass


class TestConfiguration(TestCase):

    @requirements(['#005000'])
    def test_config_angle_units(self):
        """
        the turtle can be configured to accept degree values or radian values. If no unit is specified during configuration, the turtle will interpret angle values in degrees by default
        """
        pass