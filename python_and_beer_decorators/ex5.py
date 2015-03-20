from __future__ import print_function
import time

def time_me_cumulative(function):
    def inner_function(*args, **kwargs):
        t0 = time.time()
        out = function(*args, **kwargs)
        delta = time.time() - t0
        inner_function.cumsum += delta
        print("This run:", delta, "in total:",
              inner_function.cumsum)
        return out
    inner_function.cumsum = 0
    return inner_function

@time_me_cumulative
def square(n, repeat=1):
    for _ in range(repeat):
        out = n ** 2
    return out

square(10, 10**6)
square(10, 10**6)






