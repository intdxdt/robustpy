import unittest
from validate import validate_sequence as validate

class TestValidate(unittest.TestCase):
    def test_sum(self):
        self.assertTrue( validate([1e-16, 1.]))
        self.assertTrue(not validate([0.5, 1.5]))
        self.assertTrue( validate([0.]))
        self.assertTrue(not validate([]))

suite = unittest.TestLoader().loadTestsFromTestCase(TestValidate)
unittest.TextTestRunner(verbosity=4).run(suite)
