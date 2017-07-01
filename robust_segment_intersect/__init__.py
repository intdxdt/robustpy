from robust_orient import orientation2d

def segments_intersect(a0, a1, b0, b1):
    x0 = orientation2d(a0, b0, b1)
    y0 = orientation2d(a1, b0, b1)

    if (x0 > 0 and y0 > 0) or (x0 < 0 and y0 < 0):
        return False

    x1 = orientation2d(b0, a0, a1)
    y1 = orientation2d(b1, a0, a1)

    if (x1 > 0 and y1 > 0) or (x1 < 0 and y1 < 0):
        return False

    # check for degenerate collinear case
    if x0 == 0 and y0 == 0 and x1 == 0 and y1 == 0:
        return check_collinear(a0, a1, b0, b1)

    return True

def check_collinear(a0, a1, b0, b1):
    for d in xrange(0, 2):
        x0 = a0[d]
        y0 = a1[d]
        l0 = min(x0, y0)
        h0 = max(x0, y0)

        x1 = b0[d]
        y1 = b1[d]
        l1 = min(x1, y1)
        h1 = max(x1, y1)

        if h1 < l0 or h0 < l1:
            return False
    return True
