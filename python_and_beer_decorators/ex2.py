from __future__ import print_function

def my_decorator(function):
    def inner_function():
        print('Look at me, look at me, I\'m a decorator')
        function()
    return inner_function

@my_decorator
def my_function():
    print('python and beers')

my_function()
