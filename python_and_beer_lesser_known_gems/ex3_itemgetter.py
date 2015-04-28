"""Itemgetter demonstration"""

from __future__ import print_function
from pprint import pprint
from operator import itemgetter, attrgetter
from random import randint
import copy

def itemgette_demonstration():
    """Main function"""
    test_data1 = [[randint(0, 10), randint(0, 10)] for _ in range(10)]
    test_data2 = copy.copy(test_data1)

    print('Input data')
    pprint(test_data1)
    print('Test data equal:', test_data1 == test_data2)

    # Sort by secod item in inner lists with lambda :(
    test_data1.sort(key=lambda item: item[1])
    # And with the itemgetter
    test_data2.sort(key=itemgetter(1))

    print('\nOutput data')
    pprint(test_data1)
    print('Output data equal:', test_data1 == test_data2)


if __name__ == '__main__':
    itemgette_demonstration()
