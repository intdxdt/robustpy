from compress import compress
from  rsum import robust_sum as rsum
from  scale import robust_scale as  rscale
from  two_product import two_product as tprod
from  seg_intersects import segment_intersects


# Robust segment intersection of line segments
def segment_intersection(a, b, c, d):
    return exact_intersect(a, b, c, d)


# Find solution to system of two linear equations
#  | a[0]  a[1]   1 |
#  | b[0]  b[1]   1 |  =  0
#  |  x      y    1 |
#
#  | c[0]  c[1]   1 |
#  | d[0]  d[1]   1 |  =  0
#  |  x      y    1 |
#
def exact_intersect(a, b, c, d):
    if not segment_intersects(a, b, c, d):
        return [[0.], [0.], [0.]]

    x1 = rsum([c[1]], [-d[1]])
    y1 = rsum([-c[0]], [d[0]])

    denom = rsum(
        rsum(rscale(y1, a[1]), rscale(y1, -b[1])),
        rsum(rscale(x1, a[0]), rscale(x1, -b[0])),
    )

    w0 = rsum(tprod(-a[0], b[1]), tprod(a[1], b[0]))
    w1 = rsum(tprod(-c[0], d[1]), tprod(c[1], d[0]))

    # Calculate nX, nY
    nx = rsum(
        rsum(rscale(w1, a[0]), rscale(w1, -b[0])),
        rsum(rscale(w0, -c[0]), rscale(w0, d[0])),
    )

    ny = rsum(
        rsum(rscale(w1, a[1]), rscale(w1, -b[1])),
        rsum(rscale(w0, -c[1]), rscale(w0, d[1])),
    )

    return [compress(nx), compress(ny), compress(denom)]
