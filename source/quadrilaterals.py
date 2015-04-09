"""
:module source.quadrilaterals

methods to determine properties about a quadrilateral defined by a list
of side lengths and a list of angles.
"""
from source.Turtle import Turtle
from source.Polygon import Polygon

# map to a static method in the Turtle class
is_connected = Turtle.is_connected

f_equal = Polygon.f_equal


# TODO: Move to parent Shape class
def _is_normal(shape):
    """
    Returns true if all angles in list are normal

    :param shape: the shape
    :return: boolean
    """
    return all(f_equal(a, 90.0) for a in shape['angles'])


def _is_convex(shape):
    """
    Returns true if all angles are either positive or negative

    :param shape: the shape
    :return: boolean
    """
    angles = shape['angles']
    return all(a >= 180.0 for a in angles) or all(a <= 180.0 for a in angles)


def _is_homogenous(shape):
    """
    Returns true if all side lengths are the same

    :param shape: the shape
    :return: boolean
    """
    lengths = shape['sides']
    return f_equal(max(lengths), min(lengths))


def _is_parallelogram(shape):
    """
    Returns true if opposite angles are equal

    :param shape: the shape
    :return: boolean
    """
    angles = shape['angles']
    return (f_equal(angles[0], angles[2]) and
            f_equal(angles[1], angles[3]))


def _is_length_equiopposite(shape):
    """
    Returns true if opposite side lengths are equal

    :param shape: the shape
    :return: boolean
    """
    sides = shape['sides']
    return (f_equal(sides[0], sides[2]) and
            f_equal(sides[1], sides[3]))


def _is_length_equiadjacent(shape):
    """
    Returns true if there exist two pairs of adjacent sides that are equal (kitelike)

    :param shape: the shape
    :return: boolean
    """
    sides = shape['sides']
    return ((f_equal(sides[0], sides[1]) and f_equal(sides[2], sides[3])) or
            (f_equal(sides[1], sides[2]) and f_equal(sides[3], sides[0])))


def _is_disconnected(shape):
    """
    Returns true if the path created by the side lengths and angles does not end at the same
    point at which it started.

    :param shape: the shape
    :return: boolean
    """
    return not is_connected(shape)


def get_quadrilateral_type(shape):
    """
    Determines the class of a quadrilateral defined by its sides and angles.

    An even more in depth classification tree:
        www.cut-the-knot.org/Curriculum/Geometry/quadrilaterals1.gif

    :param lengths:    list or tuple of side lengths
    :type lengths:     tuple or list

    :param angles:     list or tuple of angles
    :type lengths:     tuple or list

    :return: "concave", "disconnected", "square", "rectangle", "rhombus" or Error
    :rtype: str
    """
    lengths = shape['sides']
    if not isinstance(lengths, (tuple, list)):
        return 'Error: lengths must be list or tuple'
    if not len(lengths) == 4:
        return 'Error: invalid number of sides'
    if not all([n > 0 for n in lengths]):
        return 'Error: all side lengths must be > 0'

    if not _is_convex(shape):
        return 'concave'

    if _is_disconnected(shape):
        return 'disconnected'

    ret_val = 'Error: unhandled exception'

    is_homogenous = _is_homogenous(shape)
    is_length_equiopposite = _is_length_equiopposite(shape)

    if _is_parallelogram(shape):
        if _is_normal(shape):
            if is_homogenous:
                ret_val = "square"
            elif is_length_equiopposite:
                ret_val = "rectangle"
        elif is_length_equiopposite:
            if is_homogenous:
                ret_val = "rhombus"
            else:
                ret_val = "parallelogram"
    else:
        if _is_length_equiadjacent(shape):
            ret_val = "kite"
        else:
            ret_val = "trapezoid"

    return ret_val