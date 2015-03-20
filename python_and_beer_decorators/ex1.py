from __future__ import print_function

def my_decorator(function):
    return function

@my_decorator
def my_function():
    print('python and beers')

my_function()
