import math

SPLITTER = math.pow(2, 27) + 1.0


def two_product(a, b):
    """
    two product
    :param a:
    :param b:
    :return:
    """
    x = a * b

    c = SPLITTER * a
    abig = c - a
    ahi = c - abig
    alo = a - ahi

    d = SPLITTER * b
    bbig = d - b
    bhi = d - bbig
    blo = b - bhi

    err1 = x - (ahi * bhi)
    err2 = err1 - (alo * bhi)
    err3 = err2 - (ahi * blo)

    y = alo * blo - err3

    return y, x
