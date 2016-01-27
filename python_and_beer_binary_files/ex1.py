from __future__ import print_function, division
from time import time

OUT = '{}, {} call(s), this call: {:.2e}s, on avg: {:.2e}s, total: {:.2e}s'

def timeme(function):
    timings = []
    def inner_function(*args, **kwargs):
        start = time()
        return_value = function(*args, **kwargs)
        timings.append(time() - start)
        total = sum(timings)
        print(OUT.format(function.__name__, len(timings), timings[-1], total/len(timings), total))
        return return_value
    return inner_function
