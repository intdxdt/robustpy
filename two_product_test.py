import math
import unittest
from random import random
from two_product import two_product

testValues = [
    0, 1,
    math.pow(2, -52),
    math.pow(2, -53),
    1.0 - math.pow(2, -53),
    1.0 + math.pow(2, -52),
    math.pow(2, -500),
    math.pow(2, 500),
    2, 0.5, 3, 1.5, 0.1, 0.3, 0.7]

for i in xrange(0, 20):
    testValues.append(random())
    testValues.append(random() * math.pow(2, 1000 * random() - 500))

for i in range(len(testValues) - 1, 0, -1):
    testValues.append(-testValues[i])


class TestTwoProduct(unittest.TestCase):
    def test_product(self):
        self.assertEqual(
            two_product(1.0 + math.pow(2, -52), 1.0 + math.pow(2, -52)),
            (math.pow(2, -104), 1.0 + math.pow(2, -51))
        )

        for j in range(0, len(testValues)):
            a = testValues[j]
            self.assertTrue(a * a < float('inf'))
            self.assertEqual(two_product(0, a), (0, 0))
            self.assertEqual(two_product(1, a), (0, a))
            self.assertEqual(two_product(-1, a), (0, -a))


suite = unittest.TestLoader().loadTestsFromTestCase(TestTwoProduct)
unittest.TextTestRunner(verbosity=4).run(suite)
