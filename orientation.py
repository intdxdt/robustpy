from robust_diff import robust_subtract
from scale import robust_scale
from rsum import robust_sum
from two_product import two_product

EPSILON = 1.1102230246251565e-16
ERRBOUND3 = (3.0 + 16.0 * EPSILON) * EPSILON
ERRBOUND4 = (7.0 + 56.0 * EPSILON) * EPSILON

sub = robust_subtract
sum = robust_sum
prod = two_product
scale = robust_scale


def orientation1d(a, b):
    """
    orientation 1d space
    :param a:
    :param b:
    :return:
    """
    return b[0] - a[0]


def orientation2d(a, b, c):
    """
    orientation in 2d space
    :param a:
    :param b:
    :param c:
    :return:
    """
    l = (a[1] - c[1]) * (b[0] - c[0])
    r = (a[0] - c[0]) * (b[1] - c[1])
    det = l - r
    if l > 0:
        if r <= 0:
            return det
        else:
            s = l + r

    elif l < 0:
        if r >= 0:
            return det
        else:
            s = -(l + r)
    else:
        return det

    tol = ERRBOUND3 * s
    if det >= tol or det <= -tol:
        return det

    return orientation3Exact(a, b, c)


def orientation3d(a, b, c, d):
    """
    orientation in 3d space
    :param a:
    :param b:
    :param c:
    :param d:
    :return:
    """
    adx = a[0] - d[0]
    bdx = b[0] - d[0]
    cdx = c[0] - d[0]
    ady = a[1] - d[1]
    bdy = b[1] - d[1]
    cdy = c[1] - d[1]
    adz = a[2] - d[2]
    bdz = b[2] - d[2]
    cdz = c[2] - d[2]
    bdxcdy = bdx * cdy
    cdxbdy = cdx * bdy
    cdxady = cdx * ady
    adxcdy = adx * cdy
    adxbdy = adx * bdy
    bdxady = bdx * ady
    det = (
        adz * (bdxcdy - cdxbdy) +
        bdz * (cdxady - adxcdy) +
        cdz * (adxbdy - bdxady)
    )

    permanent = (
        (abs(bdxcdy) + abs(cdxbdy)) * abs(adz) +
        (abs(cdxady) + abs(adxcdy)) * abs(bdz) +
        (abs(adxbdy) + abs(bdxady)) * abs(cdz)
    )

    tol = ERRBOUND4 * permanent

    if (det > tol) or (-det > tol):
        return det

    return orientation4Exact(a, b, c, d)


def orientation3Exact(m0, m1, m2):
    """
    orientation 2d exact
    :param m0:
    :param m1:
    :param m2:
    :return:
    """
    p = sum(
        sum(prod(m1[1], m2[0]), prod(-m2[1], m1[0])),
        sum(prod(m0[1], m1[0]), prod(-m1[1], m0[0]))
    )
    n = sum(prod(m0[1], m2[0]), prod(-m2[1], m0[0]))
    d = sub(p, n)
    return d[-1]


def orientation4Exact(m0, m1, m2, m3):
    p = sum(
        sum(
            scale(sum(prod(m2[1], m3[0]), prod(-m3[1], m2[0])), m1[2]),
            sum(
                scale(sum(prod(m1[1], m3[0]), prod(-m3[1], m1[0])), -m2[2]),
                scale(sum(prod(m1[1], m2[0]), prod(-m2[1], m1[0])), m3[2])
            )
        ),
        sum(
            scale(sum(prod(m1[1], m3[0]), prod(-m3[1], m1[0])), m0[2]),
            sum(
                scale(sum(prod(m0[1], m3[0]), prod(-m3[1], m0[0])), -m1[2]),
                scale(sum(prod(m0[1], m1[0]), prod(-m1[1], m0[0])), m3[2])
            )
        )
    )

    n = sum(
        sum(
            scale(sum(prod(m2[1], m3[0]), prod(-m3[1], m2[0])), m0[2]),
            sum(
                scale(sum(prod(m0[1], m3[0]), prod(-m3[1], m0[0])), -m2[2]),
                scale(sum(prod(m0[1], m2[0]), prod(-m2[1], m0[0])), m3[2])
            )
        ),
        sum(
            scale(sum(prod(m1[1], m2[0]), prod(-m2[1], m1[0])), m0[2]),
            sum(
                scale(sum(prod(m0[1], m2[0]), prod(-m2[1], m0[0])), -m1[2]),
                scale(sum(prod(m0[1], m1[0]), prod(-m1[1], m0[0])), m2[2])
            )
        )
    )
    d = sub(p, n)
    return d[-1]
