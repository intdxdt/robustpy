import unittest
from compress import compress

class TestRobustCompress(unittest.TestCase):
    def test_compress(self):
        self.assertEqual(compress((0.,)), (0.,))
        self.assertEqual(compress((1.,)), (1.,))

suite = unittest.TestLoader().loadTestsFromTestCase(TestRobustCompress)
unittest.TextTestRunner(verbosity=4).run(suite)
