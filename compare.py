from subtract import robust_subtract


def robust_compare(a, b):
    return robust_subtract(a, b)[-1]
