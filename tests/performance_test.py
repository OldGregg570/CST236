from Tracer import Tracer
from Surface import Surface
import sys
import time

ops = 0


def draw_path_and_save(path):
    global ops
    r = Surface((800, 800))

    for i in range(len(path) - 1):
        start = path [i]
        end = path[i + 1]
        r.line(start, end)
        ops += 1

    r.save('./performance_test.png')


def squiggly_test():
    global ops
    t = Tracer()
    start = time.time()
    for x in range(int(sys.argv[1])):
        for y in range(16):
            for z in range(8):
                for n in range(z):
                    t.trace(4, x)
                for n in range (y):
                    t.trace(4, y)
                for n in range(x):
                    t.trace(4, z)

    draw_path_and_save(t.path)
    end = time.time()

    print "Draw iterations: " + str(sys.argv[1])
    print "Draw operations: " + str(ops)
    print "Time elapsed:    " + str(end - start) + " seconds"


squiggly_test()