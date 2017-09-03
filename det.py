from compress import compress
from rsum import robust_sum as rsum
from scale import robust_scale as rscale
from two_product import two_product as tprod


def det2(m):
    e = rsum(
        tprod(m[0][0], m[1][1]),
        tprod(-m[0][1], m[1][0])
    )
    return compress(e)


def det3(m):
    e = rsum(
        rscale(
            rsum(
                tprod(m[1][1], m[2][2]),
                tprod(-m[1][2], m[2][1])
            ),
            m[0][0]
        ),
        rsum(
            rscale(
                rsum(
                    tprod(m[1][0], m[2][2]),
                    tprod(-m[1][2], m[2][0]),
                ),
                -m[0][1]
            ),
            rscale(
                rsum(
                    tprod(m[1][0], m[2][1]),
                    tprod(-m[1][1], m[2][0]),
                ),
                m[0][2]
            ),
        ),
    )
    return compress(e)
