import unittest
from random import random

from bench.cases import cases
from bench.brute_force import intersectBruteForce
from bench.rblsi import rbinters

brutal = intersectBruteForce
rblsi = rbinters


class TestTestCases(unittest.TestCase):
    def test_fuzz(self):
        print '\n\n'
        for j in range(0, 10):
            red = []
            for i in range(0, 10 * (j + 1)):
                red.append([
                    [random(), random()],
                    [random(), random()]
                ])

            blue = []
            for i in range(0, 10 * (j + 1)):
                blue.append([
                    [random(), random()],
                    [random(), random()]
                ])
            expected = brutal(red, blue)
            expected.sort()

            actual = rblsi(red, blue)
            actual.sort()
            self.assertEqual(actual, expected, msg="fuzz test")


suite = unittest.TestLoader().loadTestsFromTestCase(TestTestCases)
unittest.TextTestRunner(verbosity=4).run(suite)
