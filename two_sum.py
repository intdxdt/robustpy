def two_sum(a, b):
    """
    fast two sum
    :param a:
    :param b:
    :return:
    """
    x = a + b
    bv = x - a
    av = x - bv
    br = b - bv
    ar = a - av
    return ar + br, x
