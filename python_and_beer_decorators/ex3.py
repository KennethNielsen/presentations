from __future__ import print_function
import time

def time_me(function):
    def inner_function(arg0):
        t0 = time.time()
        out = function(arg0)
        print('Duration', time.time() - t0, 's')
        return out
    return inner_function

@time_me
def square(n):
    return n ** 2

if __name__ == '__main__':
    print(square(10))
