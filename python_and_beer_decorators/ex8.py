from __future__ import print_function

def memory(function):
    cache = {}
    def inner_function(n):
        if n not in cache:
            cache[n] = function(n)
        return cache[n]
    return inner_function


def memory2(function):
    def inner_function(n):
        if n not in inner_function.cache:
            inner_function.cache[n] = function(n)
        return inner_function.cache[n]
    inner_function.cache = {}
    return inner_function


from ex3 import time_me

@time_me
@memory
def expensive(n):
    for n in range(10**7):
        out = n ** 2
    return out

out1 = expensive(8)
out2 = expensive(8)
print(out1 == out2)

        
