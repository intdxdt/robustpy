import gc
import sys
import time
from rblsi import rbinters
from cases import cases
from brute_force import intersectBruteForce

if sys.platform == 'win32':
    # On Windows, the best timer is time.clock
    default_timer = time.clock
else:
    # On most other platforms the best timer is time.time
    default_timer = time.time

NUM_ITER = 100
WARM_UP = 10

implementations = [
    dict(name="Brute-force", algo=intersectBruteForce),
    dict(name="RBLSI", algo=rbinters)
]


def benchmark(red, blue, algo):
    for i in range(0, WARM_UP):
        algo(red, blue)

    start = default_timer()
    count = 0
    for i in range(0, NUM_ITER):
        result = algo(red, blue)
        count += len(result)
    end = default_timer()
    return [((end - start) *1000) / NUM_ITER, count]


for i in range(0, len(implementations)):
    impl = implementations[i]
    print "testing", impl['name'], "...\n"
    for j in range(0, len(cases)):
        print "case:", cases[j]['name']
        gcold = gc.isenabled()
        gc.disable()
        try:
            res = benchmark(cases[j]['red'], cases[j]['blue'], impl['algo'])
        finally:
            if gcold: gc.enable()
        print "\ttime:", res[0], "ms - total isect:", res[1]
