import unittest
from det import det2, det3


class TestRobustDet(unittest.TestCase):
    def test_det(self):
        self.assertEqual(det3((
            (1., 2., 3.),
            (3., 4., 5.),
            (6., 7., 8.),
        )), (0.,))
        self.assertEqual(det2((
            (1., 2.),
            (3., 4.),
        )), (-2.,))
        self.assertEqual(det3((
            (1., 2., 3.),
            (3., 4., 5.),
            (6., 7., 8.),
        )), (0.,))
        self.assertEqual(det2((
            (1., 2.),
            (3., 4.),
        )), (-2.,))


suite = unittest.TestLoader().loadTestsFromTestCase(TestRobustDet)
unittest.TextTestRunner(verbosity=4).run(suite)
