import math
import unittest
from random import random

from subtract import robust_subtract


class TestRobustDiff(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(robust_subtract([1], [1]), (0,))
        s = [0]
        for i in range(0, 100):
            s = robust_subtract(s, [random() * math.pow(2, random() * 1000)])
            # self.assertTrue(validate(s))


suite = unittest.TestLoader().loadTestsFromTestCase(TestRobustDiff)
unittest.TextTestRunner(verbosity=4).run(suite)
