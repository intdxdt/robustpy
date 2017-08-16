import unittest
from pnp import robust_pt_in_polygon as inside


class TestRobustPnP(unittest.TestCase):
    def test_pnp(self):
        polygon = [[1, 1], [1, 2], [2, 2], [2, 1]]
        self.assertEqual(inside(polygon, [1.5, 1.5]), -1)
        self.assertEqual(inside(polygon, [1.2, 1.9]), -1)
        self.assertEqual(inside(polygon, [0, 1.9]), 1)
        self.assertEqual(inside(polygon, [1.5, 2]), 0)
        self.assertEqual(inside(polygon, [1.5, 2.2]), 1)
        self.assertEqual(inside(polygon, [3, 5]), 1)
        self.assertEqual(inside(polygon, [1.5, 2]), 0)

        polygon = [[-1, -1], [1, -1], [1, 1], [-1, 1]]
        for j in xrange(0, 3):
            self.assertEqual(inside(polygon, [0, 0]), -1)
            subdiv = []
            for i in xrange(0, len(polygon)):
                a = polygon[i]
                b = polygon[(i + 1) % len(polygon)]
                c = [0.5 * (a[0] + b[0]), 0.5 * (a[1] + b[1])]
                subdiv.extend([a, c])
                self.assertEqual(inside(polygon, polygon[i]), 0)
                self.assertEqual(inside(polygon, c), 0)

            self.assertEqual(inside(polygon, [1e10, 1e10]), 1)
            polygon = subdiv


suite = unittest.TestLoader().loadTestsFromTestCase(TestRobustPnP)
unittest.TextTestRunner(verbosity=2).run(suite)
