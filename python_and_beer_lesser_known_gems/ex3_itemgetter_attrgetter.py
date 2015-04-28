"""Itemgetter demonstration"""

from __future__ import print_function
from pprint import pprint
from operator import itemgetter, attrgetter
from random import randint
import copy


### itemgetter
def itemgetter_demonstration():
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


### attrgetter
class TestItem(object):
    """Class for this fancy test"""

    def __init__(self, number):
        self.name = 'Number:{}'.format(number)
        self.value = randint(0, 10)

    def __repr__(self):
        return '<TestItem {} with value {}>'.format(self.name, self.value)


def attrgetter_demonstration():
    """attrgetter demonstration"""
    objects = [TestItem(n) for n in range(10)]
    print('\n\n### attrgetter demonstration\nInitial data')
    pprint(objects)

    # labmda solution (yikes):
    #objects.sort(key=lambda item: item.value)

    # Nice solution:
    objects.sort(key=attrgetter('value'))

    print('Output')
    pprint(objects)


if __name__ == '__main__':
    #itemgetter_demonstration()
    attrgetter_demonstration()
