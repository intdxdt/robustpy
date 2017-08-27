import struct


def write_f64(n):
    """
    write to buffer as f64
    :param n:
    :return:
    """
    return struct.pack('<d', n)


def write_u32s(lo, hi):
    """
    write low and high into of u32 into 8bytes
    :param hi:
    :param lo:
    :return:
    """
    return struct.pack('<II', lo, hi)


def read_u32(buf):
    """
    read buffer as two uint32
    :param buf:
    :return:
    """
    return struct.unpack('<II', buf)


def read_f64(buf):
    """
    read buffer as f64
    :param buf:
    :return:
    """
    return struct.unpack('<d', buf)


def db(n):
    """
    pack as double(8bytes) and unpack as uint32(4,4 bytes)
    :param n:
    :return:
    """
    return read_u32(write_f64(n))


def pack(lo, hi):
    """
    pack low and high u32 and read as f64
    :param lo:
    :param hi:
    :return:
    """
    return read_f64(write_u32s(lo, hi))[0]


def lo(n):
    """
    read first 4bytes of 8byte
    :param n:
    :return:
    """
    return read_u32(write_f64(n))[0]


def hi(n):
    """
    read last 4bytes of 8byte
    :param n:
    :return:
    """
    return read_u32(write_f64(n))[1]


def sign(n):
    return hi(n) >> 31


def exponent(n):
    b = hi(n)
    return ((b << 1) >> 21) - 1023


def fraction(n):
    l = lo(n)
    h = hi(n)
    b = h & ((1 << 20) - 1)
    if (h & 0x7ff00000) != 0:
        b += 1 << 20
    return l, b


def denormalized(n):
    h = hi(n)
    return (h & 0x7ff00000) == 0

