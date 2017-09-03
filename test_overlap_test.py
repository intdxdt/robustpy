import math
import unittest
from test_overlap import test_overlap


class TestTestOverlap(unittest.TestCase):
    def test_float_overlap(self):
        self.assertTrue(test_overlap(1.5, 0.5))
        self.assertTrue(test_overlap(math.pow(2, -52), 1.0 + math.pow(2, -52)))
        self.assertTrue(not test_overlap(1.0, 0.5))

        # Test 0
        self.assertTrue(not test_overlap(0.0, 1.0))
        self.assertTrue(not test_overlap(0.0, 0.0))

        # test denormalized numbers
        # underflow - MIN_EXP == -1021

        self.assertTrue(not test_overlap(math.pow(2, -1024), math.pow(2., -1023)))
        self.assertTrue(not test_overlap(math.pow(2, -1023), math.pow(2, -1022)))
        self.assertTrue(test_overlap(math.pow(2, -1024) + math.pow(2, -1040), math.pow(2, -1030)))
        self.assertTrue(not test_overlap(math.pow(2, -1030) - math.pow(2, -1031), math.pow(2, -1030)))


suite = unittest.TestLoader().loadTestsFromTestCase(TestTestOverlap)
unittest.TextTestRunner(verbosity=4).run(suite)
