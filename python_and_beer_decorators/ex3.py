import time

def time_me(function):
    def inner_function(n):
        t0 = time.time()
        out = function(n)
        print 'Duration', str(time.time() - t0), 's'
        return out
    return inner_function

@time_me
def square(n):
    return n ** 2

if __name__ == '__main__':
    print square(10)
