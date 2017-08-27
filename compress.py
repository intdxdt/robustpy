def compress(e):
    return compress_expansion(e)

def compress_expansion(e):
    e = list(e)
    m = len(e)
    Q = e[-1]
    bottom = m
    for i in xrange(m - 2, 0 - 1, -1):
        a = Q
        b = e[i]
        Q = a + b
        bv = Q - a
        q = b - bv
        if q != 0.0:
            bottom -= 1
            e[bottom] = Q
            Q = q
    top = 0
    for i in xrange(bottom, m):
        a = e[i]
        b = Q
        Q = a + b
        bv = Q - a
        q = b - bv
        if q != 0.0:
            e[top] = q
            top += 1
    e[top] = Q
    top += 1
    return tuple(e[0:top])
