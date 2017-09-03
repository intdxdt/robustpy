from test_overlap import test_overlap


def validate_sequence(x):
    n = len(x)
    if n < 1:
        return False

    for i in range(1, n):
        if abs(x[i - 1]) >= abs(x[i]):
            return False

        if test_overlap(x[i], x[i - 1]):
            return False

    return True
