import unittest
from dbits import *


class TestDoubleBits(unittest.TestCase):
    def test_db(self):
        self.assertEqual(lo(1.0), 0)
        self.assertEqual(hi(1.0), 0x3ff00000)
        self.assertEqual(pack(0, 0x3ff00000), 1.0)
        self.assertEqual(db(1.0), (0, 0x3ff00000))
        print db(75.0)

        self.assertEqual(fraction(1.), (0, 1 << 20))
        self.assertEqual(exponent(1.), 0)
        self.assertEqual(sign(1.), 0)
        self.assertEqual(sign(-1.), 1)
        self.assertEqual(exponent(0.5), -1)

        self.assertTrue(denormalized(2.0 ** (-1024)))
        self.assertTrue(not denormalized(1.))
        self.assertTrue(denormalized(2.0 ** (-1023)))
        self.assertTrue(not denormalized(2.0 ** (-1022)))


suite = unittest.TestLoader().loadTestsFromTestCase(TestDoubleBits)
unittest.TextTestRunner(verbosity=4).run(suite)
