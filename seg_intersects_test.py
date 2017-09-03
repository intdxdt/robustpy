import unittest
from seg_intersects import segment_intersects as crosses


class TestRobustSegIntersect(unittest.TestCase):
    def test_seg_intersect(self):
        self.assertTrue(crosses([-1, 0], [1, 0], [0, -1], [0, 1]))  # general test
        self.assertFalse(crosses([0.5, 0], [1, 0], [0, -1], [0, 1]))
        self.assertTrue(crosses([0, 0], [1, 0], [0, -1], [0, 1]))
        self.assertTrue(crosses([0, 0], [100000000000000020000, 1e-12], [1, 0], [1e20, 1e-11]))
        self.assertFalse(crosses([0, 0], [1e20, 1e-11], [1, 0], [100000000000000020000, 1e-12]))

        self.assertFalse(crosses([0, 1], [0, 2], [0, -1], [0, -2]))  # collinear, no intersect
        self.assertTrue(crosses([0, 1], [0, 2], [0, 1.5], [0, -2]))  # collinear, intersect

        self.assertTrue(crosses([0, 1], [0, 2], [0, 1], [0, -2]))  # collinear, endpoint touch
        self.assertTrue(crosses([0, 1], [0, -1], [0, 0], [0, 1]))  # endpoint touches


suite = unittest.TestLoader().loadTestsFromTestCase(TestRobustSegIntersect)
unittest.TextTestRunner(verbosity=4).run(suite)
