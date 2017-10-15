from seg_intersects import segment_intersects


def addSegment(index, red, redList, blue, blueList, visit, flip):
    # Look up segment
    seg = red[index]

    # Get segment end points
    x0 , x1 = seg[0], seg[1]

    # Read out components
    a0, a1 = x0[1], x1[1]
    l0, h0 = min(a0, a1), max(a0, a1)

    # Scan over blue intervals for point
    intervals = blueList.intervals
    blueIndex = blueList.index
    count = blueList.count
    ptr = 2 * count

    for i in xrange(count - 1, 0 - 1, -1):
        ptr += -1
        h1 = intervals[ptr]
        ptr += -1
        l1 = intervals[ptr]

        # Test if intervals overlap
        if l0 <= h1 and l1 <= h0:
            bindex = blueIndex[i]
            bseg = blue[bindex]

            # Test if segments intersect
            if segment_intersects(x0, x1, bseg[0], bseg[1]):
                if flip:
                    ret = visit(bindex, index)
                else:
                    ret = visit(index, bindex)

                if ret:
                    return ret

    # Then add to red list
    redList.insert(l0, h0, index)
    return False
