
from __future__ import print_function
from functools import partial

# replace args
def print_power(power, value):
    print(value ** power)

print('\n\nReplace args')

print_power(2, 4)

print_squares = partial(print_power, 2)
print_squares(8)

# replace kwargs
def themed_print_power(power, value, prefix='The answer is'):
    print(prefix, value ** power)

print('\n\nReplace kwargs')

themed_print_power(2, 4)
themed_print_power(2, 6.48074069840786, prefix='Little facts:')

homer_print_power = partial(themed_print_power, prefix='D\'oh!')
homer_print_power(3, 4)
