import math
import unittest
from rprod import robust_product as product


class TestRobustProduct(unittest.TestCase):
    def test_product(self):
        def pow2(n):
            return math.pow(2, n)

        for i in range(-20, 20 + 1):
            for j in range(-20, 20 + 1):
                fi, fj = float(i), float(j)
                self.assertEqual(product([fi], [fj]), (fi * fj,))

        self.assertEqual(
            product(
                [pow2(-50), pow2(50)],
                [pow2(-50), pow2(50)]
            ),
            (pow2(-100), pow2(1), pow2(100))
        )


suite = unittest.TestLoader().loadTestsFromTestCase(TestRobustProduct)
unittest.TextTestRunner(verbosity=4).run(suite)
