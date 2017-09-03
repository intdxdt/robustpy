"""
 Bit twiddling hacks.
 Based on Stanford bit twiddling hack library:
    http:#graphics.stanford.edu/~seander/bithacks.html
"""

INT_BITS = 32  # number of bits in an integer
INT_MAX = 0x7fffffff
INT_MIN = -1 << (INT_BITS - 1)
REVERSE_TABLE = (
    0, 128, 64, 192, 32, 160, 96, 224, 16, 144, 80, 208, 48,
    176, 112, 240, 8, 136, 72, 200, 40, 168, 104, 232, 24, 152, 88, 216, 56, 184, 120, 248, 4,
    132, 68, 196, 36, 164, 100, 228, 20, 148, 84, 212, 52, 180, 116, 244, 12, 140, 76, 204, 44,
    172, 108, 236, 28, 156, 92, 220, 60, 188, 124, 252, 2, 130, 66, 194, 34, 162, 98, 226, 18,
    146, 82, 210, 50, 178, 114, 242, 10, 138, 74, 202, 42, 170, 106, 234, 26, 154, 90, 218, 58,
    186, 122, 250, 6, 134, 70, 198, 38, 166, 102, 230, 22, 150, 86, 214, 54, 182, 118, 246, 14,
    142, 78, 206, 46, 174, 110, 238, 30, 158, 94, 222, 62, 190, 126, 254, 1, 129, 65, 193, 33,
    161, 97, 225, 17, 145, 81, 209, 49, 177, 113, 241, 9, 137, 73, 201, 41, 169, 105, 233, 25,
    153, 89, 217, 57, 185, 121, 249, 5, 133, 69, 197, 37, 165, 101, 229, 21, 149, 85, 213, 53,
    181, 117, 245, 13, 141, 77, 205, 45, 173, 109, 237, 29, 157, 93, 221, 61, 189, 125, 253, 3,
    131, 67, 195, 35, 163, 99, 227, 19, 147, 83, 211, 51, 179, 115, 243, 11, 139, 75, 203, 43,
    171, 107, 235, 27, 155, 91, 219, 59, 187, 123, 251, 7, 135, 71, 199, 39, 167, 103, 231, 23,
    151, 87, 215, 55, 183, 119, 247, 15, 143, 79, 207, 47, 175, 111, 239, 31, 159, 95, 223, 63,
    191, 127, 255
)


def sign(v):
    """
    Returns -1, 0, +1 depending on sign of x
    :param v:
    :return:
    """
    return (v > 0) - (v < 0)


def is_pow2(v):
    """
    Checks if a number is a power of two
    :param v:
    :return:
    """
    return (v != 0) and ((v & (v - 1)) == 0)


def log2(v):
    """
    Computes log base 2 of v
    :param v:
    :return:
    """
    # @formatter:off
    r = (v > 0xFFFF) << 4; v >>= r
    shift = (v > 0xFF) << 3; v >>= shift; r |= shift
    shift = (v > 0xF) << 2; v >>= shift; r |= shift
    shift = (v > 0x3) << 1; v >>= shift; r |= shift
    return r | (v >> 1)
    #@formatter:on


def log10(v):
    """
    Computes log base 10 of v
    :param v:
    :return:
    """
    lg = 0
    # @formatter:off
    if   v >= 1000000000 : lg = 9
    elif v >= 100000000 : lg = 8
    elif v >= 10000000 : lg = 7
    elif v >= 1000000 : lg = 6
    elif v >= 100000 : lg = 5
    elif v >= 10000 : lg = 4
    elif v >= 1000 : lg = 3
    elif v >= 100 : lg = 2
    elif v >= 10 : lg = 1
    return lg
    #@formatter:on


def pop_count(v):
    """
    Counts number of bits
    :param v:
    :return:
    """
    #    other solution
    #    v = v - ((v >> 1) & 0x55555555)
    #    v = (v & 0x33333333) + ((v >> 2) & 0x33333333)
    #    ((v + (v >> 4) & 0xF0F0F0F) * 0x1010101) >> 24 #i32 & u32 cause overflow on this line
    (s0, s1, s2, s3, s4) = (1, 2, 4, 8, 16)  # magic binary numbers
    (b0, b1, b2, b3, b4) = (0x55555555, 0x33333333, 0x0F0F0F0F, 0x00FF00FF, 0x0000FFFF)

    c = v - ((v >> s0) & b0)
    c = ((c >> s1) & b1) + (c & b1)
    c = ((c >> s2) + c) & b2
    c = ((c >> s3) + c) & b3
    return ((c >> s4) + c) & b4


# finding the log base 2 in parallel
# first isolate the lowest 1 bit, and then
# proceed with c starting at the maximum and decreasing
# def count_trailing_zeros(v)  {
#    v = v
#    c = 32u32
#    sv = v as i32
#    v = (sv & -sv) as u32 #NOTE: may overflow u32 -> -i32
#    if v != 0 { c -= 1 }
#    if v & 0x0000FFFF != 0 { c -= 16 }
#    if v & 0x00FF00FF != 0 { c -= 8 }
#    if v & 0x0F0F0F0F != 0 { c -= 4 }
#    if v & 0x33333333 != 0 { c -= 2 }
#    if v & 0x55555555 != 0 { c -= 1 }
#    c
# }

def count_trailing_zeros(v):
    """
    Computes the number of trailing zeros by accumulating c
    in a manner akin to binary search
    :param v:
    :return:
    """
    # @formatter:off
    c = 32
    # NOTE: if 0 == v, then c = 31.
    # short circuit v == 0 as 32
    if v == 0:
        return c
    if v & 0x1 != 0:
        c = 0  # special case for odd v (assumed to happen half of the time)
    else:
        c = 1
        if (v & 0xffff) == 0:
            v >>= 16; c += 16
        if (v & 0xff) == 0:
            v >>= 8; c += 8
        if (v & 0xf) == 0:
            v >>= 4; c += 4
        if (v & 0x3) == 0:
            v >>= 2; c += 2
        c -= v & 0x1

    return c


def next_pow2(v):
    """
    Rounds to next power of 2
    :param v:
    :return:
    """
    v += (v == 0)
    v -= 1
    v |= v >> 1
    v |= v >> 2
    v |= v >> 4
    v |= v >> 8
    v |= v >> 16
    return v + 1


def prev_pow2(v):
    """
    Rounds down to previous power of 2
    :param v:
    :return:
    """
    v |= v >> 1
    v |= v >> 2
    v |= v >> 4
    v |= v >> 8
    v |= v >> 16
    return v - (v >> 1)


def parity(v):
    """
    Computes parity of word
    :param v:
    :return:
    """
    v ^= v >> 16
    v ^= v >> 8
    v ^= v >> 4
    v &= 0xf
    return (0x6996 >> v) & 1


# fn _gen_reverse_table(table:&[i32256]) {
#  for i in  0..256 {
#     v = i
#    r = i
#    s = 7
#    v >>= 1
#    while v != 0 {
#      r <<= 1
#      r |= v & 1
#      s-=1
#      v >>= 1
#    }
#    table[i] = (r << s) & 0xff
#  }
# }


def reverse(v):
    """
    Reverse bits in a 32 bit word
    :param v:
    :return:
    """
    # @formatter:off
    return (REVERSE_TABLE[(v & 0xff)] << 24) | \
           (REVERSE_TABLE[((v >> 8)  & 0xff)] << 16) | \
           (REVERSE_TABLE[((v >> 16) & 0xff)] << 8) | \
           (REVERSE_TABLE[((v >> 24) & 0xff)])
    #@formatter:on


def interleave2(x, y):
    """
    Interleave bits of 2 coordinates with 16
    Useful for fast quadtree codes
    :param x:
    :param y:
    :return:
    """
    # @formatter:off
    x &= 0xFFFF
    x = (x | (x << 8)) & 0x00FF00FF
    x = (x | (x << 4)) & 0x0F0F0F0F
    x = (x | (x << 2)) & 0x33333333
    x = (x | (x << 1)) & 0x55555555

    y &= 0xFFFF
    y = (y | (y << 8)) & 0x00FF00FF
    y = (y | (y << 4)) & 0x0F0F0F0F
    y = (y | (y << 2)) & 0x33333333
    y = (y | (y << 1)) & 0x55555555

    return x | (y << 1)


def deinterleave2(v, n):
    """
    Extracts the nth interleaved component
    :param v:
    :param n:
    :return:
    """
    # @formatter:off
    v = (v >> n)        & 0x55555555
    v = (v | (v >> 1))  & 0x33333333
    v = (v | (v >> 2))  & 0x0F0F0F0F
    v = (v | (v >> 4))  & 0x00FF00FF
    v = (v | (v >> 16)) & 0x000FFFF
    return (v << 16) >> 16
    #@formatter:on


def interleave3(x, y, z):
    """
    Interleave bits of 3 coordinates, each with 10
    Useful for fast octree codes
    :param x:
    :param y:
    :param z:
    :return:
    """
    # @formatter:off
    x &= 0x3FF
    x = (x | (x << 16)) & 4278190335
    x = (x | (x << 8))  & 251719695
    x = (x | (x << 4))  & 3272356035
    x = (x | (x << 2))  & 1227133513

    y &= 0x3FF
    y = (y | (y << 16)) & 4278190335
    y = (y | (y << 8))  & 251719695
    y = (y | (y << 4))  & 3272356035
    y = (y | (y << 2))  & 1227133513
    x |= y << 1

    z &= 0x3FF
    z = (z | (z << 16)) & 4278190335
    z = (z | (z << 8))  & 251719695
    z = (z | (z << 4))  & 3272356035
    z = (z | (z << 2))  & 1227133513

    return x | (z << 2)


def deinterleave3(v, n):
    """
    Extracts nth interleaved component of a 3-tuple
    :param v:
    :param n:
    :return:
    """
    # @formatter:off
    v = (v >> n)        & 1227133513
    v = (v | (v >> 2))  & 3272356035
    v = (v | (v >> 4))  & 251719695
    v = (v | (v >> 8))  & 4278190335
    v = (v | (v >> 16)) & 0x3FF
    return (v << 22) >> 22




def next_combination(v):
    """
    Computes next combination in colexicographic order (this is mistakenly called
    nextPermutation on the bit twiddling hacks page)
    :param v:
    :return:
    """
    t = v | (v - 1)
    c = (~t & -~t) - 1
    return (t + 1) | (c >> (count_trailing_zeros(v) + 1))
