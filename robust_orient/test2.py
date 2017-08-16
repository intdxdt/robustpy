import json
import math
from robust_orient import orientation2d

NX = 512
NY = 512

def naiveLeftRight(a, b, c):
    abx = c[0] - a[0]
    aby = c[1] - a[1]
    acx = b[0] - a[0]
    acy = b[1] - a[1]
    return abx * acy - aby * acx


def plotPredicate(pred, out):
    res = []
    for i in xrange(0, NX):
        for j in xrange(0, NY):
            px = 0.5 + i * math.pow(2, -53)
            py = 0.5 + j * math.pow(2, -53)

            o = pred([px, py], [12, 12], [24, 24])
            res.append(o)
    print "len or arr = ", len(res)
    fid = open(out, 'w')
    fid.write("module.exports=" + json.dumps(res) + "\n")


if __name__ == '__main__':
    # plotPredicate(naiveLeftRight, 'pynaive.js')
    # plotPredicate(orientation2d, 'pyrobust.js')

    a = (237, 289)
    b = (404.25, 357.25)
    c = (460, 380)

    # c = (548.533232040746, 416.127910832771)
    print naiveLeftRight(a, b, c)
    print orientation2d(a, b, c)
    # ln = LineString([a, b])
    # print ln.intersects(Point(c))
    # print ln.distance(Point(c))
