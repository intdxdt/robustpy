import unittest
from rubust_orient import orientation2d, orientation3d

class TestRobustOrient(unittest.TestCase):
    def test_orient_2d(self):
        self.assertEqual(orientation2d([0.1, 0.1], [0.1, 0.1], [0.3, 0.7]), 0)
        self.assertTrue(orientation2d([0, 0], [-1e-64, 0], [0, 1]) > 0)

        self.assertEqual(orientation2d([0, 0], [1e-64, 1e-64], [1, 1]), 0)
        self.assertTrue(orientation2d([0, 0], [1e-64, 0], [0, 1]) < 0)

        x = 1e-64
        for i in xrange(0, 200):
            self.assertTrue(orientation2d([-x, 0], [0, 1], [x, 0]) > 0)
            self.assertEqual(orientation2d([-x, 0], [0, 0], [x, 0]), 0)
            self.assertTrue(orientation2d([-x, 0], [0, -1], [x, 0]) < 0)
            self.assertTrue(orientation2d([0, 1], [0, 0], [x, x]) < 0)
            x *= 10

    def test_orient_3d(self):
        self.assertTrue(orientation3d([0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1]) < 0)
        self.assertTrue(orientation3d([0, 0, 0], [1, 0, 0], [0, 0, 1], [0, 1, 0]) > 0)
        self.assertTrue(orientation3d([0, 0, 0], [1e-64, 0, 0], [0, 0, 1], [0, 1e64, 0]) > 0)


suite = unittest.TestLoader().loadTestsFromTestCase(TestRobustOrient)
unittest.TextTestRunner(verbosity=4).run(suite)
