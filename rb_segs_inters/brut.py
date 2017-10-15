# It is silly, but this is faster than doing the right thing for up to a
# few thousand segments, which hardly occurs in practice.
class BruteForceList(object):
    def __init__(self, capacity):
        self.intervals = [None] * (2 * capacity)
        self.index = [None] * capacity  # pool.mallocInt32(capacity)
        self.count = 0

    def insert(self, lo, hi, index):
        count = self.count
        self.index[count] = index
        self.intervals[2 * count] = lo
        self.intervals[2 * count + 1] = hi
        self.count += 1

    def remove(self, index):
        count = self.count
        rindex = self.index
        intervals = self.intervals
        for i in xrange(count - 1, 0 - 1, -1):
            if rindex[i] == index:
                rindex[i] = rindex[count - 1]
                intervals[2 * i] = intervals[2 * (count - 1)]
                intervals[2 * i + 1] = intervals[2 * count - 1]
                self.count -= 1
                return
