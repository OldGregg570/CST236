Turtle Draw
===========

A python turtle graphics painting library.


Usage
=====
    from Tracer import Tracer
    from Surface import Surface
    
    t = Tracer()
    r = Surface()
    
    # Trace a square
    t.trace(10, 90)
    t.trace(10, 90)
    t.trace(10, 90)
    t.trace(10, 90)
    
    # Render the path
    for i in range(len(path) - 1):
        start = path [i]
        end = path[i + 1]
        r.line(start, end)
    
    
    # Output the rendering
    r.save('./output_file.png')


This allows you to override the line drawing method with whatever you want.
You can draw colored lines, dotted lines, or even sine or zigzagged lines.
