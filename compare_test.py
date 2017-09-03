import unittest
from compare import robust_compare as compare


class TestRobustCompare(unittest.TestCase):
    def test_cmp(self):
        self.assertTrue(compare([5.], [1., 4.]) == 0.)
        self.assertTrue(compare([1e64], [-1e-100, 1e64]) > 0.)
        self.assertTrue(compare([1e64], [1e-100, 1e64]) < 0.)


suite = unittest.TestLoader().loadTestsFromTestCase(TestRobustCompare)
unittest.TextTestRunner(verbosity=4).run(suite)
