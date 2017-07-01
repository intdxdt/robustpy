import math
import unittest
from random import random
from robust_scale import robust_scale
from two_product import two_product


class TestRobustScale(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(robust_scale([4], 2), (8,))
        self.assertEqual(robust_scale([1, 1e64], 2), (2, 2e64))
        self.assertEqual(robust_scale([1], 1), (1,))
        s = robust_scale([-2.4707339790384e-144, -1.6401064715739963e-142, 2e-126], -10e-64)
        self.assertTrue(s[-1] < 0)

        for i in range(-50, 50):
            for j in range(-50, 50):
                self.assertEqual(robust_scale([i], j), (i * j,))


suite = unittest.TestLoader().loadTestsFromTestCase(TestRobustScale)
unittest.TextTestRunner(verbosity=4).run(suite)
