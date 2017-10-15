import unittest
from bench.cases import cases
from bench.brute_force import intersectBruteForce
from bench.rblsi import rbinters

brutal =  intersectBruteForce
rblsi = rbinters
class TestTestCases(unittest.TestCase):
    def test_cases(self):
        for testCase in cases :
            expected = brutal(testCase['red'], testCase['blue'])
            expected.sort()

            actual = rblsi(testCase['red'], testCase['blue'])
            actual.sort()
            self.assertEqual(actual, expected, msg=testCase['name'])

suite = unittest.TestLoader().loadTestsFromTestCase(TestTestCases)
unittest.TextTestRunner(verbosity=4).run(suite)