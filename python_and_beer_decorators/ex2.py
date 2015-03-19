def my_decorator(function):
    print 'Look at me, look at me, I\'m a decorator'
    return function

@my_decorator
def my_function():
    print 'python and beers'

my_function()
