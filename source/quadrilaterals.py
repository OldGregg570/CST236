"""
:mod:`source.source1` -- Example source code
============================================

The following example code determines if a set of 3 sides of a triangle is equilateral, scalene or iscoceles
"""
from source.Turtle import Turtle

def get_quadrilateral_type(side_lengths, angles):
    """
    Determine if the given quadrilateral

    :param side_lengths:    list or tuple of side lengths
    :type side_lengths:     tuplse or list

    :param angles:          list or tuple of angles
    :type side_lengths:     tuple or list

    :return: "square", "rectangle", "rhombus", "disconnected" or "invalid"
    :rtype: str
    """

    if not (isinstance(side_lengths, (tuple, list)) and len(side_lengths) == 4):
        return "invalid"

    for n in side_lengths:
        if n <= 0:
            return "invalid"

    angle_sum = sum (angles);
    if angle_sum != 360:
        return "disconnected"

    is_normal = all(89.9 < a < 90.1 for a in angles)

    is_homogenous = all(a == side_lengths[0] for a in side_lengths)

    is_parallelogram = ((angles[0] == angles[2]) and
                        (angles[1] == angles[3]))

    is_length_equiopposite = ((side_lengths[0] == side_lengths[2]) and
                              (side_lengths[1] == side_lengths[3]))

    is_angle_equiopposite = ((angles[0] == angles[2]) or
                             (angles[1] == angles[3]))

    is_length_equiadjacent = (((side_lengths[0] == side_lengths[1]) and
                               (side_lengths[2] == side_lengths[3])) or
                              ((side_lengths[1] == side_lengths[2]) and
                               (side_lengths[3] == side_lengths[0])))


    ret_val = 'unhandled exception'

    if is_parallelogram:
        if is_normal:
            if is_homogenous:
                ret_val = "square"
            elif is_length_equiopposite:
                ret_val = "rectangle"
        elif is_length_equiopposite:
            ret_val = "rhombus"
    else:
        if is_angle_equiopposite and is_length_equiadjacent:
            ret_val = "kite"
        else:
            ret_val = "trapezoid"

    if Turtle.is_connected(side_lengths, angles):
        return ret_val
    else:
        return "disconnected"