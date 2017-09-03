import unittest
from det import det2
from random import random
from  rsum import robust_sum as rsum
from compare import robust_compare as cmp
from rprod import robust_product as rprod
from subtract import robust_subtract as rsub
from validate import validate_sequence as validate
from seg_intersection import segment_intersection as seg_intersection


def rnd():
    return random()


class TestRobustSegIntersection(unittest.TestCase):
    def test_seg_intersect(self):
        # | a[0]  a[1]  1 |
        # | b[0]  b[1]  1 |
        # |  x     y    w |

        def test_pt_seq(a, b, x, y, w):
            d0 = rsum([a[1]], [-b[1]])
            d1 = rsum([a[0]], [-b[0]])
            d2 = det2([[a[0], a[1]], [b[0], b[1]]])

            # validate det.RobustDet2
            self.assertTrue(validate(d2))

            p0 = rprod(x, d0)
            p1 = rprod(y, d1)
            p2 = rprod(w, d2)
            # validate p0
            self.assertTrue(validate(p0))
            # validate p1
            self.assertTrue(validate(p1))
            # validate p2
            self.assertTrue(validate(p2))

            s = rsum(rsub(p0, p1), p2)
            # validate s
            self.assertTrue(validate(s))
            # check point on line
            self.assertTrue(cmp(s, (0.,)) == 0.)

        def verify(a, b, c, d):
            x = seg_intersection(a, b, c, d)
            # validate x
            self.assertTrue(validate(x[0]))
            # validate y
            self.assertTrue(validate(x[1]))
            # validate w
            self.assertTrue(validate(x[2]))
            test_pt_seq(a, b, x[0], x[1], x[2])
            test_pt_seq(c, d, x[0], x[1], x[2])

            p = ((a, b), (c, d))
            for s in range(0, 2):
                for r in range(0, 2):
                    for h in range(0, 2):
                        y = seg_intersection(p[h][s], p[h][s ^ 1], p[h ^ 1][r], p[h ^ 1][r ^ 1])
                        # validate x
                        self.assertTrue(validate(y[0]))
                        # validate y
                        self.assertTrue(validate(y[1]))
                        # validate w
                        self.assertTrue(validate(y[2]))
                        # check x
                        self.assertTrue(cmp(rprod(y[0], x[2]), rprod(x[0], y[2])) == 0.)
                        # check y
                        self.assertTrue(cmp(rprod(y[1], x[2]), rprod(x[1], y[2])) == 0.)

        for _ in range(0, 100):
            verify((rnd(), rnd()), (rnd(), rnd()), (rnd(), rnd()), (rnd(), rnd()))

        isect = seg_intersection((-1., 10.), (-10., 1.), (10., 0.), (10., 10.))
        # no intersections
        self.assertTrue(isect[2][0] == 0.)


suite = unittest.TestLoader().loadTestsFromTestCase(TestRobustSegIntersection)
unittest.TextTestRunner(verbosity=4).run(suite)
