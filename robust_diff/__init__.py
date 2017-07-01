def robust_diff(e, f):
    """
    robust subtraction
    :param e:
    :param f:
    :return:
    """
    return linear_expansion_diff(e, f)


def linear_expansion_diff(e, f):
    """
    linear expansion
    :param e:
    :param f:
    :return:
    """
    ne = len(e)
    nf = len(f)
    if ne == 1 and nf == 1:
        return scalar_scalar(e[0], -f[0])

    n = ne + nf
    g = [0] * n
    count = 0
    eptr = 0
    fptr = 0

    ei = e[eptr]
    ea = abs(ei)
    fi = -f[fptr]
    fa = abs(fi)

    if ea < fa:
        b = ei
        eptr += 1
        if eptr < ne:
            ei = e[eptr]
            ea = abs(ei)

    else:
        b = fi
        fptr += 1
        if fptr < nf:
            fi = -f[fptr]
            fa = abs(fi)

    if (eptr < ne and ea < fa) or (fptr >= nf):
        a = ei
        eptr += 1
        if eptr < ne:
            ei = e[eptr]
            ea = abs(ei)

    else:
        a = fi
        fptr += 1
        if fptr < nf:
            fi = -f[fptr]
            fa = abs(fi)

    x = a + b
    bv = x - a
    y = b - bv
    q0 = y
    q1 = x

    while eptr < ne and fptr < nf:
        if ea < fa:
            a = ei
            eptr += 1
            if eptr < ne:
                ei = e[eptr]
                ea = abs(ei)
        else:
            a = fi
            fptr += 1
            if fptr < nf:
                fi = -f[fptr]
                fa = abs(fi)

        b = q0
        x = a + b
        bv = x - a
        y = b - bv
        if y:
            g[count] = y
            count += 1

        _x = q1 + x
        _bv = _x - q1
        _av = _x - _bv
        _br = x - _bv
        _ar = q1 - _av
        q0 = _ar + _br
        q1 = _x

    while eptr < ne:
        a = ei
        b = q0
        x = a + b
        bv = x - a
        y = b - bv
        if y:
            g[count] = y
            count += 1

        _x = q1 + x
        _bv = _x - q1
        _av = _x - _bv
        _br = x - _bv
        _ar = q1 - _av
        q0 = _ar + _br
        q1 = _x
        eptr += 1
        if eptr < ne:
            ei = e[eptr]

    while fptr < nf:
        a = fi
        b = q0
        x = a + b
        bv = x - a
        y = b - bv
        if y:
            g[count] = y
            count += 1

        _x = q1 + x
        _bv = _x - q1
        _av = _x - _bv
        _br = x - _bv
        _ar = q1 - _av
        q0 = _ar + _br
        q1 = _x
        fptr += 1
        if fptr < nf:
            fi = -f[fptr]

    if q0:
        g[count] = q0
        count += 1

    if q1:
        g[count] = q1
        count += 1

    if not count:
        g[count] = 0.0
        count += 1

    return tuple(g[:count])


def scalar_scalar(a, b):
    """
    scalar sum: easy case: add two scalars
    :param a:
    :param b:
    :return:tuple
    """
    x = a + b
    bv = x - a
    av = x - bv
    br = b - bv
    ar = a - av
    y = ar + br
    if y:
        return y, x
    return (x,)
