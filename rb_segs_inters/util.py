import sys

def lexsort3d(a, b):
    """
    sort 3d coordinates lexicographically
    :return:
    """

    d = a[0] - b[0]
    if float_equal(d, 0):
        d = a[1] - b[1]
    else:
        return -1 if d < 0 else 1

    if float_equal(d, 0):
        d = a[2] - b[2]
    else:
        return -1 if d < 0 else 1

    return 0 if float_equal(d, 0) else (-1 if d < 0 else 1)


def float_equal(a, b, eps=1.0e-10):
    """
    float_equal compare the equality of floats
    Ref: http://floating-point-gui.de/errors/comparison/
    compare floating point precision
    :param eps:
    :param b:
    :param a:
    """
    absA = abs(a)
    absB = abs(b)
    diff = abs(a - b)

    if a == b:
        # shortcut, handles infinities
        return True
    elif a == 0.0 or b == 0.0 or diff < eps:
        # a or b is zero or both are extremely close to it
        # relative error is less meaningful here
        return (diff < eps) or (diff < (eps * eps))
    # use relative error
    return (diff / min((absA + absB), sys.float_info.max)) < eps
