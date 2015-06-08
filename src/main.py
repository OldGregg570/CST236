from Tracer import Tracer
from Surface import Surface

def draw_path_and_save(path):
    r = Surface((800, 800))

    for i in range(len(path) - 1):
        start = path [i]
        end = path[i + 1]
        r.line(start, end)

    r.save('./performance_test.png')

def performance_tests():
    t = Tracer()
    for x in range (200):
        for y in range(200):
            for z in range(200):
                t.trace(2, 90)
                t.trace(2, 90)
                t.trace(2, 90)
                t.trace(2, 90)

    draw_path_and_save(t.path)


performance_tests()