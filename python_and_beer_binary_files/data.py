
"""22800 points, data starts at 0x1800 = 6144"""


from __future__ import unicode_literals, print_function
from struct import unpack
import numpy
from ex1 import timeme


@timeme
def version1():
    """Parse until there are no more bytes"""
    data = []
    with open('FID1A.ch', 'rb') as file_:
        file_.seek(6144)
        raw = file_.read(8)
        while len(raw) == 8:
            data.append(unpack('<d', raw)[0])
            raw = file_.read(8)
    return numpy.array(data)


@timeme
def version2():
    """Calculate the number of points before hand"""
    with open('FID1A.ch', 'rb') as file_:
        file_.seek(0, 2)  # Seek to the end of the file
        end = file_.tell()
        num_points = (end - 6144) // 8
        file_.seek(6144)
        raw = file_.read(end - 6144)
        data = unpack('<{}d'.format(num_points), raw)
    return numpy.array(data)


@timeme
def version3():
    """Calculate number of points and parse directly into numpy array"""
    with open('FID1A.ch', 'rb') as file_:
        file_.seek(0, 2)  # Seek to the end of the file
        end = file_.tell()
        num_points = (end - 6144) // 8
        file_.seek(6144)
        data = numpy.fromfile(file_, dtype='<d', count=num_points)
    return data


ver1 = version1()
ver2 = version2()
ver3 = version3()


from matplotlib import pyplot as plt
plt.plot(ver1)
plt.plot(ver2 + 1000)
plt.plot(ver3 + 2000)
plt.show()
       
