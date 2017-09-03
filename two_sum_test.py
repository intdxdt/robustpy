import unittest
from two_sum import two_sum


class TestTwoSum(unittest.TestCase):
    def test_sum(self):
        self.assertEqual (two_sum(1e+64, 1) , (1.0, 1e+64))
        self.assertEqual (two_sum(1, 1) , (0, 2))
        self.assertEqual (two_sum(0, -1415) , (0, -1415))
        self.assertEqual (two_sum(1e-64, 1e64) , (1e-64, 1e64))
        self.assertEqual (two_sum(0, 0) , (0, 0))
        self.assertEqual (two_sum(9e15 + 1, 9e15) , (1, 18000000000000000))

suite = unittest.TestLoader().loadTestsFromTestCase(TestTwoSum)
unittest.TextTestRunner(verbosity=4).run(suite)
