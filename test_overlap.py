from dbits import exponent, fraction, denormalized
from twiddle import count_trailing_zeros, log2


def tz(f):
    if f[0] != 0:
        return count_trailing_zeros(f[0])
    elif f[1] != 0:
        return 32 + count_trailing_zeros(f[1])
    return 0


def lz(f):
    if f[1] != 0:
        return 20 - (log2(f[1]))
    elif f[0] != 0:
        return 52 - (log2(f[0]))
    return 52


def lo(n):
    e = exponent(n)
    f = fraction(n)
    z = tz(f)
    return e - (52 - z)


def hi(n):
    if denormalized(n):
        return -(1023 + lz(fraction(n)))
    return exponent(n)


def test_overlap(a, b):
    if abs(b) > abs(a):
        a, b = b, a

    if a == 0.0 or b == 0.0:
        return False

    a0 = hi(a)
    a1 = lo(a)
    b0 = hi(b)
    b1 = lo(b)
    # [a1------a0]
    #     [b1-----b0]
    # ----------------
    #    [a1-------a0]
    # [b1-------b0]
    return (b1 <= a0) and (a1 <= b0)
