from __future__ import print_function

def get_argstring(*args, **kwargs):
    arglist = [str(arg) for arg in args]
    arglist += ['{}={}'.format(key, kwarg)
                for key, kwarg in kwargs.items()]
    return ', '.join(arglist)

def spec_me(function):
    def inner_function(*args, **kwargs):
        argstring = get_argstring(*args, **kwargs)
        print('+{}({})'.format(function.__name__,
                               argstring))
        out = function(*args, **kwargs)
        print('>{}'.format(out))
        return out
    return inner_function

@spec_me
def square(n, repeat=1):
    for _ in range(repeat):
        out = n ** 2
    return out

square(10)
square(10, repeat=2)
