from __future__ import print_function
import time

def time_me(function):
    def inner_function(*args, **kwargs):
        t0 = time.time()
        out = function(*args, **kwargs)
        print('Duration', str(time.time() - t0), 's')
        return out
    return inner_function

@time_me
def square(n, repeat=1):
    for _ in range(repeat):
        out = n ** 2
    return out

print(square(10))
print()
print(square(10, 10**6))






