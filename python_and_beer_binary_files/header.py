
from __future__ import print_function
from struct import unpack, calcsize
import time


# Constants used for binary file parsing
ENDIAN = '>'
STRING = ENDIAN + '{}s'
UINT8 = ENDIAN + 'B'
UINT16 = ENDIAN + 'H'
INT16 = ENDIAN + 'h'
#INT32 = ENDIAN + 'i'


fields = (
    ('sequence_line_or_injection', 252, UINT16),
    ('injection_or_sequence_line', 256, UINT16),
    ('start_time', 282, 'x-time'),
    ('end_time', 286, 'x-time'),
    ('version_string', 326, 'utf16'),
    ('description', 347, 'utf16'),
    ('sample', 858, 'utf16'),
    ('operator', 1880, 'utf16'),
    ('date', 2391, 'utf16'),
    ('inlet', 2492, 'utf16'),
    ('instrument', 2533, 'utf16'),
    ('method', 2574, 'utf16'),
    ('software version', 3601, 'utf16'),
    ('software name', 3089, 'utf16'),
    ('software revision', 3802, 'utf16'),
    ('units', 4172, 'utf16'),
    ('detector', 4213, 'utf16'),
    ('yscaling', 4732, ENDIAN + 'd')
)


def parse_utf16_string(file_, encoding='UTF16'):
    """Parse a pascal type UTF16 encoded string from a binary file object"""
    # First read the expected number of CHARACTERS
    string_length = unpack(UINT8, file_.read(1))[0]
    # Then read and decode
    parsed = unpack(STRING.format(2 * string_length),
                    file_.read(2 * string_length))
    return parsed[0].decode(encoding)


def parse_header(file_):
    """Parse the header"""
    metadata = {}
    # Parse all metadata fields
    for name, offset, type_ in fields:
        file_.seek(offset)
        if type_ == 'utf16':
            metadata[name] = parse_utf16_string(file_)
        elif type_ == 'x-time':
            metadata[name] = unpack(ENDIAN + 'f', file_.read(4))[0] / 60000
        else:
            metadata[name] = unpack(type_, file_.read(calcsize(type_)))[0]

    # Convert date
    metadata['datetime'] = time.strptime(metadata['date'], '%d-%b-%y, %H:%M:%S')
    return metadata


with open('FID1A.ch', 'rb') as file_:
    metadata = parse_header(file_)
    for key, value in metadata.items():
        print(key, '->', value)
