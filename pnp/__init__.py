from robust_orient import orientation2d as orient


def robust_pt_in_polygon(vs, point):
    x = point[0]
    y = point[1]
    n = len(vs)
    inside = 1
    lim = n
    i = 0
    j = n - 1

    while i < lim:
        a = vs[i]
        b = vs[j]
        yi = a[1]
        yj = b[1]

        if yj < yi:
            if yj < y < yi:
                s = orient(a, b, point)
                if s == 0:
                    return 0
                else:
                    inside ^= (0 < s) | 0

            elif y == yi:
                c = vs[(i + 1) % n]
                yk = c[1]
                if yi < yk:
                    s = orient(a, b, point)
                    if s == 0:
                        return 0
                    else:
                        inside ^= (0 < s) | 0

        elif yi < yj:
            if yi < y < yj:
                s = orient(a, b, point)
                if s == 0:
                    return 0
                else:
                    inside ^= (s < 0) | 0

            elif y == yi:
                c = vs[(i + 1) % n]
                yk = c[1]
                if yk < yi:
                    s = orient(a, b, point)
                    if s == 0:
                        return 0
                    else:
                        inside ^= (s < 0) | 0

        elif y == yi:
            x0 = min(a[0], b[0])
            x1 = max(a[0], b[0])
            if i == 0:
                while j > 0:
                    k = (j + n - 1) % n
                    p = vs[k]
                    if p[1] != y:
                        break

                    px = p[0]
                    x0 = min(x0, px)
                    x1 = max(x1, px)
                    j = k

                if j == 0:
                    if x0 <= x <= x1:
                        return 0

                    return 1

                lim = j + 1

            y0 = vs[(j + n - 1) % n][1]

            while i + 1 < lim:
                p = vs[i + 1]
                if p[1] != y:
                    break

                px = p[0]
                x0 = min(x0, px)
                x1 = max(x1, px)
                i += 1

            if x0 <= x <= x1:
                return 0

            y1 = vs[(i + 1) % n][1]
            if x < x0 and (y0 < y != y1 < y):
                inside ^= 1

        j = i
        i += 1

    return 2 * inside - 1
