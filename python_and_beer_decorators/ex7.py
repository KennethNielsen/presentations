from __future__ import print_function

def callstring(*args, **kwargs):
    arglist = [repr(arg) for arg in args]
    arglist += [key + "=" + str(kwarg)
                for key, kwarg in list(kwargs.items())]
    return ', '.join(arglist)

LEVEL = -1

def spec_me(function):
    def inner_function(*args, **kwargs):
        global LEVEL
        LEVEL += 1
        argstring = callstring(*args, **kwargs)
        print('{}+{}({})'.format('|' * LEVEL,
                                 function.__name__,
                                 argstring))
        out = function(*args, **kwargs)
        print('{}>{}'.format('|' * LEVEL, out))
        LEVEL -= 1
        return out
    return inner_function

@spec_me
def square(n):
    return n ** 2

@spec_me
def speak_squares(n):
    return '{} squared is {}'.format(n, square(n))

speak_squares(10)
