Source Example
==============

quadrilaterals provides functions for describing a quadrilateral defined by a list of four side lengths and a list of four angles.

Determining Quadrilateral Type
^^^^^^^^^^^^^^^^^^^^^^^^^

The function :func:`source.quadrilaterals.get_quadrilateral_type` provides users with a way to provide a set of four sides and angles
of a quadrilateral and returns the type of quadrilateral ("square", "rectangle", "rhombus", "kite", "trapezoid", "parallelogram", or "disconnected" )

Examples
^^^^^^^^

>>> from source.quadrilaterals import get_quadrilateral_type
>>> polygon_square = {'sides': [2, 2, 2, 2], 'angles': [90, 90, 90, 90]}
>>> get_quadrilateral_type(polygon_square)
'square'
>>> polygon_kite = {'sides': [1, 2.732, 2.732, 1], 'angles': [120, 30, 120, 90]}
>>> get_quadrilateral_type(polygon_kite)
'kite'



Module Reference
^^^^^^^^^^^^^^^^

.. automodule:: source.quadrilaterals
    :members: