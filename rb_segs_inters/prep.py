import ev
from util import lexsort3d
# import  numpy as np

def prepareEvts(red, blue):
    nr = len(red)
    nb = len(blue)
    n = nr + nb
    data = [None] * (2 * n)
    # data = np.zeros(((2 * n), 3))

    ptr = 0

    for i in xrange(0, nr):
        seg = red[i]
        x, y = seg[0][0], seg[1][0]

        data[ptr] = (min(x, y), ev.CREATE_RED, i)
        ptr += 1

        data[ptr] = (max(x, y), ev.REMOVE_RED, i)
        ptr += 1

    for i in xrange(0, nb):
        seg = blue[i]
        x, y = seg[0][0], seg[1][0]

        data[ptr] = (min(x, y), ev.CREATE_BLUE, i)
        ptr += 1

        data[ptr] = (max(x, y), ev.REMOVE_BLUE, i)
        ptr += 1

    data.sort(cmp=lexsort3d)
    # data = data[np.lexsort(data.T[::-1])]
    return data