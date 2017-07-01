from two_sum import two_sum
from two_product import two_product

def robust_scale(e, scale):
    """
    robust scale
    :param e:
    :param scale:
    :return:
    """
    return scaleLinearExpansion(e, scale)

def scaleLinearExpansion(e, scale):
    n = len(e)
    if n == 1:
        ts = two_product(e[0], scale)
        if ts[0]:
            return ts
        return (ts[1],)

    g = [0] * (2 * n)
    q = [0.1, 0.1]
    t = [0.1, 0.1]
    count = 0
    q = list(two_product(e[0], scale))
    if q[0]:
        g[count] = q[0]
        count += 1

    for i in range(1, n):
        t = two_product(e[i], scale)
        pq = q[1]
        q = two_sum(pq, t[0])
        if q[0]:
            g[count] = q[0]
            count += 1

        a = t[1]
        b = q[1]
        x = a + b
        bv = x - a
        y = b - bv
        q = list(q)
        q[1] = x
        if y:
            g[count] = y
            count += 1

    if q[1]:
        g[count] = q[1]
        count += 1

    if count == 0:
        g[count] = 0.0
        count += 1

    return tuple(g[:count])
