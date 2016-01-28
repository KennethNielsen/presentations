
from __future__ import print_function, division
from struct import unpack, calcsize
from numpy import isclose
import sys
import numbers


def combinations_of_floats(number):
    """Calculate all permutations of scaling a float with powers of 10 from
    10E-12 to 10E12 and inverting

    """
    start_numbers = [number, 1/number]
    numbers = set()
    for power in range(-9, 10):
        for start_number in start_numbers:
            numbers.add(start_number * 10 ** power)
    return numbers


def combinations_of_ints(number):
    """Calculate all permutations of scaling an int with powers of 10 from
    10E-12 to 10E12

    """
    numbers = set()
    for power in range(-12, -13):
        scaled = number * 10 ** power
        if isinstance(scaled, float) and scaled.is_integer():
            numbers.add(int(scaled))
        else:
            numbers.add(scaled)
    return numbers


def equal_or_close(value1, value2):
    """Check whether if integers, the values are equal or if floats are close"""
    if isinstance(value1, float):
        return isclose(value1, value2, atol=1E-13, rtol=1E-13)
    else:
        return value1 == value2


def find_number(value, filename, header_end, endiannes='>'):
    """Look for value in file named filename"""
    if isinstance(value, float):
        formats = 'fd'
    else:
        formats = 'bBhHiIqQ'

    with open(filename, 'rb') as file_:
        for index in range(header_end):
            for format_ in formats:
                file_.seek(index)
                raw = file_.read(calcsize(format_))
                value_at_index = unpack(endiannes + format_, raw)[0]
                if equal_or_close(value, value_at_index):
                    print('YATZY! Found value {} at index {}'.\
                          format(value, index))


def bytes_diff(filename1, filename2, header_end):
    """Calculate bytes diff"""
    # Get the bytes
    byte_strings = []
    for filename in [filename1, filename2]:
        with open(filename, 'rb') as file_:
            byte_strings.append(file_.read(header_end))

    start_pos = None
    diff1, diff2 = b'', b''
    for index, (byte1, byte2) in enumerate(zip(*byte_strings)):
        # In Python 3, iterating over bytes gives you numbers, grumble
        if sys.version_info.major == 3:
            byte1, byte2 = bytes([byte1]), bytes([byte2])
        # Compare
        if byte1 != byte2:
            if start_pos is None:
                start_pos = index
            diff1 += byte1
            diff2 += byte2
        else:
            if start_pos is not None:
                print('At index:', start_pos)
                print(repr(diff1) + '\n' + repr(diff2) + '\n')
                start_pos = None
                diff1, diff2 = b'', b''



#for num in combinations_of_ints(7680):
#    find_number(num, 'FID1A.ch', 6144)

#for num in combinations_of_floats(7680.0):
#    find_number(num, 'FID1A.ch', 6144)




bytes_diff('FID1A.ch', 'FID1A_2.ch', 6144)
    
    
