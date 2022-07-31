from time import time

def performance(fn):
    def wrap_func(*args, **kwargs):
        t1 = time()
        result =fn(*args, **kwargs)
        t2 = time()
        print (f'it took {t2-t1} seconds to run this function')
        return result
    return wrap_func


@performance
def function():
    for x in range(1000000):
        x*5
        
function()