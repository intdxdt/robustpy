from rsum import robust_sum as rsum
from scale import robust_scale as rscale


def robust_product(a, b):
    """
    Robust product
    :param a:
    :param b:
    :return:
    """
    if len(a) == 1:
        return rscale(b, a[0])

    if len(b) == 1:
        return rscale(a, b[0])

    if len(a) == 0 or len(b) == 0:
        return [0]

    r = [0]
    if len(a) < len(b):
        for i in range(0, len(a)):
            r = rsum(r, rscale(b, a[i]))

    else:
        for i in range(0, len(b)):
            r = rsum(r, rscale(a, b[i]))
    return r
