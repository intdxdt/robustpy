import math
import unittest
from robust_sum import robust_sum

class TestRobustSum(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(robust_sum([1, 64], [-1e-64, 1e64]), (-1e-64, 65, 1e64))
        self.assertEqual(robust_sum([0], [0]), (0,))
        self.assertEqual(robust_sum([0], [1]), (1,))
        self.assertEqual(robust_sum([1, 1e64], [1e-64, 2]), (1e-64, 3, 1e64))
        self.assertEqual(robust_sum([1], [1e-64, 1e-16]), (1e-64, 1e-16, 1))

        self.assertEqual(robust_sum([0], [1]), (1,))

        for i in xrange(-10, 10 + 1):
            for j in xrange(-10, 10 + 1):
                self.assertEqual(robust_sum([i], [j]), (i + j,))


        # t.ok(validate(robust_sum([ 5.711861227349496e-133, 1e-116 ], [ 5.711861227349496e-133, 1e-116 ])))

        nois   = [0]*10
        expect = [0]*10
        for i in xrange(0 ,10):
            nois[i]   = math.pow(2, -1000+53*i)
            expect[i] = math.pow(2, -999+53*i)

        x = robust_sum(nois, nois)
        self.assertEqual(x, tuple(expect))
        # t.ok(validate(x))

        self.assertEqual(robust_sum([0], [1, 1e64]), (1, 1e64))

        # var s = [0]
        # for(var i=0; i<1000; ++i) {
        # s = robust_sum(s, [Math.random() * Math.pow(2, Math.random()*1800-900)])
        # t.ok(validate(s))
        # }


suite = unittest.TestLoader().loadTestsFromTestCase(TestRobustSum)
unittest.TextTestRunner(verbosity=4).run(suite)
