from rb_segs_inters import rbSegIntersection


def rbinters(red, blue):
    crossings = []

    def visit(i, j):
        crossings.append((i, j))

    rbSegIntersection(red, blue, visit)
    return crossings
