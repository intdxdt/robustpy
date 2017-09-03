import unittest
from twiddle import *


class TestTwiddle(unittest.TestCase):
    def test_not(self):
        self.assertEqual(~170, -171)
        self.assertEqual(~0, -1)
        self.assertEqual(~-3, 2)

    def test_sign(self):
        self.assertEqual(sign(-100), -1)
        self.assertEqual(sign(100), 1)
        self.assertEqual(sign(0), 0)
        self.assertEqual(sign(INT_MAX), 1)
        self.assertEqual(sign(INT_MIN), -1)

    def test_abs(self):
        self.assertEqual(abs(0), 0)
        self.assertEqual(abs(1), 1)
        self.assertEqual(abs(-1), 1)
        self.assertEqual(abs(INT_MAX), INT_MAX)
        self.assertEqual(abs(-INT_MAX), INT_MAX)
        # abs(-INT_MIN) -- overflow

    def test_min(self):
        self.assertEqual(min(0, 0), 0)
        self.assertEqual(min(-1, 1), -1)
        self.assertEqual(min(INT_MAX, INT_MAX), INT_MAX)
        self.assertEqual(min(INT_MIN, INT_MIN), INT_MIN)
        self.assertEqual(min(INT_MAX, INT_MIN), INT_MIN)

    def test_max(self):
        self.assertEqual(max(0, 0), 0)
        self.assertEqual(max(-1, 1), 1)
        self.assertEqual(max(INT_MAX, INT_MAX), INT_MAX)
        self.assertEqual(max(INT_MIN, INT_MIN), INT_MIN)
        self.assertEqual(max(INT_MAX, INT_MIN), INT_MAX)

    def test_is_pow2(self):
        self.assertTrue(not is_pow2(0))
        for i in range(0, 31):
            self.assertTrue(is_pow2((1 << i)))

        self.assertTrue(not is_pow2(100))
        self.assertTrue(not is_pow2(0x7fffffff))
        self.assertTrue(not is_pow2(-1000000))

    def test_log2(self):
        for i in range(0, 31):
            if i > 0:
                self.assertEqual(log2((1 << i) - 1), i - 1)
                self.assertEqual(log2((1 << i) + 1), i)

            self.assertEqual(log2((1 << i)), i)

    def test_log10(self):
        self.assertEqual(log10(1), 0)
        self.assertEqual(log10(10), 1)
        self.assertEqual(log10(100), 2)
        self.assertEqual(log10(1000), 3)
        self.assertEqual(log10(10000), 4)
        self.assertEqual(log10(100000), 5)
        self.assertEqual(log10(1234007), 6)
        self.assertEqual(log10(10004659), 7)
        self.assertEqual(log10(100046598), 8)
        self.assertEqual(log10(1000465983), 9)

    def test_pop_count(self):
        self.assertEqual(pop_count(0), 0)
        self.assertEqual(pop_count(1), 1)
        # self.assertEqual(pop_count(-1), 32)
        for i in range(0, 31):
            self.assertEqual(pop_count(1 << i), 1)
            self.assertEqual(pop_count((1 << i) - 1), i)

        self.assertEqual(pop_count(0xf0f00f0f), 16)  # overflow for i32

    def test_count_trailing_zeros(self):
        self.assertEqual(count_trailing_zeros(0), 32)
        self.assertEqual(count_trailing_zeros(1), 0)
        #    self.assertEqual(count_trailing_zeros(-1), 0)
        for i in range(0, 31):
            self.assertEqual(count_trailing_zeros(1 << i), i)
            if i > 0:
                self.assertEqual(count_trailing_zeros((1 << i) - 1), 0)

        self.assertEqual(count_trailing_zeros(0xf81700), 8)

    def test_next_pow2(self):
        for i in range(0, 31):
            if i != 1:
                self.assertEqual(next_pow2((1 << i) - 1), 1 << i)

            self.assertEqual(next_pow2((1 << i)), 1 << i)
            if i < 30:
                self.assertEqual(next_pow2((1 << i) + 1), 1 << (i + 1))

    def test_prev_pow2(self):
        # print("{i:>2}    {input:>w$}    {prev:>w$}", i = "i", input = "((1 << i) + 1)", prev = "prev_pow2", w = 10)
        print("{}\n".format("-" * 34))
        for i in range(0, 31):
            if i > 0:
                self.assertEqual(prev_pow2((1 << i) - 1), 1 << (i - 1))

            self.assertEqual(prev_pow2((1 << i)), 1 << i)

            if 0 < i < 30:
                # print("{i:>2} .. {input:>w$} .. {prev:>w$}", i = i, input = ((1 << i) + 1), prev = prev_pow2((1 << i) + 1), w = 10)
                self.assertEqual(prev_pow2((1 << i) + 1), 1 << i)

    def test_parity(self):
        self.assertEqual(parity(1), 1)
        self.assertEqual(parity(0), 0)
        self.assertEqual(parity(0xf), 0)
        self.assertEqual(parity(0x10f), 1)

    def test_reverse(self):
        self.assertEqual(reverse(0), 0)
        # self.assertEqual(reverse(-1), -1)

    def test_next_combination(self):
        self.assertEqual(next_combination(1), 2)
        self.assertEqual(next_combination(0x300), 0x401)

    def test_interleave2(self):
        for x in range(0, 100):
            for y in range(0, 100):
                h = interleave2(x, y)
                self.assertEqual(deinterleave2(h, 0), x)
                self.assertEqual(deinterleave2(h, 1), y)

    def test_interleave3(self):
        for x in range(0, (25 + 1)):
            for y in range(0, (25 + 1)):
                for z in range(0, (25 + 1)):
                    h = interleave3(x, y, z)
                    self.assertEqual(deinterleave3(h, 0), x)
                    self.assertEqual(deinterleave3(h, 1), y)
                    self.assertEqual(deinterleave3(h, 2), z)


suite = unittest.TestLoader().loadTestsFromTestCase(TestTwiddle)
unittest.TextTestRunner(verbosity=4).run(suite)
